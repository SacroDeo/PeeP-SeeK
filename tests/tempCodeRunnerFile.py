import pandas as pd
from allfinder.email_lookup import email_lookup

# Test email
email = "vijayck1610@gmail.com"
result = email_lookup(email)

# Handle domain emails
domain_emails = result.get("domain_emails", [])
if isinstance(domain_emails, list) and domain_emails:
    df = pd.DataFrame(domain_emails)
    print(df)
else:
    print("No domain emails found.")

# Print social media data
print("\nSocial Media Info:")
social_data = result.get("social_media", {})
for site, status in social_data.items():
    print(f"{site}: {status}")
