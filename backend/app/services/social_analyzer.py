import requests
from app.config import config

def fetch_github_data(username):
    url = f"https://api.github.com/users/{username}/events/public"
    headers = {}
    if config.GITHUB_TOKEN:
        headers["Authorization"] = f"token {config.GITHUB_TOKEN}"
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code == 200:
            events = resp.json()
            # Summarize activity
            text = f"User {username} has made {len(events)} recent events. "
            for e in events[:5]:
                text += f"{e['type']} on {e.get('repo',{}).get('name','')}. "
            return text
    except:
        pass
    return ""

def analyze_behavior(text):
    # Simple rule-based personality (mock)
    # In practice, use Gemini or a small BERT model
    openness = 0.7 if "creative" in text.lower() or "explore" in text.lower() else 0.5
    conscientiousness = 0.8 if "deadline" in text.lower() or "organized" in text.lower() else 0.5
    extraversion = 0.6 if "team" in text.lower() or "lead" in text.lower() else 0.4
    agreeableness = 0.7 if "help" in text.lower() or "collaborat" in text.lower() else 0.5
    neuroticism = 0.3 if "stress" in text.lower() else 0.5
    risk = 0.4 if "job hop" in text.lower() or "contract" in text.lower() else 0.2
    return {
        "openness": openness,
        "conscientiousness": conscientiousness,
        "extraversion": extraversion,
        "agreeableness": agreeableness,
        "neuroticism": neuroticism
    }, risk