import requests
import matplotlib.pyplot as plt

data = requests.get("https://bit.ly/34TwYv8").json()

cene = []
produkti = []
rez = []
st = 0
for slovar in data:
    cene.append(int(slovar["price"]))
    produkti.append(len(slovar["title"]))
    st += len(slovar["price"])
    rez.append(st)

fig = plt.figure(figsize = [10, 6])

plt.bar(sorted(cene), rez, color = "b", label = 'CDF')
plt.bar(cene, produkti, color = "g", label = 'PDF')
plt.legend(loc = 'upper left')
plt.xlabel('Cene')
plt.ylabel('Products')
plt.show()
