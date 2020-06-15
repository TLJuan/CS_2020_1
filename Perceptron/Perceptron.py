import numpy as np
import pandas as pd
import pygame


class Perceptron:
    # n: Tasa de aprendizaje.
    # wn: Pesos actualizados después del ajuste
    # errors_: Cantidad de errores de clasificación en cada pasada

    def __init__(self, n=0.5):
        self.errors_ = []
        self.n = n

    def fit(self, X, y):
        test = X.shape[1]
        self.wn = np.zeros(test)
        errors = 1

        while errors != 0:
            errors = 0
            for xi, target in zip(X, y):
                update = self.n * (target - self.predict(xi))
                self.wn += np.dot(update, xi)
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def predict(self, X):
        """f(u) = 1 si u > 0; 0 en otro caso"""
        phi = np.where(self.summation(X) > 0.0, 1, 0)
        return phi

    def summation(self, X):
        """sumatoria de pesos x entrdas"""
        z = np.dot(X, self.wn)
        return z


def main():
    ppn0 = Perceptron(n=0.5)
    ppn1 = Perceptron(n=0.5)
    ppn2 = Perceptron(n=0.5)
    ppn3 = Perceptron(n=0.5)
    ppn4 = Perceptron(n=0.5)
    ppn5 = Perceptron(n=0.5)
    ppn6 = Perceptron(n=0.5)
    ppn7 = Perceptron(n=0.5)
    ppn8 = Perceptron(n=0.5)
    ppn9 = Perceptron(n=0.5)

    df = pd.read_csv("numbers.data", header=None)
    X = df.iloc[0:8, 0:40].values
    y = df.iloc[0:8, 40].values
    y0 = np.where(y == 'cero', 1, 0)
    y1 = np.where(y == 'uno', 1, 0)

    ppn0.fit(X, y0)
    ppn1.fit(X, y1)

    t = [0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0]  # 0
    if ppn0.predict(t) == 1:
        print("No es el numero")
    print(ppn0.predict(t))
    print(ppn1.predict(t))


if __name__ == '__main__':
    main()
