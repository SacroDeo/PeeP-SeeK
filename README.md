# 🕵️‍♂️ PeeP-SeeK

**PeeP-SeeK** is an OSINT (Open Source Intelligence) tool built with Python and Flask that allows you to find publicly available information related to a **username**, **email**, **phone number** across multiple platforms.

It integrates powerful modules like [Sherlock](https://github.com/sherlock-project/sherlock) to track usernames across social networks and other lookup tools to fetch online traces of individuals.

---

## 📂 Project Structure

PeeP-SeeK/
├── allfinder/ # Core search modules
│ ├── username_lookup.py # Username search using Sherlock
│ ├── email_lookup.py
│ ├── phone_lookup.py
│ 
├── sherlock/ # Sherlock fork (runs via Poetry)
├── tests/ # Module tests
│ ├── test_username.py
│ └── ...
├── templates/
│ └── index.html # Web interface
├── static/
│ └── style.css # Styling for the web UI
├── app.py # Flask application
├── requirements.txt
├── setup.py
└── README.md


---

## 🚀 Features

- 🔎 **Email Lookup**: Get details about an email address using OSINT sources.
- 📞 **Phone Number Lookup**: Retrieve public information related to a phone number.
- 👤 **Username Lookup**: Search for a username across multiple websites (via Sherlock).
- 🌐 **Web Interface**: Simple web page to input and search for emails, phones, and usernames.
- ✅ **Testing**: Built-in unit tests for reliability and future development.

**Note:**
- You can either do testing by running the test files or un the webpage locally  
---

## 🔧 Requirements

- Python 3.8 or above
- `pip` package manager

---

## 📦 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/allfinder.git
cd allfinder


2. **Create a Virtual Environment (optional but recommended)**

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies**
pip install -r requirements.txt


4. **Set up API Keys (Proxies is optional)
**Note:**
 - Setting up api keys is necessary 
 - You will need two api keys
   1. hunter.io api 

🔐 How to Get an API Key from Hunter.io

 Step 1: Create a Hunter.io Account
- Go to https://hunter.io
- Click “Sign up” 
- Register using:
- Your email address, or
- Sign in with Google
 Free plans are available — you’ll get limited monthly API calls (usually 25).

 Step 2: Access the Dashboard
- Once signed in:
- You'll land in the Hunter dashboard
- On the left sidebar, click “API” or go to:
- https://hunter.io/api

 Step 3: Copy Your API Key
- Under the “API” section, you'll see your personal API key.
- Click “Copy” to copy it to your clipboard.

**This key is tied to your account — keep it secret!**

    2. numverify api key:
 Steps to Obtain Your Numverify API Key
Step 1: Sign up on Numverify / APILayer
- Go to numverify.com.

- Click “Sign Up for Free” and create an account—free plan offers 100 monthly API requests 

Step 2: Choose Your Plan
After signing up, you’ll see subscription options.
The Free Plan (100 req/month) is available with no credit card required .
Paid plans (Starter, Basic, Pro) increase monthly usage limits.

Step 3: Get Your API Key
Log in, go to your Dashboard or API section.
You’ll find your unique API Access Key—a secret token used to authenticate API call


Edit the files in the config/ folder:
- api_keys.yaml: Put any required API keys.
- proxies.yaml: Add proxy settings if needed.


Sure! Here's a detailed and beginner-friendly `README.md` file for your project, written in **simple English** and tailored to your code structure:

---

```markdown
# 🔍 AllFinder

AllFinder is a powerful yet simple tool that helps you look up email addresses, phone numbers, and usernames across the internet. It uses open-source intelligence (OSINT) techniques and tools (like Sherlock) to gather public information.

## 📁 Project Structure

```

.
├── allfinder/              # Python modules for email, phone, and username lookups
├── config/                 # API keys and proxy configurations
├── data/sherlock/          # Sherlock integration for username search
├── static/                 # CSS styles
├── templates/              # HTML templates (Flask frontend)
├── tests/                  # Unit tests for the lookup modules
├── app.py                  # Main Flask app file
├── requirements.txt        # List of Python dependencies
├── setup.py                # Project setup file (optional)
├── README.md               # You're reading it!

````

---

## 🚀 Features

- 🔎 **Email Lookup**: Get details about an email address using OSINT sources.
- 📞 **Phone Number Lookup**: Retrieve public information related to a phone number.
- 👤 **Username Lookup**: Search for a username across multiple websites (via Sherlock).
- 🌐 **Web Interface**: Simple web page to input and search for emails, phones, and usernames.
- ✅ **Testing**: Built-in unit tests for reliability and future development.

---

## 🔧 Requirements

- Python 3.8 or above
- `pip` package manager

---

## 📦 Installation

1. **Clone the Repository**

```bash

git clone https://github.com/yourusername/allfinder.git
cd allfinder

````

2. **Create a Virtual Environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up API Keys & Proxies (if needed)**

Edit the files in the `config/` folder:

* `api_keys.yaml`: Put any required API keys.
* `proxies.yaml`: Add proxy settings if needed.

---

## 💻 Running the App

Use this command to start the web application:

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 🧪 Running Tests

To test each lookup module, use:

```bash

python -m unittest discover tests/

```
Or run individual test files like: (recomended)

```bash

python tests/test_email.py

```
---

## 🧠 How It Works

Each module in the `allfinder/` folder performs one type of lookup:

* `email_lookup.py`: Uses APIs and scraping for email intelligence.
* `phone_lookup.py`: Fetches details based on phone number.
* `username_lookup.py`: Integrates Sherlock to find social accounts by username.

These modules are used in `app.py`, which shows a form to the user via `index.html`, then displays the results.

---

## 📁 Using Sherlock

Sherlock must be cloned into the `data/sherlock/` directory. If you haven’t done that:

```bash
git clone https://github.com/sherlock-project/sherlock.git data/sherlock
```

---

## 🛡️ Security Warning

This tool is meant for educational and ethical OSINT purposes only. Always get permission before gathering personal data on someone else.

---

## 📃 License

MIT License. See `LICENSE` file for more info on ethical use.
Also check out the the Sherlock's `LICENSE` file for more info on ethical use.

---

## 🙋‍♂️ Contributing

Feel free to submit issues or pull requests if you want to improve or fix something!

---

## 📞 Contact

email: vijayck1610@gmail.com
```
