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
    if (ACT == 24):
        AC = "Consulta usuario."
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

#MAGIC BEGINS
Maain_Loop = True
User_OK = False
freQ = 0
while (Maain_Loop == True):
    print("\n"+"******************************************************"+"\n"+"MINILAB NORDESTE - CADASTRO DE CLIENTES E EQUIPAMENTOS"+"\n"+"******************************************************","\n")
    ct = 0
    #LOGIN
    print("***LOGIN***"+"\n")
    print("Digite o nome de usuario ou 'sair' para sair."+"\n")
    User_Current = str(input("Usuario:"))
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
                print("cc - CADASTRO DE CLIENTES")
                print("cl - CONSULTA CLIENTES")
                print("cg - CONSULTA LOG")
                print("lo - LOGOUT")
                print("sair - SAIR DO SISTEMA"+"\n")
            if (User_Power == 2):
                print("***DIGITE A OPCAO DESEJADA***" + "\n")
                print("cc - CADASTRO DE CLIENTES")
                print("cl - CONSULTA CLIENTES")
                print("lo - LOGOUT")
                print("sair - SAIR DO SISTEMA"+"\n")
            if (User_Power == 1):
                print("***DIGITE A OPCAO DESEJADA***" + "\n")
                print("cl - CONSULTA CLIENTES")
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
                LUSR = []
                TUPU = ""
                CR_oPtion = ""
                while (lcr == True):
                    if (User_Power == 4) or (User_Power == 3):
                        print("***CADASTRO DE USUARIO***"+"\n")
                        print("ad - CADASTRAR NOVO USUARIO")
                        print("as - ALTERAR SENHA")
                        print("ru - REMOVER USUARIO")
                        print("su - MOSTRAR USUARIOS")
                        if (User_Power == 4):
                            print("nv - ALTERAR NIVEL DE USUARIO")
                        print("sair - SAIR"+"\n")
                        
                    CR_oPtion = str(input("OPCAO>"))

                    if (CR_oPtion == "ad"):
                        if (User_Power == 4) or (User_Power == 3):
                            NU = True
                            while (NU == True):
                                New_User = str(input("Digite o nome do novo usuario:"))
                                if (New_User == "sair"):
                                    NU = False
                                else:
                                    if (New_User != "") and (New_User != " ") and (New_User not in User_Dic) and (New_User != User_Current):
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
                                        bb = True
                                        while (bb == True):
                                            Ky = str(input("Confirma? (s/n):"))
                                            if (Ky == "s") or (Ky == "S"):
                                                print("Usuario cadastrado com sucesso!"+"\n")
                                                User_Dic[New_User] = (New_Password,New_UserLevel)
                                                Log_Occur = loGOco(User_Current, 20)
                                                Log_List.append(Log_Occur)
                                                lcr = False
                                                bb = False
                                                NU = False
                                            if (Ky == "n") or (Ky == "N"):
                                                print("Operacao cancelada!"+"\n")
                                                bb = False
                                                lcr = False
                                                NU = False
                    if (CR_oPtion == "sair"):
                        lcr = False

                    if (CR_oPtion == "ru") and ((User_Power == 4) or (User_Power == 3)):
                        delly = True
                        while (delly == True):
                            NO_User = str(input("Digite o nome do usuario a ser removido:"))
                            if (NO_User == "sair"):
                                delly = False
                            else:
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
                                            print("Operacao cancelada!"+"\n")
                                            delly = False
                                            deaty = False
                                else:
                                    delly = True
                                    print("Usuario invalido!"+"\n")

                    if (CR_oPtion == "as") and ((User_Power == 4) or (User_Power == 3)):
                        las = True
                        while (las == True):
                            print("Alterar senha de usuario.")
                            Pass_User_Change = str(input("Digite o usuario:"))
                            if (Pass_User_Change == "sair"):
                                las = False
                            else:
                                if (Pass_User_Change in User_Dic) and (Pass_User_Change != "adm") and (Pass_User_Change != User_Current):
                                    TupIn = User_Dic[Pass_User_Change]
                                    Pass_New = str(input("Digite a nova senha:"))
                                    ll = True
                                    while (ll == True):
                                        oppsw = str(input("Confirma? (s/n)"))
                                        if (oppsw == "S") or (oppsw == "s"):
                                            PW_Old = TupIn[1]
                                            TupOut = (Pass_New,PW_Old)
                                            User_Dic[Pass_User_Change] = TupOut
                                            Log_Occur = loGOco(User_Current, 21)
                                            Log_List.append(Log_Occur)
                                            print ("Senha alterada com sucesso!"+"\n")
                                            ll = False
                                            las = False
                                        if (oppsw == "N") or (oppsw == "n"):
                                            print ("Operacao cancelada!"+"\n")
                                            ll = False
                                            las = False

                    if (CR_oPtion == "nv") and (User_Power == 4):
                        lnv = True
                        while (lnv == True):
                            print("Alterar nivel do usuario.")
                            LVL_User_Change = str(input("Digite o usuario:"))
                            if (LVL_User_Change == "sair"):
                                lnv = False
                            else:
                                if (LVL_User_Change in User_Dic) and (LVL_User_Change != "adm") and (LVL_User_Change != User_Current):
                                    TupyIn = User_Dic[LVL_User_Change]
                                    print("Escolha: 3 - Gerente, 2 - Técnico ou 1 - Estagiário")
                                    LVL_New = str(input("Digite o novo nivel:"))
                                    if (LVL_New != "1") and (LVL_New != "2") and (LVL_New != "3"):
                                        print("Nivel invalido."+"\n")
                                        lnv = True
                                    else:
                                        ln = True
                                        while (ln == True):
                                            oplvl = str(input("Confirma? (s/n)"))
                                            if (oplvl == "S") or (oplvl == "s"):
                                                PS_Old = TupyIn[0]
                                                TupyOut = (PS_Old,LVL_New)
                                                User_Dic[LVL_User_Change] = TupyOut
                                                Log_Occur = loGOco(User_Current, 23)
                                                Log_List.append(Log_Occur)
                                                print ("Nivel alterado com sucesso!"+"\n")
                                                ln = False
                                                lnv = False
                                            if (oplvl == "N") or (oplvl == "n"):
                                                print ("Operacao cancelada!"+"\n")
                                                ln = False
                                                lnv = False

                    if (CR_oPtion == "su") and ((User_Power == 4) or (User_Power == 3)):
                        for usyy in User_Dic.keys():
                            if (usyy == "adm") and (User_Power == 3):
                                dummy = 0
                            else:
                                print("Usuario:",usyy)
                                print("Senha:",User_Dic[usyy][0])
                                if (User_Dic[usyy][1] == "1"):
                                    print("Estagiario"+"\n")
                                if (User_Dic[usyy][1] == "2"):
                                    print("Tecnico"+"\n")
                                if (User_Dic[usyy][1] == "3"):
                                    print("Gerente"+"\n")
                                if (User_Dic[usyy][1] == "4") and (User_Power == 4):
                                    print("Administrador"+"\n")
                        Log_Occur = loGOco(User_Current,24)
                        Log_List.append(Log_Occur)

                    if (CR_oPtion != "ad") and (CR_oPtion != "su") and (CR_oPtion != "as") and (CR_oPtion != "ru") and (CR_oPtion != "nv") and (CR_oPtion != "sair"):
                        lcr = True
                        print("Opcao invalida!"+"\n")
            
            #CADASTRO DE CLIENTES
            if (oPtion == "cc") and (User_Power != 1):
                cc_Loop = True
                while (cc_Loop == True):
                    print("***CADASTRO DE CLIENTES***"+"\n")
                    print("ci - CADASTRAR NOVO CLIENTE")
                    print("ac - ALTERAR DADOS DE CLIENTE")
                    print("rc - REMOVER CLIENTE")
                    print("sair - SAIR"+"\n")
                    CC_oPtion = str(input("OPCAO>"))
                    if (CC_oPtion == "sair"):
                        cc_Loop = False
                    if (CC_oPtion != "ci") and (CC_oPtion != "ac") and (CC_oPtion != "rc") and (CC_oPtion != "sair"):
                        cc_Loop = True
                        print("Opcao invalida!"+"\n")
                    if (CC_oPtion == "ci"):
                        CCpk = str(input("Cadastro de novo cliente. Deseja continuar? (s/n):"))
                        if (CCpk == "n") or (CCpk == "N"):
                            print("Operacao cancelada!"+"\n")
                            cc_Loop = True
                        if (CCpk == "S") or (CCpk == "s"):
                            print("\n")
                            pree_loop = True
                            while (pree_loop == True):
                                Codcli = str((Maior_Numero(Data_Dic)) + 1)
                                print ("Codigo de cliente:",Codcli)
                                Nome_Fantasia = str(input("Nome Fantasia:"))
                                if (Nome_Fantasia == "sair"):
                                    pree_loop = False
                                else:
                                    Razao_Social = str(input("Razao Social:"))
                                    Tele = str(input("Telefone:"))
                                    Nom = str(input("Pessoa de contato:"))
                                    Ende = str(input("Endereco:"))
                                    Cida = str(input("Cidade:"))
                                    Estad = str(input("Estado:"))
                                    cEp = str(input("CEP.:"))
                                    eQp = str(input("Equipamento / Modelo:"))
                                    nSe = str(input("Numero de Serie:"))
                                    cOntr = str(input("Contrato:"))
                                    cliente_Data_Tup = (Nome_Fantasia,Razao_Social,Tele,Nom,Ende,Cida,Estad,cEp,eQp,nSe,cOntr)
                                    print("\n"+"Dados do cliente:"+"\n")
                                    print("Codigo de cliente:",Codcli)
                                    print("Nome Fantasia:",Nome_Fantasia)
                                    print("Razao Social:",Razao_Social)
                                    print("Telefone:",Tele)
                                    print("Pessoa de contato:",Nom)
                                    print("Endereco:",Ende)
                                    print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                    print("Equipamento / Modelo:",eQp,"   Numero de Serie:",nSe)
                                    print("Contrato:",cOntr,"\n")
                                    ooop = str(input("Deseja cadastrar novo cliente? (s/n):"))
                                    if (ooop == "n") or (ooop == "N"):
                                        pree_loop = False
                                        print("Operacao cancelada!"+"\n")
                                    if (ooop == "s") or (ooop == "S"):
                                        Data_Dic[Codcli] = cliente_Data_Tup
                                        Log_Occur = loGOco(User_Current,3)
                                        Log_List.append(Log_Occur)
                                        print ("Cliente cadastrado com sucesso!"+"\n")
                                        pree_loop = False
                                        cc_Loop = False
                    if (CC_oPtion == "ac"):
                        CCpp = str(input("Alterar cadastro de cliente. Deseja continuar? (s/n):"))
                        if (CCpp == "n") or (CCpp == "N"):
                            print("Operacao cancelada!"+"\n")
                            cc_Loop = True
                        if (CCpp == "S") or (CCpp == "s"):
                            print("\n")
                            pre_lop = True
                            while (pre_lop == True):
                                Data_Entry_ac = str(input("Digite o codigo de cliente:"))
                                if (Data_Entry_ac in Data_Dic.keys()):
                                    Tup_Cliente = Data_Dic[Data_Entry_ac]
                                    Codcli = Data_Entry_ac
                                    Nome_Fantasia = Tup_Cliente[0]
                                    Razao_Social = Tup_Cliente[1]
                                    Tele = Tup_Cliente[2]
                                    Nom = Tup_Cliente[3]
                                    Ende = Tup_Cliente[4]
                                    Cida = Tup_Cliente[5]
                                    Estad = Tup_Cliente[6]
                                    cEp = Tup_Cliente[7]
                                    eQp = Tup_Cliente[8]
                                    nSe = Tup_Cliente[9]
                                    cOntr = Tup_Cliente[10]
                                    Altera_Dados_Loop = True
                                    while(Altera_Dados_Loop == True):
                                        print("\n"+"Dados do cliente:"+"\n")
                                        print("Codigo de cliente:",Codcli)
                                        print("Nome Fantasia:",Nome_Fantasia)
                                        print("Razao Social:",Razao_Social)
                                        print("Telefone:",Tele)
                                        print("Pessoa de contato:",Nom)
                                        print("Endereco:",Ende)
                                        print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                        print("Equipamento / Modelo:",eQp,"   Numero de Serie:",nSe)
                                        print("Contrato:",cOntr,"\n")
                                        print("Selecione qual dado deseja alterar:"+"\n")
                                        print("1 Nome Fantasia")
                                        print("2 Razao Social")
                                        print("3 Telefone")
                                        print("4 Pessoa de contato")
                                        print("5 Endereco")
                                        print("6 Cidade")
                                        print("7 Estado")
                                        print("8 CEP")
                                        print("9 Equipamento / Modelo")
                                        print("10 Numero de Serie")
                                        print("11 Contrato")
                                        print("12 Alterar todos os dados"+"\n")
                                        Data_Opt = str(input("OPCAO>"))
                                        if (Data_Opt == "1") or (Data_Opt == "12"):
                                            Nome_Fantasia = str(input("Nome Fantasia:"))
                                        if (Data_Opt == "2") or (Data_Opt == "12"):
                                            Razao_Social = str(input("Razao Social:"))
                                        if (Data_Opt == "3") or (Data_Opt == "12"):
                                            Tele = str(input("Telefone:"))
                                        if (Data_Opt == "4") or (Data_Opt == "12"):
                                            Nom = str(input("Pessoa de contato:"))
                                        if (Data_Opt == "5") or (Data_Opt == "12"):
                                            Ende = str(input("Endereco:"))
                                        if (Data_Opt == "6") or (Data_Opt == "12"):
                                            Cida = str(input("Cidade:"))
                                        if (Data_Opt == "7") or (Data_Opt == "12"):
                                            Estad = str(input("Estado:"))
                                        if (Data_Opt == "8") or (Data_Opt == "12"):
                                            cEp = str(input("CEP.:"))
                                        if (Data_Opt == "9") or (Data_Opt == "12"):
                                            eQp = str(input("Equipamento / Modelo:"))
                                        if (Data_Opt == "10") or (Data_Opt == "12"):
                                            nSe = str(input("Numero de Serie:"))
                                        if (Data_Opt == "11") or (Data_Opt == "12"):
                                            cOntr = str(input("Contrato:"))
                                        print("\n"+"Novos dados do cliente:"+"\n")
                                        print("Codigo de cliente:",Codcli)
                                        print("Nome Fantasia:",Nome_Fantasia)
                                        print("Razao Social:",Razao_Social)
                                        print("Telefone:",Tele)
                                        print("Pessoa de contato:",Nom)
                                        print("Endereco:",Ende)
                                        print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                        print("Equipamento / Modelo:",eQp,"   Numero de Serie:",nSe)
                                        print("Contrato:",cOntr,"\n")
                                        ppyp = str(input("Deseja alterar mais algum dado? (s/n)"))
                                        if (ppyp == "s") or (ppyp == "S"):
                                            Altera_Dados_Loop = True
                                        else:
                                            Altera_Dados_Loop = False
                                            ynloop = True
                                            while (ynloop == True):
                                                ac_yn = str(input("Deseja atualizar os dados? (s/n)"))
                                                if (ac_yn == "n") or (ac_yn == "N"):
                                                    print("Operacao cancelada!"+"\n")
                                                    cc_Loop = False
                                                    pre_lop = False
                                                    ynloop = False
                                                if (ac_yn == "s") or (ac_yn == "S"):
                                                    Tup_Cliente = (Nome_Fantasia,Razao_Social,Tele,Nom,Ende,Cida,Estad,cEp,eQp,nSe,cOntr)
                                                    Data_Dic[Codcli] = Tup_Cliente
                                                    Log_Occur = loGOco(User_Current,6)
                                                    Log_List.append(Log_Occur)
                                                    print("Dados de Cliente atualizados com sucesso!"+"\n")
                                                    cc_Loop = False
                                                    pre_lop = False
                                                    ynloop = False
                                else:
                                    pre_lop = False
                                    print("Cliente inexistente!"+"\n")

                    if (CC_oPtion == "rc"):
                        Loop_Death = True
                        while(Loop_Death == True):
                            Death_Toll = str(input("Remover cliente. Deseja continuar? (s/n)"))
                            if (Death_Toll == "n") or (Death_Toll == "N"):
                                Loop_Death = False
                            if (Death_Toll == "s") or (Death_Toll == "S"):
                                print("\n")
                                Death_Chosen = str(input("Digite o codigo de cliente:"))
                                if (Death_Chosen in Data_Dic.keys()):
                                    Tup_Death = Data_Dic[Death_Chosen]
                                    Codcli = Death_Chosen
                                    Nome_Fantasia = Tup_Death[0]
                                    Razao_Social = Tup_Death[1]
                                    Tele = Tup_Death[2]
                                    Nom = Tup_Death[3]
                                    Ende = Tup_Death[4]
                                    Cida = Tup_Death[5]
                                    Estad = Tup_Death[6]
                                    cEp = Tup_Death[7]
                                    eQp = Tup_Death[8]
                                    nSe = Tup_Death[9]
                                    cOntr = Tup_Death[10]
                                    print("\n"+"Dados do cliente:"+"\n")
                                    print("Codigo de cliente:",Codcli)
                                    print("Nome Fantasia:",Nome_Fantasia)
                                    print("Razao Social:",Razao_Social)
                                    print("Telefone:",Tele)
                                    print("Pessoa de contato:",Nom)
                                    print("Endereco:",Ende)
                                    print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                    print("Equipamento / Modelo:",eQp,"   Numero de Serie:",nSe)
                                    print("Contrato:",cOntr,"\n")
                                    Death_Angel = str(input("Deseja realmente excluir todos os dados cliente? (s/n)"))
                                    if (Death_Angel == "n") or (Death_Angel == "N"):
                                        print("Operacao cancelada!"+"\n")
                                        Loop_Death == False
                                    if (Death_Angel == "s") or (Death_Angel == "S"):
                                        del Data_Dic[Codcli]
                                        Log_Occur = loGOco(User_Current,4)
                                        Log_List.append(Log_Occur)
                                        print("Cliente removido com sucesso!"+"\n")
                                        cc_Loop = False
                                        Loop_Death = False
                                else:
                                    Loop_Death == True
                                    print("Cliente inexistente!"+"\n")




























    

















