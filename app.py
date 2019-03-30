from flask import Flask, render_template, request
import opinion

app= Flask ("app")


@app.route("/")
def hello():
    mindful_tweets=opinion.tweet_main()
    return render_template("index.html",tweets=mindful_tweets)

@app.route("/<string:name>")
def hello_someone(name):
    return render_template("index.html",name=name.title())

@app.route("/signup", methods=["POST"])
def signup():
    form_data=request.form
    email=form_data["email"]
    return f"Thanks for signing up with email address {email}"

@app.route("/form", methods=["POST"])
def signup_form():
    data=request.form
    fname= data["firstname"]
    lname= data["lastname"]
    return f"Thanks for submitting a form {fname}"

if __name__ =="__main__":
    app.run(debug=True)



# })


'''
You can use HTML forms to get all sorts of information from visitors to your website,
including text, email, numbers, dates, and more.
You’re not limited to just using text felds either
– you can use input types like radio buttons, tick boxes, etc.

Add another one or two input felds of your choice to your HTML form,
and update your Python code to do something with that information
(for example, display it back to your user).
 If you want to get a bit creative with input felds,
 have a look at the W3 Schools HTML form tutorial,
 and W3 Schools input type tutorial for inspiration.

'''
