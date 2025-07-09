def vsebovani(s, t):
    """ugotovi, ce so vsi znaki niza s vsebovani v t"""
    st_znakov = len(s)
    znaki = 0
    for znak in s:
        if znak in t:
            znaki += 1
    if znaki == st_znakov:
        return True
    
def resitev(s, t):
    return set(s) <= set(t)

def resitev2(s, t):
    for znak in s:
        if znak not in t:
            return False
    return True

b1 = "osa"
b2 = "postaja"
print(f"Za {b1} v {b2} je odgovor {resitev(b1, b2)}")