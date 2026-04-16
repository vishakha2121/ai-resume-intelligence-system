import re

def detect_bias(resume_text, parsed_json):
    import json
    data = json.loads(parsed_json) if isinstance(parsed_json, str) else parsed_json
    name = data.get("name", "")
    
    # Age bias from graduation year
    years = re.findall(r'\b(19[0-9]{2}|20[0-2][0-9])\b', resume_text)
    age_bias = 0.0
    if years:
        latest = max(int(y) for y in years)
        age_estimate = 2026 - latest
        if age_estimate > 55:
            age_bias = 0.8
        elif age_estimate < 22:
            age_bias = 0.4
    
    # Gender and race biases are not evaluated in this practice version
    gender_bias = 0.0
    race_bias = 0.0
    overall_flag = 1 if (gender_bias > 0.5 or age_bias > 0.5 or race_bias > 0.5) else 0
    details = f"Age bias: {age_bias:.2f} (from graduation year). Gender and race bias not evaluated."
    
    return {
        "gender_bias": gender_bias,
        "age_bias": age_bias,
        "race_bias": race_bias,
        "overall_flag": overall_flag,
        "details": details
    }