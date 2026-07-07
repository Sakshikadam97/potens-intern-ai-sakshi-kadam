import os
import json
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

from prompts import SYSTEM_PROMPT
from tools import lookup_tool, search_tool, draft_tool


# Load .env
load_dotenv()

# Get API key
key = os.getenv("GEMINI_API_KEY")

if not key:
    raise ValueError("GEMINI_API_KEY not found in .env file")


# Configure Gemini
genai.configure(api_key=key)

# Model
model = genai.GenerativeModel("gemini-2.5-flash")


def triage(text):

    prompt = f"""
{SYSTEM_PROMPT}

You are a customer support triage agent.

Choose one category:
- Account Access
- Billing
- Technical Issue
- Complaint
- Feature Request
- General Query

Choose priority:
- P0 = security breach, production outage, complete system failure
- P1 = login issue, payment issue, major technical issue
- P2 = feature request, general query, minor complaint


Available tools:
- lookup_tool
- search_tool
- draft_tool


Return ONLY JSON:

{{
 "category":"",
 "priority":"",
 "tool":"",
 "reasoning":"",
 "why":""
}}


Customer ticket:

{text}

"""

    try:
        response = model.generate_content(prompt)

        # Remove markdown if Gemini adds ```json
        output = response.text.replace("```json", "").replace("```", "").strip()

        decision = json.loads(output)

    except Exception as e:
        return {
            "error": str(e)
        }


    # Gemini selected the tool
    tool = decision["tool"]


    if tool == "lookup_tool":

        tool_result = lookup_tool(text)


    elif tool == "search_tool":

        tool_result = search_tool(text)


    elif tool == "draft_tool":

        tool_result = draft_tool(text)


    else:

        tool_result = "No tool selected"



    result = {

        "category": decision["category"],

        "priority": decision["priority"],

        "next_tool": tool,

        "reasoning": decision["reasoning"],

        "why": decision["why"],

        "trace": [
    "Received customer ticket",
    f"Identified issue type: {decision['category']}",
    f"Assigned priority: {decision['priority']}",
    f"Selected tool: {tool}",
    "Executed selected tool successfully"
],
        "tool_output": tool_result

    }


    # Save output automatically

    filename = datetime.now().strftime(
        "outputs/response_%Y%m%d_%H%M%S.json"
    )


    with open(filename, "w") as f:

        json.dump(result, f, indent=4)


    return result