from allfinder.username_lookup import search_username
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__ == "__main__":
    username = input("Enter a username to search: ").strip()
    if username:
        result = search_username(username)
        print("Search Result:", result)
    else:
        print("Please enter a valid username.")
