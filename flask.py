from flask import Flask, render_template, url_for

app = Flask(__name__)

# Function for index.html
@app.route("/")
def reviews():
    return render_template(url_for("index.html"))
# Function for reviews.html
@app.route("/", methods=["POST"])
def reviews():
    text = request.form["text"]
    processedText = text.upper()
    return processedText, render_template(url_for("reviews.html"))


if __name__ == "__main__":
    app.run()

# TO-DO: get flask to open index html on default; catch user input for number of tools to review and display csvData