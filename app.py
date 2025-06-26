from flask import Flask, render_template, request, jsonify
from allfinder.username_lookup import search_username
from allfinder.phone_lookup import phone_lookup
from allfinder.email_lookup import email_lookup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/email-lookup')
def lookup():
    email = request.args.get("email")
    if not email:
        return jsonify({"error": "Email is required"}), 400

    result = email_lookup(email)
    return jsonify(result)

@app.route('/api/phone-lookup')
def phone_lookup_api():
    phone = request.args.get("phone")
    if not phone:
        return jsonify({"error": "Phone number is required"}), 400
    result = phone_lookup(phone)
    return jsonify(result)

@app.route('/api/username-lookup')
def username_lookup_api():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    result = search_username(username)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
