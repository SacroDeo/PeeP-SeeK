from allfinder.phone_lookup import phone_lookup

# 🔎 Test input
phone = "+919019965028"  # Example: Google USA

result = phone_lookup(phone)

print("=== Offline Validation ===")
offline = result.get("offline_validation", {})
if "error" in offline:
    print("Error:", offline["error"])
else:
    for k, v in offline.items():
        print(f"{k}: {v}")

print("\n=== Numverify API Data ===")
api_data = result.get("api_validation", {})
if "error" in api_data:
    print("Error:", api_data["error"])
else:
    for k, v in api_data.items():
        print(f"{k}: {v}")
