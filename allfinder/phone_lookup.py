import requests
import yaml
from pathlib import Path

# Load API keys
CONFIG_PATH = Path(__file__).parent.parent / "config" / "api_keys.yaml"
with open(CONFIG_PATH, "r") as f:
    API_KEYS = yaml.safe_load(f)

def numverify_lookup(phone_number):
    api_key = API_KEYS.get("numverify")
    if not api_key:
        return {"error": "No Numverify API key configured."}
    
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"
    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        if not data.get("valid"):
            return {"error": "Invalid number or not found."}
        
        return {
            "valid": data.get("valid"),
            "number": data.get("international_format"),
            "country_name": data.get("country_name"),
            "location": data.get("location"),
            "carrier": data.get("carrier"),
            "line_type": data.get("line_type")
        }
    except Exception as e:
        return {"error": str(e)}

def phone_lookup(phone_number):
    online = numverify_lookup(phone_number)

    return {
        "api_validation": online
    }
