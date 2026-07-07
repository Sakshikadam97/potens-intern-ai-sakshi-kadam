from agent import triage

def test_priority():
    result = triage("Unable to login after password reset")
    assert result["priority"] == "P1"

def test_missing():
    result = triage("")
    assert result is not None

def test_nomatch():
    result = triage("I like pizza")
    assert result["category"] == "General Query"

def test_account_access():
    result = triage("Unable to login after password reset")
    assert result["category"] == "Account Access"

def test_billing():
    result = triage("I was charged twice for my subscription")
    assert result["category"] == "Billing"