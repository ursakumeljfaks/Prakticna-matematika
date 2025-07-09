# valovi epidemije
def valovi(po_dnevih):
    skupaj = 0
    val = []
    koncni_val = []
    for okuzba in po_dnevih:
        if okuzba != 0:
            skupaj += okuzba
        else:
            val.append(skupaj)
            skupaj = 0
    for stevilo in val:
        if stevilo != 0:
            koncni_val.append(stevilo)
    return koncni_val

print(valovi([1, 5, 6, 0, 0, 0, 2, 3, 0, 5, 8, 0]))

# sledilnk
def sledilnik(dnevi):
    zaprti = 0
    tabela_zaprtih = []
    for i in range(len(dnevi)-1):
        zaprt1 = dnevi[i][0]
        odprt1 = dnevi[i][1]
        zaprt2 = dnevi[i+1][0]
        for posebi in zaprt1:
            zaprti += 1
            for posebi2 in odprt1:
                for posebi3 in zaprt2:
                    if posebi3 == posebi2:
                        zaprti += 1
                    zaprti += 1
    return zaprti
                    
dnevi = [
            (["gledališča", "smučišča"], []),
            (["šole", "frizer", "muzeji"], ["smučišča"]),
            (["knjižnice"], ["muzeji", "smučišča"]),
            (["smučišča", "knjižnice", "gledališča"], ["šole"]),
            (["šole"], ["frizer", "smučišča"]),
            (["smučišča"], []),
            ([], []),
            ([], ["smučišča"])
        ]

print(sledilnik(dnevi))
# sirjenje okuzbe
def okuzeni(oseba, cas, druzenja):
    mnozica_oseb = set()
    for morebitno_okuzen in druzenja:
        if morebitno_okuzen == oseba:
            for osebe in druzenja[oseba]:
                if osebe[1] > cas:
                    mnozica_oseb.add(osebe[0])
    # for okuzen_par in druzenja.values():
    #     if okuzen_par[1] > cas:
    #         if okuzen_par[0] == oseba:
    #             for se_en in druzenja.values():
    #                 mnozica_oseb.add(se_en[0])
    return mnozica_oseb

druzenja = {
            "Ana": [("Berta", 7), ("Cilka", 10), ("Dani", 4), ("Fanči", 3)],
            "Berta": [("Ana", 7), ("Cilka", 3)],
            "Cilka": [("Ana", 10), ("Berta", 3), ("Dani", 5)],
            "Dani": [("Ana", 4), ("Cilka", 5), ("Ema", 1), ("Fanči", 2)],
            "Ema": [("Dani", 1), ("Fanči", 8), ("Greta", 3)],
            "Fanči": [("Ana", 3), ("Dani", 2), ("Ema", 8), ("Greta", 2)],
            "Greta": [("Ema", 3), ("Fanči", 2)]
        }

print(okuzeni("Ana", 3, druzenja))

# V vhodnih podatkih imamo več vnosov celih števil. Prvi nam pove število nadaljnih vnosov. Za branje podatkov sem
# se odločila z zanko for. Naša naloga je najti število vseh nizov, ki ne vsebujejo podniza "11". Ker 
