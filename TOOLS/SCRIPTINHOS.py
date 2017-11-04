'''
USR = open("usuarios.txt","r")
USRSTR = USR.read()
bunga = XRISTE(USRSTR)

print (bunga)
'''
'''
WOW = ELEISSON(bunga)

USA = open("usuarios.txt","w")
USA.write(WOW)
USA.close()

print (WOW)
'''
'''
DICTESTE = {"1":("FOTO XAROPINHO","FOTO TESTE LTDA ME.","8134000000","Bruno","Rua da Hora, 250, Espinheiro","RECIFE","PE","51021-000","LP1500","2917613","N")}

CHEESE = ELEISSON(DICTESTE)
print(CHEESE)
USA = open("TESTECRU.txt","w")
USA.write(CHEESE)
USA.close()
'''
'''
ELE = open("elementos.txt","r")
ELESTR = ELE.read()
bungabunga = CHRISTUS(ELESTR)

print (bungabunga)
'''
'''
pr = loGOco("Bruno",8)
print (pr)
'''
'''
#MAIOR NUMERO DO DICIONARIO
def Maior_Numero(DIC):
    L_Keys = []
    for nm in DIC.keys():
        L_Keys.append(int(nm))
    ct = -1
    for xz in L_Keys:
        ct += 1
    n1 = 0
    n2 = 0
    nM = 0
    cl = 0
    if (ct == 0):
        nM = L_Keys[0]
    else:
        for oo in range(ct):
            n1 = (L_Keys[cl])
            if (nM > n1):
                n1 = nM
            n2 = (L_Keys[cl + 1])
            if (n1 <= n2):
                nM = n2
            if (n1 >= n2):
                nM = n1
            cl += 1
    return(nM)

Lista = {"2":"Jabiromba","5":(1,2),"1":"x"} 

maximo = Maior_Numero(Lista)
print (maximo)
'''
def Dados_Cliente_Imp(nc,nof,raz,tel,con,end,cid,est,cep,equ,nus,cot):
    Line1 = "\n" + "Codigo de Cliente: " + nc + "\n"
    Line2 = "Nome Fantasia: " + nof + "\n"
    Line3 = "Razao Social: " + raz + "\n"
    Line4 = "Telefone: " + tel + "\n"
    Line5 = "Pessoa de Contato: " + con + "\n"
    Line6 = "Endereco: " + end + "\n"
    Line7 = "Cidade: " + cid + "   Estado: " + est + "   CEP.: " + cep + "\n"
    Line8 = "Equipamento / Modelo: " + equ + "  Numero de Serie: " + nus + "\n"
    Line9 = "Contrato: " + cot + "\n"
    return (Line1 + Line2 + Line3 + Line4 + Line5 + Line6 + Line7 + Line8 + Line9)

CODCLI = "4"
NOMEFAN = "Foto Xaropinho"
RAZAO = "Xarope Com. e Serv LTDA."
TEL = "(041) 3333-5665"
CON = "Pedro"
END = "Rua da Macieira, 45, Pinheiros"
CID = "Sao Paulo"
EST = "SP"
CEP = "02345-000"
EQUIP = "Fujifilm LP1500"
NS = "2915776"
COT = "N"

XOM = Dados_Cliente_Imp(CODCLI,NOMEFAN,RAZAO,TEL,CON,END,CID,EST,CEP,EQUIP,NS,COT)
print (XOM)



