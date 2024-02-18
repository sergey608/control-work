from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h3>Это заглавная страница сайта</h3>"

@app.route("/info")
def info():
    return "<h3>Страница с информацией находится в разработке</h3>"

if __name__ == "__main__":
    app.run()