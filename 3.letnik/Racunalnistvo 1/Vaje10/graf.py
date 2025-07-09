import matplotlib.pyplot as plt

x = [0, 48, 59, 75, 91, 99, 107, 115, 131, 147, 174, 192, 220]
y = [0, 7, 13, 17, 20, 22, 24, 26, 29, 33, 35, 39, 60]

plt.figure(figsize=(10, 6))
for i in range(len(x) - 1):
    plt.hlines(y[i], x[i], x[i+1], color='b')

plt.xticks(x[:-1])
plt.yticks(y[:-1])
plt.xlabel('prostor')
plt.ylabel('vrednost')
plt.title('Graf odvisnosti razpoložljivega prostora od optimalne vrednosti nahrbtnika')
plt.savefig('graf.png')
plt.show()
