from flask import Flask, render_template, url_for, request
from csvReader import csvRead
import csvData
from webscraper import runWebscraper

app = Flask(__name__)

# Function for index.html
@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")
# Function for reviews.html
@app.route("/reviews", methods=["POST", "GET"])
def reviews():
    if request.method == "POST":
        # If Get Reviews button is clicked
        if request.form["Get Reviews"]:
            # If user input is not empty
            if request.form["userInput"] != "":
                userInput = int(request.form["userInput"])
                runWebscraper(userInput)
                reader = csvRead("reviewScraper.csv")
                site = csvData.getSites(reader)
                rev = csvData.getReviews(reader, userInput)
                return render_template("reviews.html", site=site, rev=rev)


if __name__ == "__main__":
    app.run()
