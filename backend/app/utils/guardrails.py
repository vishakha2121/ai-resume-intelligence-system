import re

def remove_pii(text):
    # Remove emails, phone numbers, names (simple)
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL]', text)
    text = re.sub(r'\b\d{10}\b', '[PHONE]', text)
    return text

def check_bias_threshold(bias_score, threshold=0.7):
    if bias_score > threshold:
        return {"flag": True, "message": "High bias detected, human review recommended"}
    return {"flag": False, "message": "Bias within acceptable limits"}

def validate_input(file_content, max_size_mb=10):
    if len(file_content) > max_size_mb * 1024 * 1024:
        return False, "File too large"
    return True, "OK"