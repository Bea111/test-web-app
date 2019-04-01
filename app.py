from flask import Flask, render_template, request
import opinion

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
    return f"Thank you for sharing your mindfulness techniques {fname}. We will review your document and add it to our page. Please keep updated on our live tweet feed. And {fname}... remember to stop and breathe once in a while..."

if __name__ =="__main__":
    app.run(debug=True)




@app.route("/contact")
def contact():
    return render_template("contact.html")


'''
@app.route("/<path:path>")
def static_file(path):
    return app.send_static_file(path)
'''

# })
