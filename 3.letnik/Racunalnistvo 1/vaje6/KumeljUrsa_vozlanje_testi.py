from vstavi import Vozel, VerizniSeznam, vstavi_veriga_vozlov, vstavi_verizni_seznam


# vstavi 3 v 1->2->4->5
v1 = Vozel(1, Vozel(2, Vozel(4, Vozel(5))))
v2 = vstavi_veriga_vozlov(v1, 3)
trenutni = v2
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
# dobiti bi morali 1->2->3->4->5

# vstavi 5 v 1->2->4->5
v1 = Vozel(1, Vozel(2, Vozel(4, Vozel(5))))
v2 = vstavi_veriga_vozlov(v1, 5)
trenutni = v2
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
# dobiti bi morali 1->2->4->5->5

# vstavi 1 v 1->2->4->5
v1 = Vozel(1, Vozel(2, Vozel(4, Vozel(5))))
v2 = vstavi_veriga_vozlov(v1, 1)
trenutni = v2
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
# dobiti bi morali 1->1->2->4->5
print("\n")


###############################################################


# vstavi 10 v 1->2->4->5
s1 = VerizniSeznam()
vstavi_verizni_seznam(s1, 1)
vstavi_verizni_seznam(s1, 2)
vstavi_verizni_seznam(s1, 4)
vstavi_verizni_seznam(s1, 5)
print(vstavi_verizni_seznam(s1,10))# 1->2->4->5->10

# vstavi 2 v prazen
s2 = VerizniSeznam()
print(vstavi_verizni_seznam(s2,2)) # 2->

# vstavi 1 v 1->2->4->5
s3 = VerizniSeznam()
vstavi_verizni_seznam(s3, 1)
vstavi_verizni_seznam(s3, 2)
vstavi_verizni_seznam(s3, 4)
vstavi_verizni_seznam(s3, 5)
print(vstavi_verizni_seznam(s3,1)) # 1->1->2->4->5

# vstavi 3 v 1->2->4->5
s4 = VerizniSeznam()
vstavi_verizni_seznam(s4, 1)
vstavi_verizni_seznam(s4, 2)
vstavi_verizni_seznam(s4, 4)
vstavi_verizni_seznam(s4, 5)
print(vstavi_verizni_seznam(s4,3)) # 1->2->3->4->5







