from os import environ

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    background_color = environ.get("BACKGROUND_COLOR", "lightblue")
    welcome_text = environ.get("WELCOME_TEXT", "Welcome to the Flask Demo!")

    # 從 Secret 中取得敏感資訊（模擬 API Token）
    api_token = environ.get("API_TOKEN", "No token")

    return render_template('index.html',
                           background_color=background_color,
                           welcome_text=welcome_text,
                           api_token=api_token)


@app.route("/env")
def show_env():
    return "<br>".join([f"{key}={value}" for key, value in environ.items()])


if __name__ == '__main__':
    app.run(debug=True)
