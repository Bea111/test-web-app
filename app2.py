from flask import Flask, render_template

app=Flask ("app2")

@app.route("/advice")
def advice():
    some_advice=randomadvice.get_advice()
    return render_template ("advice.html",advice=some_advice)
