#VERIFICADOR MAIUSCULO MINUSCULO
'''Verifica se mesmo digitando letras maiusculas ou minusculas se uma palavra
e igual ou diferente.
'''

def Mai_Min(entrada,compare):
    Lord1 = []
    Lord2 = []
    cont = 0
    cont2 = 0
    death = 0
    ccp = 0
    ch4 = 0
    for ch in entrada:
        ch = ord(ch)
        Lord1.append(ch)
        cont += 1
    for ch2 in compare:
        ch2 = ord(ch2)
        Lord2.append(ch2)
        cont2 += 1
    if (cont == cont2):
        for ch3 in range(cont):
            ch3 = Lord1[ccp]
            ch4 = Lord2[ccp]
            if ((ch4 != ch3) and (ch4 != (ch3 - 32)) and (ch4 != (ch3 + 32))):
                death += 1
            ccp += 1
        if (death == 0):
            return(True)
        else:
            return(False)
    else:
        return(False)

w1 = str(input("Palavra1:"))
w2 = str(input("Palavra2:"))
print(Mai_Min(w1,w2))

        
        
    
    
