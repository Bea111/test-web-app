from flask import Flask, render_template
import opinion
import requests

app= Flask ("app")

@app.route("/signup", methods=["POST"])
def signup():
    form_data=request.form
    email=form_data["email"]
    return render_template ("contact.html")
    return f"Thanks for signing up with email address {email}"

@app.route("/form", methods=["POST"])
def signup_form():
    data=request.form
    fname= data["firstname"]
    lname= data["lastname"]
    return render_template ("contact.html")
    return f"Thanks for submitting a form {fname}"
