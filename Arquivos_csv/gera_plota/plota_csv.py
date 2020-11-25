import matplotlib.pyplot as plt
import csv

t = []
Xa = []
Xb = []
Xc = []

with open('dados.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
        t.append(float(row[0]))
        Xa.append(int(row[1]))
        Xb.append(int(row[2]))
        Xc.append(int(row[3]))

plt.plot(t,Xa, label='Xa')
plt.plot(t,Xb, label='Xb')
plt.plot(t,Xc, label='Xc')
plt.xlabel('Tempo [ms]', fontweight="bold")
plt.ylabel('Estado [Desligado/Ligado]', fontweight="bold")
plt.title('Tempo de fechamento\ndo disjuntor', fontweight="bold")
plt.legend()
plt.grid()
plt.show()