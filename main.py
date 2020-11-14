from flask import Flask, render_template, redirect, request, abort, url_for
import os


app = Flask(__name__)
#app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=1)
#app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global list_of_products, list_of_products_with_varfarin

    port = int(os.environ.get("PORT", 5000))
    print(1)
    app.run(host='127.0.0.1', port=port)


@app.route("/")
def index():   # главная страница
    return render_template("Main.html")


if __name__ == '__main__':
    main()   # старт
