from flask import Flask, render_template, redirect, request, abort, url_for
import os

import numpy as np # библиотека для удобной работы с массивами
import pandas as pd # библиотека для удобной работы с датасетами
import matplotlib.pyplot as plt # библиотека для графики
import seaborn as sns # библиотека для отображения диаграмм
import seaborn as sns
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.utils import shuffle


app = Flask(__name__)
#app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=1)
#app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def define(data):  # получить предсказание с помощью ранее обученной модели
    pred = linear_model.predict(data)
    return pred


def main():
    global list_of_products, list_of_products_with_varfarin

    port = int(os.environ.get("PORT", 5000))
    print(1)
    app.run(host='0.0.0.0', port=port)


@app.route("/")
def index():   # главная страница
    names = []
    i = 0
    for data in dataframe.profession_name.values:
        names.append((data, dataframe.area.values[i]))
        i += 1

    return render_template("Main.html", result='', names=names)

@app.route('/<int:num>')
def main_num(num):
    result = str(define([[num]]))

    names = []
    i = 0
    for data in dataframe.profession_name.values:
        names.append((data, dataframe.area.values[i]))
        i += 1

    return render_template("Main.html", result=result, names=names)


if __name__ == '__main__':
    dataframe = pd.read_csv(
        'dataset.csv',
        sep=',',  # что является разделителем колонок в файле,
        decimal='.'
        # что является разделителем десятичных дробей в записи чисел
    )

    # посмотрим на случайные 15 записей


    random_indices = shuffle(range(len(dataframe)), random_state=1)
    train_indices = random_indices

    sliced = slice(len(train_indices) // 4, len(train_indices))
    plt.scatter(dataframe['perspective'][sliced], dataframe['area'][sliced]);  # посмотреть как распределены данные

    linear_model = LinearRegression().fit(
        dataframe.area.values[train_indices][sliced].reshape(-1, 1),
        dataframe.perspective[train_indices][sliced].values)

    main()   # старт
