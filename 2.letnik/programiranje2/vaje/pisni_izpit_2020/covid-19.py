import requests
import datetime
import matplotlib.pyplot as plt

data = requests.get("https://api.sledilnik.org/api/hospitals").json()

X = [] 
proste_postelje = []
prosti_ventilatorji = []
for slovar in data:
    if 3 <= slovar["month"] <= 5 and slovar["year"] == 2020 and slovar["day"] <= 31:
        X.append(datetime.datetime(2020, slovar["month"], slovar["day"]))
        proste_postelje.append(slovar["overall"]["beds"]["free"])
        prosti_ventilatorji.append(slovar["overall"]["vents"]["free"])

fig = plt.figure(figsize = [7, 5])

plt.semilogy(X, proste_postelje, "-b", label = "Postelje")
plt.fill_between(X, proste_postelje, "b")
plt.semilogy(X, prosti_ventilatorji, "-r", label = "Ventilatorji")
plt.fill_between(X, prosti_ventilatorji, "red")
plt.ylim([1, 1500])
plt.xlim([datetime.datetime(2020,3,10), datetime.datetime(2020,5,31)])
plt.xticks([datetime.datetime(2020,3,10), datetime.datetime(2020,3,26),datetime.datetime(2020,4,11),datetime.datetime(2020,4,28), datetime.datetime(2020,5,14), datetime.datetime(2020,5,31)])
plt.xlabel("Datum")
plt.ylabel("Število postelj")
plt.legend(loc = 'upper right', frameon = False)

plt.show()