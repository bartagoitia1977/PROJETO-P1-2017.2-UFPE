'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor:	Bruno Artagoitia Vicente do Nascimento (bavn)
Email:	bavn@cin.ufpe.br
Data:	2017-10-22

Copyright(c) 2017 Bruno Artagoitia Vicente do Nascimento
'''

#NUCLEO DO PROJETO P1
#PYTHON LAB - ASSISTENCIA TECNICA

#DESCRIPTOGRAFIA USUARIO
def XRISTE(FILE):
    u = ""
    p = ""
    l = ""
    numinho = 0
    JOHN = ""
    supla = ""
    lisupla = []
    JR = ""
    cploc = 0
    for q in FILE:
        q = str(q)
        if (q != " "):
            JR += q
        if (q == " "):
            numinho = ((int(JR)) - 37)
            JR = ""
            if (numinho != 254):
                JOHN = (chr(numinho))
                if (cploc == 0):
                    u += JOHN
                if (cploc == 1):
                    p += JOHN
                if (cploc == 2):
                    l += JOHN
            if (numinho == 254):
                cploc += 1
                numinho = 0
        if (cploc == 3):
            supla = (u,p,l)
            lisupla.append(supla)
            u = ""
            p = ""
            l = ""
            cploc = 0
    DICU = {}
    for j in lisupla:
        papito = (j[1], j[2])
        DICU[j[0]] = papito
    return (DICU)

#CRIPTOGRAFA USUARIO E ELEMENTOS
def ELEISSON(DIC3):
    JN = []
    jupla = ""
    for us in DIC3.keys():
        JN.append(us)
        jupla = DIC3[us]
        for xiz in jupla:
            JN.append(xiz)
    STRONG = ""
    SS = 0
    for wd in JN:
        for lt in wd:
            SS = ((ord(lt)) + 37)
            STRONG += str(SS)
            STRONG += " "
        STRONG += "291"
        STRONG += " "

    return (STRONG)

#DESCRIPTOGRAFIA ELEMENTOS
def CHRISTUS(FILE):
    nc = ""
    nof = ""
    raz = ""
    tel = ""
    con = ""
    end = ""
    cid = ""
    est = ""
    cep = ""
    equ = ""
    nus = ""
    cot = ""
    numinho = 0
    JOHN = ""
    supla = ""
    lisupla = []
    JR = ""
    cploc = 0
    for q in FILE:
        q = str(q)
        if (q != " "):
            JR += q
        if (q == " "):
            numinho = ((int(JR)) - 37)
            JR = ""
            if (numinho != 254):
                JOHN = (chr(numinho))
                if (cploc == 0):
                    nc += JOHN
                if (cploc == 1):
                    nof += JOHN
                if (cploc == 2):
                    raz += JOHN
                if (cploc == 3):
                    tel += JOHN
                if (cploc == 4):
                    con += JOHN
                if (cploc == 5):
                    end += JOHN
                if (cploc == 6):
                    cid += JOHN
                if (cploc == 7):
                    est += JOHN
                if (cploc == 8):
                    cep += JOHN
                if (cploc == 9):
                    equ += JOHN
                if (cploc == 10):
                    nus += JOHN
                if (cploc == 11):
                    cot += JOHN
            if (numinho == 254):
                cploc += 1
                numinho = 0
        if (cploc == 12):
            supla = (nc,nof,raz,tel,con,end,cid,est,cep,equ,nus,cot)
            lisupla.append(supla)
            nc = ""
            nof = ""
            raz = ""
            tel = ""
            con = ""
            end = ""
            cid = ""
            est = ""
            cep = ""
            equ = ""
            nus = ""
            cot = ""
            cploc = 0
    DICU = {}
    for j in lisupla:
        papito = (j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8],j[9],j[10],j[11])
        DICU[j[0]] = papito
    return (DICU)

#TUPLA LOG
def loGOco(USR,ACT):
    from datetime import datetime
    AC = ""
    if (ACT == 11):
        AC = "Login."
    if (ACT == 12):
        AC = "Logout."
    if (ACT == 20):
        AC = "Cadastro usuario."
    if (ACT == 21):
        AC = "Cadastro usuario: Alterou senha."
    if (ACT == 22):
        AC = "Remocao usuario."
    if (ACT == 23):
        AC = "Cadastro usuario: Alterou nivel acesso."
    if (ACT == 3):
        AC = "Cadastro cliente."
    if (ACT == 4):
        AC = "Remocao cliente."
    if (ACT == 5):
        AC = "Busca cliente."
    if (ACT == 6):
        AC = "Atualizacao cliente."
    if (ACT == 7):
        AC = "Impressao arquivo."
    if (ACT == 71):
        AC = "Consulta log."
    if (ACT == 8):
        AC = "Saida do sistema."

    X = datetime.now()
    MOCO = (USR+":",str(X.day)+"/"+str(X.month)+"/"+str(X.year)+" - "+str(X.hour)+":"+str(X.minute)+":"+str(X.second)+":",AC)
    return (MOCO)

#STRING PARA ARQUIVO LOG
def GERALOG(LIST):
    STR_LOG = ""
    for tp in LIST:
        for it in tp:
            if (it != "_") or (it != "\n"):
                STR_LOG += it
                STR_LOG += "_"
        STR_LOG += "\n"
    return (STR_LOG)

#NUCLEO PRINCIPAL

#INICIALIZACAO
User_Power = ""
User_Passw_Compare = ""
USR = open("usuarios.txt","r")
USRSTR = USR.read()
User_Dic = XRISTE(USRSTR)
ELE = open("elementos.txt","r")
ELESTR = ELE.read()
Data_Dic = CHRISTUS(ELESTR)
Log_Occur = ""
Log_STR = ""
USREXTSTR = ""
ELEEXTSTR = ""

#LEITOR DO LOG
LOGGYR = open("log.txt","r")
LS = LOGGYR.read()
Log_List = []
ct = 0
ONE = ""
TWO = ""
THREE = ""
TUP = ""
ww = ""
for ls in LS:
    if (ls != "_") and (ls != "\n"):
        ww += ls
    if (ls == "_"):
        if (ct == 0):
            ONE = ww
            ww = ""
        if (ct == 1):
            TWO = ww
            ww = ""
        if (ct == 2):
            THREE = ww
            ww = ""
        ct += 1
    if (ls == "\n"):
        ct = 0
        TUP = (ONE,TWO,THREE)
        Log_List.append(TUP)
        ONE = ""
        TWO = ""
        THREE = ""
        ww = ""

print(User_Dic)
print(Data_Dic)

#MAGIC BEGINS
Maain_Loop = True
User_OK = False
freQ = 0
while (Maain_Loop == True):
    print("\n"+"******************************************************"+"\n"+"MINILAB NORDESTE - CADASTRO DE CLIENTES E EQUIPAMENTOS"+"\n"+"******************************************************","\n")
    ct = 0
    #LOGIN
    print("***LOGIN***"+"\n")
    User_Current = str(input("Usuario (digite 'sair' para sair):"))
    if (User_Current != "sair"):
        User_Password = str(input("Senha:"))
    else:
        User_Password = ""
        if (freQ > 0):
            LOGGY = open("log.txt", "w")
            Log_STR = GERALOG(Log_List)
            LOGGY.write(Log_STR)
            LOGGY.close()
            USREXTSTR = ELEISSON(User_Dic)
            USY = open("usuarios.txt", "w")
            USY.write(USREXTSTR)
            USY.close()
            ELEEXTSTR = ELEISSON(Data_Dic)
            ELY = open("elementos.txt", "w")
            ELY.write(ELEEXTSTR)
            ELY.close()

    for u in User_Dic.keys():
        if (u == User_Current):
            User_Passw_Compare = User_Dic[u][0]
            ct += 1
            if (User_Password == User_Passw_Compare):
                User_Power = int(User_Dic[u][1])
                User_OK = True
                ct += 1
                freQ += 1
                Log_Occur = loGOco(User_Current,11)
                Log_List.append(Log_Occur)
            if (User_Password != User_Passw_Compare):
                User_OK = False
                print("Senha invalida!","\n")
    if (ct == 0) and (User_Current != "sair"):
        User_OK = False
        Maain_Loop = True
        print("Usuario inexistente!","\n")
    if (User_Current == "sair"):
        User_OK = False
        Maain_Loop = False
        User_Power = ""

#MENU PRINCIPAL
    if (User_OK == True):
        Menu_Loop = True
        while (Menu_Loop == True):
            if (User_Power == 4) or (User_Power == 3):
                print("***DIGITE A OPCAO DESEJADA***" + "\n")
                print("cr - CADASTRO DE USUARIO")
                print("cc - CADASTRO DE CLIENTE")
                print("cl - CONSULTA DE CLIENTES")
                print("lo - LOGOUT")
                print("sair - SAIR DO SISTEMA"+"\n")
            if (User_Power == 2):
                print("***DIGITE A OPCAO DESEJADA***" + "\n")
                print("cc - CADASTRO DE CLIENTE")
                print("cl - CONSULTA DE CLIENTES")
                print("lo - LOGOUT")
                print("sair - SAIR DO SISTEMA"+"\n")
            if (User_Power == 1):
                print("***DIGITE A OPCAO DESEJADA***" + "\n")
                print("cl - CONSULTA DE CLIENTES")
                print("lo - LOGOUT")
                print("sair - SAIR DO SISTEMA"+"\n")
            oPtion = str(input("OPCAO>"))

            #SAIDA
            if (oPtion == "sair"):
                Maain_Loop = False
                Menu_Loop = False
                Log_Occur = loGOco(User_Current, 8)
                Log_List.append(Log_Occur)
                LOGGY = open("log.txt", "w")
                Log_STR = GERALOG(Log_List)
                LOGGY.write(Log_STR)
                LOGGY.close()
                USREXTSTR = ELEISSON(User_Dic)
                USY = open("usuarios.txt","w")
                USY.write(USREXTSTR)
                USY.close()
                ELEEXTSTR = ELEISSON(Data_Dic)
                ELY = open("elementos.txt","w")
                ELY.write(ELEEXTSTR)
                ELY.close()


            #LOGOUT
            if (oPtion == "lo"):
                Maain_Loop = True
                Menu_Loop = False
                Log_Occur = loGOco(User_Current, 12)
                Log_List.append(Log_Occur)

            #CADASTRO DE USUARIO
            if (oPtion == "cr"):
                lcr = True
                cr_count = 0
                LUSR = []
                TUPU = ""
                CR_oPtion = ""
                while (lcr == True):
                    if (User_Power == 4) or (User_Power == 3):
                        print("***CADASTRO DE USUARIO***"+"\n")
                        print("ad - CADASTRAR NOVO USUARIO")
                        print("as - ALTERAR SENHA")
                        print("ru - REMOVER USUARIO")
                        if (User_Power == 4):
                            print("nv - ALTERAR NIVEL DE USUARIO")
                        print("sair - SAIR"+"\n")
                        if (User_Power == 3):
                            print("\n")
                    CR_oPtion = str(input("OPCAO>"))
                    if (CR_oPtion == "ad"):
                        if (User_Power == 4) or (User_Power == 3):
                            NU = True
                            while (NU == True):
                                New_User = str(input("Digite o nome do novo usuario:"))
                                if (New_User == "") or (New_User == " ") or (New_User in User_Dic) or (New_User == User_Current):
                                    NU = True
                                else:
                                    NU = False
                            NP = True
                            while (NP == True):
                                New_Password = str(input("Digite a senha do novo usuario:"))
                                if (New_User == ""):
                                    NP = True
                                else:
                                    NP = False
                            if (User_Power == 4):
                                pinG = True
                                while (pinG == True):
                                    New_UserLevel = str(input("Digite 3 para Gerente, 2 para Tecnico ou 1 para Estagiario:"))
                                    if (New_UserLevel != "4") and (New_UserLevel != "3") and (New_UserLevel != "2") and (New_UserLevel != "1"):
                                        print("Nivel invalido."+"\n")
                                        pinG = True
                                    else:
                                        pinG = False
                            if (User_Power == 3):
                                New_UserLevel = "1"

                            print ("Novo usuario:",New_User)
                            print ("Senha:", New_Password)
                            if (User_Power == 4):
                                if (New_UserLevel == "1"):
                                    print("Estagiario"+"\n")
                                if (New_UserLevel == "2"):
                                    print("Tecnico"+"\n")
                                if (New_UserLevel == "3"):
                                    print("Gerente"+"\n")
                            if (User_Power == 3):
                                print("Estagiario"+"\n")
                            Ky = "a"
                            while (Ky != "s") and (Ky != "n") and (Ky != "S") and (Ky != "N"):
                                Ky = str(input("Confirma? (s/n):"))
                                if (Ky == "s") or (Ky == "S"):
                                    print("Usuario cadastrado com sucesso!"+"\n")
                                    User_Dic[New_User] = (New_Password,New_UserLevel)
                                    Log_Occur = loGOco(User_Current, 20)
                                    Log_List.append(Log_Occur)
                                    lcr = False
                                if (Ky == "n") or (Ky == "N"):
                                    print("Operacao cancelada!"+"\n")
                                    lcr = True
                    if (CR_oPtion == "sair"):
                        lcr = False

                    if (CR_oPtion == "ru"):
                        delly = True
                        while (delly == True):
                            NO_User = str(input("Digite o nome do usuario a ser removido:"))
                            if (NO_User in User_Dic) and (NO_User != "adm") and (NO_User != User_Current):
                                deaty = True
                                while (deaty == True):
                                    Kd = str(input("Confirma? (s/n)"))
                                    if (Kd == "s") or (Kd == "S"):
                                        User_Dic.pop(NO_User)
                                        Log_Occur = loGOco(User_Current, 22)
                                        Log_List.append(Log_Occur)
                                        print("Usuario removido com sucesso!"+"\n")
                                        deaty = False
                                        delly = False
                                    if (Kd == "N") or (Kd == "n"):
                                        print("\n")
                                        delly = False
                                        deaty = False
                            else:
                                delly = True
                                print("Usuario invalido!"+"\n")

                    if (CR_oPtion != "ad") and (CR_oPtion != "as") and (CR_oPtion != "ru") and (CR_oPtion != "nv") and (CR_oPtion != "sair"):
                        lcr = True
                        print("Opcao invalida!"+"\n")





    

















