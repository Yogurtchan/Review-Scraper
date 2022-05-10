from flask import Flask, redirect, url_for

app = Flask(__name__)

# Function for index.html
@app.route("/index.html")
def reviews():
    return redirect(url_for("index"))
# Function for reviews.html
@app.route("/reviews.html")
def reviews():
    return "Enter number of tools to scrape: {tools}"


if __name__ == "__main__":
    app.run()