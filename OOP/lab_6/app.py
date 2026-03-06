from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Мій перший сайт на Flask</h1>"

@app.route("/program")
def program():
    result = ""

    for i in range(1, 6):
        result += f"Число: {i}<br>"

    return f"<h2>Результат програми</h2>{result}"

if __name__ == "__main__":
    app.run(debug=True)