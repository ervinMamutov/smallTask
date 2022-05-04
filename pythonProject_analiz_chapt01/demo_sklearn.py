# coding: utf8
# Chap01/demo_sklearn.py
from sklearn import datasets
from sklearn.cluster import KMeans

# Графические настройки
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Ubuntu Condensed']
rcParams['figure.figsize'] = (5, 4)
rcParams['legend.fontsize'] = 10
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9


def saveplot(dest):
    plt.tight_layout()
    plt.savefig(dest, dpi=600)


if __name__ == '__main__':
    # Загрузить данные
    iris = datasets.load_iris()
    X = iris.data
    petal_length = X[:, 2]
    petal_width = X[:, 3]
    true_labels = iris.target

    # Применить алгоритм кластеризации K-средних
    estimator = KMeans(n_clusters=3)
    estimator.fit(X)
    predicted_labels = estimator.labels_

    # Задать цветовую схему: красный, желтый и синий
    color_scheme = ['r', 'y', 'b']

    # Задать маркеры: круг, "x" и "плюс"
    marker_list = ['x', 'o', '+']

    # Назначить цвета/маркеры предсказанным меткам
    colors_predicted_labels = [color_scheme[lab] for lab in predicted_labels]
    markers_predicted = [marker_list[lab] for lab in predicted_labels]

    # Назначить цвета/маркеры истинным меткам
    colors_true_labels = [color_scheme[lab] for lab in true_labels]
    markers_true = [marker_list[lab] for lab in true_labels]

    # Построить и сохранить 2 точечных графика
    for x, y, c, m in zip(petal_width,
                          petal_length,
                          colors_predicted_labels,
                          markers_predicted):
        plt.scatter(x, y, c=c, marker=m)
    saveplot('iris_clusters.png')
    for x, y, c, m in zip(petal_width,
                          petal_length,
                          colors_true_labels,
                          markers_true):
        plt.scatter(x, y, c=c, marker=m)
    saveplot('iris_true_labels.png')

    print(iris.target_names)