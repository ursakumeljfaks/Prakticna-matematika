# 1. naloga
def ogrozena(povezave):
    slovar = {}
    for mesto1, mesto2 in povezave:
        slovar[mesto1] = povezave.count(mesto1)
        slovar[mesto2] = povezave.count(mesto2)
    return slovar

povezave = [("Piran", "Koper"),
            ("Koper", "Postojna"),
            ("Ilirska Bistrica", "Postojna"),
            ("Postojna", "Logatec"), ("Postojna", "Cerknica"),
            ("Gorica", "Ajdovščina"), ("Gorica", "Bled"), ("Gorica", "Jesenice"),
            ("Ajdovščina", "Postojna"),
            ("Idrija", "Logatec"), ("Idrija", "Žiri"),
            ("Logatec", "Žiri"), ("Logatec", "Vrhnika"), ("Logatec", "Cerknica"),
            ("Cerknica", "Ribnica"),
            ("Vrhnika", "Ljubljana"),
            ("Žiri", "Škofja Loka"),
            ("Ljubljana", "Škofja Loka"), ("Ljubljana", "Kamnik"),
            ("Ljubljana", "Celje"), ("Ljubljana", "Litija"),
            ("Ljubljana", "Grosuplje"), ("Ljubljana", "Kranj"),
            ("Ribnica", "Grosuplje"), ("Ribnica", "Kočevje"),
            ("Kočevje", "Novo mesto"),
            ("Grosuplje", "Novo mesto"),
            ("Litija", "Trbovlje"),
            ("Kranj", "Bled"), ("Kranj", "Škofja Loka"), ("Kranj", "Kamnik"),
            ("Kamnik", "Velenje"), ("Kamnik", "Celje"), ("Kamnik", "Škofja Loka"),
            ("Trbovlje", "Celje"), ("Trbovlje", "Krško"),
            ("Novo mesto", "Krško"),
            ("Krško", "Ptuj"),
            ("Celje", "Velenje"), ("Celje", "Slovenska Bistrica"),
            ("Maribor", "Slovenska Bistrica"), ("Maribor", "Ptuj"),
            ("Maribor", "Murska Sobota"), ("Maribor", "Ljutomer"),
            ("Velenje", "Slovenska Bistrica"),
            ("Slovenska Bistrica", "Ptuj"),
            ("Murska Sobota", "Gornja Radgona"), ("Murska Sobota", "Ljutomer"),
            ("Ptuj", "Ormož"),
            ("Ljutomer", "Ormož"),
            ("Bled", "Jesenice")]

print(ogrozena(povezave))

