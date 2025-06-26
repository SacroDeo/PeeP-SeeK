import requests
import subprocess
import yaml
from pathlib import Path

# Load API keys
CONFIG_PATH = Path(__file__).parent.parent / "config" / "api_keys.yaml"
if CONFIG_PATH.exists():
    with open(CONFIG_PATH, "r") as f:
        API_KEYS = yaml.safe_load(f)
else:
    API_KEYS = {}

def check_social_media(email):
    try:
        result = subprocess.run(
            ["holehe", email, "--no-color", "--no-clear", "--only-used"],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode != 0:
            return {"error": result.stderr.strip()}

        output = result.stdout.splitlines()
        social_data = {}

        for line in output:
            line = line.strip()
            if line.startswith("[+]"):
                site = line.replace("[+]", "").strip()
                social_data[site] = True
            elif line.startswith("[-]"):
                site = line.replace("[-]", "").strip()
                social_data[site] = False
            elif line.lower().startswith("[x]"):
                site = line.replace("[x]", "").strip()
                social_data[site] = "rate_limited"

        return social_data if social_data else {}
    except Exception as e:
        return {"error": str(e)}

def check_domain_emails(email):
    domain = email.split("@")[-1]
    if "hunter" not in API_KEYS:
        return {"error": "Hunter.io API key not found"}

    try:
        response = requests.get(
            f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={API_KEYS['hunter']}"
        )
        if response.status_code != 200:
            return {"error": f"Hunter API error: {response.text}"}
        return response.json().get("data", {}).get("emails", [])
    except Exception as e:
        return {"error": str(e)}

def email_lookup(email):
    return {
        "social_media": check_social_media(email),
        "domain_emails": check_domain_emails(email)
    }
