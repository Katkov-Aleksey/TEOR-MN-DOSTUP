# Смоделировать работу Марковской цепи с двумя состояниями за t шагов. Оценить
# вероятность того, что она окажется в i-ом состоянии на шаге t. Также произвести
# теоретический расчет данной вероятности.
import random
import matplotlib.pyplot as plt
import numpy as np


def theor(state):
    list_pr = []
    if state == 0:
        list_pr.append(1)
    elif state == 1:
        list_pr.append(0)

    matrix = np.array([[0.8, 0.2], [0.6, 0.4]])
    p0 = np.array([1, 0])

    for step in range(1, 100):
        p0 = p0.dot(matrix)
        list_pr.append(p0[state])
    return list_pr


def prob(n, t, state):
    # если мы в 0, то TRUE
    flag = state
    count = 0
    p00 = 0.8
    p11 = 0.4

    if not state and t == 0:
        return 0
    for j in range(0, n):
        for step in range(0, t):
            c = random.random()
            if flag:
                if c > p00:
                    flag = False
            else:
                if c > p11:
                    flag = True
        if state == flag:
            count += 1
    return count / n


listPrState0 = []
listPrState1 = []
listT = []

for t in range(0, 100):
    listT.append(t)
    listPrState0.append(prob(50000, t, True))
    listPrState1.append(prob(50000, t, False))

list_pr1 = theor(1)
list_pr0 = theor(0)

plt.figure()
plt.plot(listT, listPrState0, color='red', label='State(0)')
#plt.plot(listT, listPrState1, color='green', label='State(1)')
plt.plot(listT, list_pr0, color='blue', label='Theor(0)')
#plt.plot(listT, list_pr1, color='black', label='Theor(1)')
plt.legend()
plt.xlabel('T(time)')
plt.ylabel('Pr(prob)')
plt.savefig('res1.png')
plt.show()
