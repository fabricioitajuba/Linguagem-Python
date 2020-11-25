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
plt.xlabel('Tempo')
plt.ylabel('Estado')
plt.title('Tempo de fechamento\ndo disjuntor')
plt.legend()
plt.show()