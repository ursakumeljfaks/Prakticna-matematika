import os

with open('//Users/spela/Desktop/pisni_izpit_2020/mathematics.tab', 'r') as dat:
    slovar = {}
    leta = []
    vse_tocke = 0
    prva = dat.readline()
    for vrstica in dat:
        vrstica1 = vrstica.strip().split("\t")
        ime = vrstica1[0]
        priimek = vrstica1[1]
        id = vrstica1[2]
        leto = int(vrstica1[13])
        tocke = vrstica1[22]
        # print(leto)
        if tocke != 'NA':
            tocke = float(vrstica1[22])
            if id in slovar: 
                slovar[id]["st. clankov"] += 1
                slovar[id]["tocke"] += tocke
                slovar[id]["zadnje leto"] = max(leto, slovar[id]["zadnje leto"])
            else: 
                slovar[id] = {"ime": ime, "priimek": priimek, "st. clankov": 1, "tocke": tocke, "prvo leto": leto, "zadnje leto": leto }
       
with open('scores.tab', 'w') as file:
    for avtor, sl in slovar.items():
        if sl["tocke"] != 'NA':
            povprecje_clankov = sl["st. clankov"] // (sl["zadnje leto"] - sl["prvo leto"] + 1)
            povprecje_tock = sl["tocke"] / ((sl["zadnje leto"]) - (sl["prvo leto"]) + 1)
            file.write(f"{sl['ime']} {sl['priimek']} {povprecje_clankov} {povprecje_tock}")
            file.write('\n')



    


             
