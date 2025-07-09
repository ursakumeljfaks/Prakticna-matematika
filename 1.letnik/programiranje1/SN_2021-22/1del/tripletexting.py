babicino_besedilo = input()
dolzina_babicinega_besedila = int(len(babicino_besedilo))
dolzina_ene_babicine_besede = dolzina_babicinega_besedila // 3 #babica vsako besedo napise 3x, vmes pa se lahko zmoti za kakšno črko

babicina_prva_beseda = babicino_besedilo[0 : dolzina_ene_babicine_besede]
babicina_druga_beseda = babicino_besedilo[dolzina_ene_babicine_besede : 2*dolzina_ene_babicine_besede]
babicina_tretja_beseda = babicino_besedilo[2*dolzina_ene_babicine_besede : dolzina_babicinega_besedila]

#pregledati moramo 3 možnosti in sicer, če
# 1. babicina_prva_beseda == babicina_druga_beseda
# 2. babicina_prva_beseda == babicina_tretja_beseda
# 3. babicina_druga_beseda == babicina_tretja_beseda
# ker posatvimo rezultat oz. besedilo na začetno vrednost kar babicina_prva_beseda, moramo potem 
# preveriti le še tretjo točko, saj pri prvih dveh bo rezultat kar prva_babicina_beseda

besedilo = babicina_prva_beseda #besedilo bo naš rezultat, ki je na začetku enak prvi besedi in se potem lahko spremeni
if babicina_druga_beseda == babicina_tretja_beseda:
    besedilo = babicina_druga_beseda

print(besedilo)