def zdruzi(tabela_tabel):
    """vrne tabelo z elementi tistih podtabel, ki vsebujejo vsaj tri elemente"""
    nova_tabela = []
    for tabela in tabela_tabel:
        dolzina = len(tabela)
        if dolzina >= 3:
            nova_tabela.extend(tabela)
    return nova_tabela

print(zdruzi([[1,2,3,4],[8,4],[3],[4,5,3,2],[3,4,8],[6,4]]))