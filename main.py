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
    data = {}
    data['top_1_1'] = 'Management Analysts (100000)'
    data['top_1_2'] = '1Management Analysts (100000)'
    data['top_1_3'] = 'M1anagement Analysts (100000)'
    data['top_1_4'] = 'Ma1nagement Analysts (100000)'
    data['top_1_5'] = 'Management Analysts (100000)'
    data['top_1_6'] = 'Ma1nagement Analysts (100000)'
    data['top_1_7'] = 'Ma11nagement Analysts (100000)'
    data['top_1_8'] = 'Ma1nagement Analysts (100000)'
    data['top_1_9'] = 'Management Analysts (100000)'
    data['top_1_10'] = 'M1anagement Analysts (100000)'

    data['top_2_1'] = 'Manag2ement Analysts (100000)'
    data['top_2_2'] = 'Management Analysts (100000)'
    data['top_2_3'] = 'Mana2gement Analysts (100000)'
    data['top_2_4'] = 'Management Analysts (100000)'
    data['top_2_5'] = 'Man2agement Analysts (100000)'
    data['top_2_6'] = 'Management Analysts (100000)'
    data['top_2_7'] = 'Mana22gement Analysts (100000)'
    data['top_2_8'] = 'Mana2gement Analysts (100000)'
    data['top_2_9'] = 'Man2agement Analysts (100000)'
    data['top_2_10'] = 'Ma2nagement Analysts (100000)'

    return render_template("Main.html", **data)


if __name__ == '__main__':
    main()   # старт
