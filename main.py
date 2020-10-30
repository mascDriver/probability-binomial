from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

def process_binomial(n ,p, x):
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='Probabilidade individual')
    ax.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
    rv = binom(n, p)
    print(f"A probabilidade individual é de {rv.pmf(x)*100}%")
    ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
              label='Casos de sucessos encontrados')
    ax.legend(loc='best', frameon=False)
    plt.show()


def process_binomial_regular(n ,p, x, rv):
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='Probabilidade individual')
    ax.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
    ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
              label='Casos de sucessos encontrados')
    ax.legend(loc='best', frameon=False)
    plt.show()


if __name__ == '__main__':
    while True:
        entrada = input("Digite 1 para calcular binomial individual e 2 para acumulativa ")
        n = input("Insira o valor de observacoes: ")
        x = input("Insira o valor de sucessos: ")
        p = input("Insira o valor de probabilidade de sucesso: ")
        sum = 0
        if int(entrada) == 2:
            rv = binom(n, p)
            for i in range(0, int(x)):
                sum += rv.pmf(i)
            print(f"A probabilidade individual é de {sum * 100}%")
            process_binomial_regular(int(n), float(p), int(x), rv)
        else:
            process_binomial(int(n), float(p), int(x))
