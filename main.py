from flask import Flask, render_template, url_for, request
from csvReader import csvRead
import csvData

app = Flask(__name__)

# Function for index.html
@app.route("/index")
def index():
    return render_template("index.html")
# Function for reviews.html
@app.route("/reviews", methods=["POST", "GET"])
def reviews():
    if request.method == "POST":
        pass
    # text = request.form["text"]
    # processedText = text.upper()
    reader = csvRead("reviewScraper.csv")
    site = csvData.getSites(reader)
    rev = csvData.getReviews(reader, 20)
    return render_template("reviews.html", site=site, rev=rev)


if __name__ == "__main__":
    app.run()

# TO-DO: get flask to open index html on default; catch user input for number of tools to review and display csvData
# TO-DO: pass csv file through reviews route