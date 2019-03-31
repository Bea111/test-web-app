from flask import Flask, render_template
import opinion
import requests

app= Flask ("app")


@app.route("/")
def hello():
    mindful_tweets=opinion.tweet_main()
    return render_template("index.html",tweets=mindful_tweets)




@app.route("/form", methods=["POST"])
def form():
    form_data=request.form
    fname= form_data["firstname"]
    lname= form_data["lastname"]
    return f"Thanks for submitting a form {fname}"

if __name__ =="__main__":
    app.run(debug=True)



# })
