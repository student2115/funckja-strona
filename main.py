from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template('landing.html', name="landing")

@app.route("/about_us")
def about_us():
    return render_template('about_us.html', name="about_us")
