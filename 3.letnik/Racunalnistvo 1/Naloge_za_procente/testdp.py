def najkrajsa_pot(matrika):
    '''vrne najkrajso pot skozi matriko iz levega zgornjega kota do desnega spodnjega kota,
       veljavne poti so desno, dol in desno-dol (diagonala).
    '''
    n = len(matrika) - 1
    m = len(matrika[0]) - 1
    cache = dict()
    
    def pomozna(i,j):
        # če pademo ven iz naše matrike
        if (i,j) not in cache:
            if i == n and j == m:
                return matrika[n][m]
            if i > n or j > m:
                return float("inf")
            cache[(i,j)] = min(pomozna(i+1,j), pomozna(i,j+1), pomozna(i+1,j+1)) + matrika[i][j]
        return cache[(i,j)]
    
    return pomozna(0,0)
    
    

matrika = [[1,2,1,2,2],
           [3,6,0,2,7,0],
           [0,1,3,4,8,3],
           [2,5,7,0,1,4]]
matrika2 = [[1,0,2],
            [3,4,5]]
print(najkrajsa_pot(matrika))



