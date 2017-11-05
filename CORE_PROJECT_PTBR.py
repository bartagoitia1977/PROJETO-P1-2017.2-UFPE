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
        AC = "Cadastro usuário."
    if (ACT == 21):
        AC = "Cadastro usuário: Alterou senha."
    if (ACT == 22):
        AC = "Remoção usuário."
    if (ACT == 23):
        AC = "Cadastro usuário: Alterou nivel acesso."
    if (ACT == 24):
        AC = "Consulta usuário."
    if (ACT == 3):
        AC = "Cadastro cliente."
    if (ACT == 4):
        AC = "Remoção cliente."
    if (ACT == 5):
        AC = "Busca cliente."
    if (ACT == 6):
        AC = "Atualização cliente."
    if (ACT == 7):
        AC = "Impressão arquivo."
    if (ACT == 71):
        AC = "Consulta log."
    if (ACT == 8):
        AC = "Saída do sistema."

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

#VERIFICA MAIUSCULO E MINUSCULO STRING
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

#STRING PARA IMPRESSAO ELEMENTOS
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

#STRING PARA EXIBICAO LOG
def LogOPR(tuplalog):
    usr = tuplalog[0]
    US = ""
    for l in usr:
        if (l != ":"):
            US += l
    dathr = tuplalog[1]
    ocorr = tuplalog[2]
    print("Usuário:",US)
    print("Data e hora:",dathr)
    print("Ocorrência:",ocorr)
    print("\n")

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
    print("\n"+"************************************************************"+"\n"+"   MINILAB NORDESTE - CADASTRO DE CLIENTES E EQUIPAMENTOS   "+"\n"+"************************************************************","\n")
    ct = 0
    #LOGIN
    print("***LOGIN***"+"\n")
    print("Digite o nome de usuário ou 'sair' para sair."+"\n")
    User_Current = str(input("Usuário:"))
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
                print("Senha inválida!","\n")
    if (ct == 0) and (User_Current != "sair"):
        User_OK = False
        Maain_Loop = True
        print("Usuário inexistente!","\n")
    if (User_Current == "sair"):
        User_OK = False
        Maain_Loop = False
        User_Power = ""

#MENU PRINCIPAL
    if (User_OK == True):
        Menu_Loop = True
        while (Menu_Loop == True):
            if (User_Power == 4) or (User_Power == 3):
                print("***DIGITE A OPÇÃO DESEJADA***" + "\n")
                print("cr - CADASTRO DE USUÁRIO")
                print("cc - CADASTRO DE CLIENTES")
                print("cl - CONSULTA CLIENTES")
                print("im - GERA ARQUIVO DE CLIENTES")
                print("cg - CONSULTA LOG")
                print("lo - LOGOUT")
                print("sair - SAIR DO SISTEMA"+"\n")
            if (User_Power == 2):
                print("***DIGITE A OPCAO DESEJADA***" + "\n")
                print("cc - CADASTRO DE CLIENTES")
                print("cl - CONSULTA CLIENTES")
                print("im - GERA ARQUIVO DE CLIENTES")
                print("lo - LOGOUT")
                print("sair - SAIR DO SISTEMA"+"\n")
            if (User_Power == 1):
                print("***DIGITE A OPCAO DESEJADA***" + "\n")
                print("cl - CONSULTA CLIENTES")
                print("lo - LOGOUT")
                print("sair - SAIR DO SISTEMA"+"\n")
            oPtion = str(input("OPÇÃO>"))

            #OPCAO INVALIDA GERAL
            if (oPtion != "cr") and (oPtion != "cc") and (oPtion != "cl") and (oPtion != "im") and (oPtion != "cg") and (oPtion != "lo") and (oPtion != "sair"):
                Menu_Loop = True
                print("Opção inválida!"+"\n")

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
                        print("***CADASTRO DE USUÁRIO***"+"\n")
                        print("ad - CADASTRAR NOVO USUÁRIO")
                        print("as - ALTERAR SENHA")
                        print("ru - REMOVER USUÁRIO")
                        print("su - MOSTRAR USUÁRIOS")
                        if (User_Power == 4):
                            print("nv - ALTERAR NÍVEL DE USUÁRIO")
                        print("sair - SAIR"+"\n")
                        
                    CR_oPtion = str(input("OPÇÃO>"))

                    #CADASTRO DE NOVO USUARIO
                    if (CR_oPtion == "ad"):
                        if (User_Power == 4) or (User_Power == 3):
                            NU = True
                            while (NU == True):
                                New_User = str(input("Digite o nome do novo usuário:"))
                                if (New_User == "sair"):
                                    NU = False
                                else:
                                    if (New_User != "") and (New_User != " ") and (New_User not in User_Dic) and (New_User != User_Current):
                                        NP = True
                                        while (NP == True):
                                            New_Password = str(input("Digite a senha do novo usuário:"))
                                            if (New_User == ""):
                                                NP = True
                                            else:
                                                NP = False
                                        if (User_Power == 4):
                                            pinG = True
                                            while (pinG == True):
                                                New_UserLevel = str(input("Digite 3 para Gerente, 2 para Técnico ou 1 para Estagiário:"))
                                                if (New_UserLevel != "4") and (New_UserLevel != "3") and (New_UserLevel != "2") and (New_UserLevel != "1"):
                                                    print("Nivel inválido."+"\n")
                                                    pinG = True
                                                else:
                                                    pinG = False
                                        if (User_Power == 3):
                                            New_UserLevel = "1"

                                        print ("Novo usuário:",New_User)
                                        print ("Senha:", New_Password)
                                        if (User_Power == 4):
                                            if (New_UserLevel == "1"):
                                                print("Estagiário"+"\n")
                                            if (New_UserLevel == "2"):
                                                print("Técnico"+"\n")
                                            if (New_UserLevel == "3"):
                                                print("Gerente"+"\n")
                                        if (User_Power == 3):
                                            print("Estagiário"+"\n")
                                        bb = True
                                        while (bb == True):
                                            Ky = str(input("Confirma? (s/n):"))
                                            if (Ky == "s") or (Ky == "S"):
                                                print("Usuário cadastrado com sucesso!"+"\n")
                                                User_Dic[New_User] = (New_Password,New_UserLevel)
                                                Log_Occur = loGOco(User_Current, 20)
                                                Log_List.append(Log_Occur)
                                                lcr = True
                                                bb = False
                                                NU = False
                                            if (Ky == "n") or (Ky == "N"):
                                                print("Operação cancelada!"+"\n")
                                                bb = False
                                                lcr = True
                                                NU = False
                    #SAIR DO SUBMENU USUARIO
                    if (CR_oPtion == "sair"):
                        lcr = False

                    #REMOVER USUARIO
                    if (CR_oPtion == "ru") and ((User_Power == 4) or (User_Power == 3)):
                        delly = True
                        while (delly == True):
                            NO_User = str(input("Digite o nome do usuário a ser removido:"))
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
                                            print("Usuário removido com sucesso!"+"\n")
                                            deaty = False
                                            delly = False
                                            lcr = True
                                        if (Kd == "N") or (Kd == "n"):
                                            print("Operação cancelada!"+"\n")
                                            delly = False
                                            deaty = False
                                            lcr = True
                                else:
                                    delly = True
                                    print("Usuário inválido!"+"\n")

                    #ALTERAR SENHA
                    if (CR_oPtion == "as") and ((User_Power == 4) or (User_Power == 3)):
                        las = True
                        while (las == True):
                            print("Alterar senha de usuário.")
                            Pass_User_Change = str(input("Digite o usuário:"))
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
                                            lcr = True
                                        if (oppsw == "N") or (oppsw == "n"):
                                            print ("Operação cancelada!"+"\n")
                                            ll = False
                                            las = False
                                            lcr = True

                    #ALTERAR NIVEL USUARIO
                    if (CR_oPtion == "nv") and (User_Power == 4):
                        lnv = True
                        while (lnv == True):
                            print("Alterar nível do usuário.")
                            LVL_User_Change = str(input("Digite o usuário:"))
                            if (LVL_User_Change == "sair"):
                                lnv = False
                            else:
                                if (LVL_User_Change in User_Dic) and (LVL_User_Change != "adm") and (LVL_User_Change != User_Current):
                                    TupyIn = User_Dic[LVL_User_Change]
                                    print("Escolha: 3 - Gerente, 2 - Técnico ou 1 - Estagiário")
                                    LVL_New = str(input("Digite o novo nível:"))
                                    if (LVL_New != "1") and (LVL_New != "2") and (LVL_New != "3"):
                                        print("Nível inválido."+"\n")
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
                                                print ("Nível alterado com sucesso!"+"\n")
                                                ln = False
                                                lnv = False
                                                lcr = True
                                            if (oplvl == "N") or (oplvl == "n"):
                                                print ("Operação cancelada!"+"\n")
                                                ln = False
                                                lnv = False
                                                lcr = True

                    #CONSULTA USUARIOS
                    if (CR_oPtion == "su") and ((User_Power == 4) or (User_Power == 3)):
                        for usyy in User_Dic.keys():
                            if (usyy == "adm") and (User_Power == 3):
                                dummy = 0
                            else:
                                print("Usuário:",usyy)
                                print("Senha:",User_Dic[usyy][0])
                                if (User_Dic[usyy][1] == "1"):
                                    print("Estagiário"+"\n")
                                if (User_Dic[usyy][1] == "2"):
                                    print("Técnico"+"\n")
                                if (User_Dic[usyy][1] == "3"):
                                    print("Gerente"+"\n")
                                if (User_Dic[usyy][1] == "4") and (User_Power == 4):
                                    print("Administrador"+"\n")
                        Log_Occur = loGOco(User_Current,24)
                        Log_List.append(Log_Occur)
                        lcr = True

                    if (CR_oPtion != "ad") and (CR_oPtion != "su") and (CR_oPtion != "as") and (CR_oPtion != "ru") and (CR_oPtion != "nv") and (CR_oPtion != "sair"):
                        lcr = True
                        print("Opção inválida!"+"\n")
            
            #CADASTRO DE CLIENTES
            if (oPtion == "cc") and (User_Power != 1):
                cc_Loop = True
                while (cc_Loop == True):
                    print("***CADASTRO DE CLIENTES***"+"\n")
                    print("cn - CADASTRAR NOVO CLIENTE")
                    print("ac - ALTERAR DADOS DE CLIENTE")
                    print("rc - REMOVER CLIENTE")
                    print("sair - SAIR"+"\n")
                    CC_oPtion = str(input("OPÇÃO>"))
                    if (CC_oPtion == "sair"):
                        cc_Loop = False
                    if (CC_oPtion != "cn") and (CC_oPtion != "ac") and (CC_oPtion != "rc") and (CC_oPtion != "sair"):
                        cc_Loop = True
                        print("Opção invalida!"+"\n")
                    
                    #CADASTRAR NOVO CLIENTE
                    if (CC_oPtion == "cn"):
                        CCpk = str(input("Cadastro de novo cliente. Deseja continuar? (s/n):"))
                        if (CCpk == "n") or (CCpk == "N"):
                            print("Operação cancelada!"+"\n")
                            cc_Loop = True
                        if (CCpk == "S") or (CCpk == "s"):
                            print("\n")
                            print("Favor não utilizar acentos no cadastro. Ex.: 'á', 'é', 'ê', 'ã', etc."+"\n")
                            pree_loop = True
                            while (pree_loop == True):
                                Codcli = str((Maior_Numero(Data_Dic)) + 1)
                                print ("Código de cliente:",Codcli)
                                Nome_Fantasia = str(input("Nome Fantasia:"))
                                if (Nome_Fantasia == "sair"):
                                    pree_loop = False
                                    cc_Loop = True
                                else:
                                    Razao_Social = str(input("Razão Social:"))
                                    Tele = str(input("Telefone:"))
                                    Nom = str(input("Pessoa de contato:"))
                                    Ende = str(input("Endereço:"))
                                    Cida = str(input("Cidade:"))
                                    Estad = str(input("Estado:"))
                                    cEp = str(input("CEP.:"))
                                    eQp = str(input("Equipamento / Modelo:"))
                                    nSe = str(input("Número de Série:"))
                                    cOntr = str(input("Contrato:"))
                                    cliente_Data_Tup = (Nome_Fantasia,Razao_Social,Tele,Nom,Ende,Cida,Estad,cEp,eQp,nSe,cOntr)
                                    print("\n"+"Dados do cliente:"+"\n")
                                    print("Codigo de cliente:",Codcli)
                                    print("Nome Fantasia:",Nome_Fantasia)
                                    print("Razão Social:",Razao_Social)
                                    print("Telefone:",Tele)
                                    print("Pessoa de contato:",Nom)
                                    print("Endereço:",Ende)
                                    print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                    print("Equipamento / Modelo:",eQp,"   Número de Série:",nSe)
                                    print("Contrato:",cOntr,"\n")
                                    ooop = str(input("Confirma dados novo cliente? (s/n):"))
                                    if (ooop == "n") or (ooop == "N"):
                                        pree_loop = False
                                        cc_Loop = True
                                        print("Operação cancelada!"+"\n")
                                    if (ooop == "s") or (ooop == "S"):
                                        Data_Dic[Codcli] = cliente_Data_Tup
                                        Log_Occur = loGOco(User_Current,3)
                                        Log_List.append(Log_Occur)
                                        print ("Cliente cadastrado com sucesso!"+"\n")
                                        ops = str(input("Deseja cadastrar mais algum cliente? (s/n)"))
                                        if (ops == "n") or (ops == "N"):
                                            pree_loop = False
                                            cc_Loop = True
                                        else:
                                            pree_loop = True
                    
                    #ALTERAR CADASTRO DE CLIENTE
                    if (CC_oPtion == "ac"):
                        CCpp = str(input("Alterar cadastro de cliente. Deseja continuar? (s/n):"))
                        if (CCpp == "n") or (CCpp == "N"):
                            print("Operação cancelada!"+"\n")
                            cc_Loop = True
                        if (CCpp == "S") or (CCpp == "s"):
                            pre_lop = True
                            while (pre_lop == True):
                                print("\n"+"Escolha por:"+"\n")
                                print("1 - Código de cliente")
                                print("2 - Nome Fantasia")
                                print("3 - Cidade"+"\n")
                                opr = str (input("OPÇÃO>"))
                                if (opr == "1"):
                                    Data_Entry_ac = str(input("Digite o código de cliente:"))
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
                                            print("Código de cliente:",Codcli)
                                            print("Nome Fantasia:",Nome_Fantasia)
                                            print("Razão Social:",Razao_Social)
                                            print("Telefone:",Tele)
                                            print("Pessoa de contato:",Nom)
                                            print("Endereço:",Ende)
                                            print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                            print("Equipamento / Modelo:",eQp,"   Número de Série:",nSe)
                                            print("Contrato:",cOntr,"\n")
                                            print("Selecione qual dado deseja alterar:"+"\n")
                                            print("1 Nome Fantasia")
                                            print("2 Razão Social")
                                            print("3 Telefone")
                                            print("4 Pessoa de contato")
                                            print("5 Endereço")
                                            print("6 Cidade")
                                            print("7 Estado")
                                            print("8 CEP")
                                            print("9 Equipamento / Modelo")
                                            print("10 Número de Série")
                                            print("11 Contrato")
                                            print("12 Alterar todos os dados"+"\n")
                                            Data_Opt = str(input("OPÇÃO>"))
                                            if (Data_Opt == "1") or (Data_Opt == "12"):
                                                Nome_Fantasia = str(input("Nome Fantasia:"))
                                            if (Data_Opt == "2") or (Data_Opt == "12"):
                                                Razao_Social = str(input("Razão Social:"))
                                            if (Data_Opt == "3") or (Data_Opt == "12"):
                                                Tele = str(input("Telefone:"))
                                            if (Data_Opt == "4") or (Data_Opt == "12"):
                                                Nom = str(input("Pessoa de contato:"))
                                            if (Data_Opt == "5") or (Data_Opt == "12"):
                                                Ende = str(input("Endereço:"))
                                            if (Data_Opt == "6") or (Data_Opt == "12"):
                                                Cida = str(input("Cidade:"))
                                            if (Data_Opt == "7") or (Data_Opt == "12"):
                                                Estad = str(input("Estado:"))
                                            if (Data_Opt == "8") or (Data_Opt == "12"):
                                                cEp = str(input("CEP.:"))
                                            if (Data_Opt == "9") or (Data_Opt == "12"):
                                                eQp = str(input("Equipamento / Modelo:"))
                                            if (Data_Opt == "10") or (Data_Opt == "12"):
                                                nSe = str(input("Número de Série:"))
                                            if (Data_Opt == "11") or (Data_Opt == "12"):
                                                cOntr = str(input("Contrato:"))
                                            print("\n"+"Novos dados do cliente:"+"\n")
                                            print("Código de cliente:",Codcli)
                                            print("Nome Fantasia:",Nome_Fantasia)
                                            print("Razão Social:",Razao_Social)
                                            print("Telefone:",Tele)
                                            print("Pessoa de contato:",Nom)
                                            print("Endereco:",Ende)
                                            print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                            print("Equipamento / Modelo:",eQp,"   Número de Série:",nSe)
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
                                                        print("Operação cancelada!"+"\n")
                                                        cc_Loop = True
                                                        pre_lop = False
                                                        ynloop = False
                                                    if (ac_yn == "s") or (ac_yn == "S"):
                                                        Tup_Cliente = (Nome_Fantasia,Razao_Social,Tele,Nom,Ende,Cida,Estad,cEp,eQp,nSe,cOntr)
                                                        Data_Dic[Codcli] = Tup_Cliente
                                                        Log_Occur = loGOco(User_Current,6)
                                                        Log_List.append(Log_Occur)
                                                        print("Dados de Cliente atualizados com sucesso!"+"\n")
                                                        cc_Loop = True
                                                        pre_lop = False
                                                        ynloop = False
                                    else:
                                        pre_lop = False
                                        cc_Loop = True
                                        print("Cliente inexistente!"+"\n")

                                if (opr == "2"):
                                    Fantasy = str(input("Digite o Nome Fantasia:"))
                                    Tem_Nos_Dados = 0
                                    Liscli = []
                                    for val in Data_Dic.items():
                                        vlw = val[1]
                                        if (Mai_Min(Fantasy,vlw[0]) == True):
                                            Liscli.append(val[0])
                                            Codcli = val[0]
                                            Nome_Fantasia = vlw[0]
                                            Razao_Social = vlw[1]
                                            Tele = vlw[2]
                                            Nom = vlw[3]
                                            Ende = vlw[4]
                                            Cida = vlw[5]
                                            Estad = vlw[6]
                                            cEp = vlw[7]
                                            eQp = vlw[8]
                                            nSe = vlw[9]
                                            cOntr = vlw[10]
                                            print("\n"+"Dados do cliente:"+"\n")
                                            print("Código de cliente:",Codcli)
                                            print("Nome Fantasia:",Nome_Fantasia)
                                            print("Razão Social:",Razao_Social)
                                            print("Telefone:",Tele)
                                            print("Pessoa de contato:",Nom)
                                            print("Endereço:",Ende)
                                            print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                            print("Equipamento / Modelo:",eQp,"   Número de Série:",nSe)
                                            print("Contrato:",cOntr,"\n")
                                            Tem_Nos_Dados += 1
                                    if (Tem_Nos_Dados > 0):
                                        pinky = True
                                        while (pinky == True):
                                            coddy = str(input("Digite o cliente que deseja alterar:"))
                                            if (coddy == "sair"):
                                                pinky = False
                                                pre_lop = False
                                                cc_Loop = True
                                            else:
                                                if coddy in Liscli:
                                                    Tup_Cliente = Data_Dic[coddy]
                                                    Codcli = coddy
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
                                                        print("Código de cliente:",Codcli)
                                                        print("Nome Fantasia:",Nome_Fantasia)
                                                        print("Razão Social:",Razao_Social)
                                                        print("Telefone:",Tele)
                                                        print("Pessoa de contato:",Nom)
                                                        print("Endereço:",Ende)
                                                        print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                                        print("Equipamento / Modelo:",eQp,"   Número de Série:",nSe)
                                                        print("Contrato:",cOntr,"\n")
                                                        print("Selecione qual dado deseja alterar:"+"\n")
                                                        print("1 Nome Fantasia")
                                                        print("2 Razão Social")
                                                        print("3 Telefone")
                                                        print("4 Pessoa de contato")
                                                        print("5 Endereço")
                                                        print("6 Cidade")
                                                        print("7 Estado")
                                                        print("8 CEP")
                                                        print("9 Equipamento / Modelo")
                                                        print("10 Número de Série")
                                                        print("11 Contrato")
                                                        print("12 Alterar todos os dados"+"\n")
                                                        Data_Opt = str(input("OPÇÃO>"))
                                                        if (Data_Opt == "1") or (Data_Opt == "12"):
                                                            Nome_Fantasia = str(input("Nome Fantasia:"))
                                                        if (Data_Opt == "2") or (Data_Opt == "12"):
                                                            Razao_Social = str(input("Razão Social:"))
                                                        if (Data_Opt == "3") or (Data_Opt == "12"):
                                                            Tele = str(input("Telefone:"))
                                                        if (Data_Opt == "4") or (Data_Opt == "12"):
                                                            Nom = str(input("Pessoa de contato:"))
                                                        if (Data_Opt == "5") or (Data_Opt == "12"):
                                                            Ende = str(input("Endereço:"))
                                                        if (Data_Opt == "6") or (Data_Opt == "12"):
                                                            Cida = str(input("Cidade:"))
                                                        if (Data_Opt == "7") or (Data_Opt == "12"):
                                                            Estad = str(input("Estado:"))
                                                        if (Data_Opt == "8") or (Data_Opt == "12"):
                                                            cEp = str(input("CEP.:"))
                                                        if (Data_Opt == "9") or (Data_Opt == "12"):
                                                            eQp = str(input("Equipamento / Modelo:"))
                                                        if (Data_Opt == "10") or (Data_Opt == "12"):
                                                            nSe = str(input("Número de Série:"))
                                                        if (Data_Opt == "11") or (Data_Opt == "12"):
                                                            cOntr = str(input("Contrato:"))
                                                        print("\n"+"Novos dados do cliente:"+"\n")
                                                        print("Código de cliente:",Codcli)
                                                        print("Nome Fantasia:",Nome_Fantasia)
                                                        print("Razão Social:",Razao_Social)
                                                        print("Telefone:",Tele)
                                                        print("Pessoa de contato:",Nom)
                                                        print("Endereco:",Ende)
                                                        print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                                        print("Equipamento / Modelo:",eQp,"   Número de Série:",nSe)
                                                        print("Contrato:",cOntr,"\n")
                                                        ac_yn = str(input("Deseja atualizar os dados? (s/n)"))
                                                        if (ac_yn == "n") or (ac_yn == "N"):
                                                            print("Operação cancelada!"+"\n")
                                                            cc_Loop = True
                                                            pre_lop = False
                                                            pinky = False
                                                            Altera_Dados_Loop = False
                                                        if (ac_yn == "s") or (ac_yn == "S"):
                                                            Tup_Cliente = (Nome_Fantasia,Razao_Social,Tele,Nom,Ende,Cida,Estad,cEp,eQp,nSe,cOntr)
                                                            Data_Dic[Codcli] = Tup_Cliente
                                                            Log_Occur = loGOco(User_Current,6)
                                                            Log_List.append(Log_Occur)
                                                            print("Dados de Cliente atualizados com sucesso!"+"\n")
                                                            cc_Loop = True
                                                            pre_lop = False
                                                            pinky = False
                                                            ppyp = str(input("Deseja alterar mais algum dado? (s/n)"))
                                                            if (ppyp == "s") or (ppyp == "S"):
                                                                Altera_Dados_Loop = True
                                                            else:
                                                                Altera_Dados_Loop = False
                                                                cc_Loop = True
                                                                pre_lop = False
                                                                pinky = False
                                                else:
                                                    print("Cliente iválido!")
                                                    pinky = True
                                                    cc_Loop = True
                                    if (Tem_Nos_Dados == 0):
                                        print ("Cliente com Nome Fantasia inexistente!"+"\n")
                                        pre_lop = True

                                if (opr == "3"):
                                    CITY = str(input("Digite a Cidade:"))
                                    Tem_Nos_Dados = 0
                                    Liscli = []
                                    for val in Data_Dic.items():
                                        vlw = val[1]
                                        if (Mai_Min(CITY,vlw[5]) == True):
                                            Liscli.append(val[0])
                                            Codcli = val[0]
                                            Nome_Fantasia = vlw[0]
                                            Razao_Social = vlw[1]
                                            Tele = vlw[2]
                                            Nom = vlw[3]
                                            Ende = vlw[4]
                                            Cida = vlw[5]
                                            Estad = vlw[6]
                                            cEp = vlw[7]
                                            eQp = vlw[8]
                                            nSe = vlw[9]
                                            cOntr = vlw[10]
                                            print("\n"+"Dados do cliente:"+"\n")
                                            print("Código de cliente:",Codcli)
                                            print("Nome Fantasia:",Nome_Fantasia)
                                            print("Razão Social:",Razao_Social)
                                            print("Telefone:",Tele)
                                            print("Pessoa de contato:",Nom)
                                            print("Endereço:",Ende)
                                            print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                            print("Equipamento / Modelo:",eQp,"   Número de Série:",nSe)
                                            print("Contrato:",cOntr,"\n")
                                            Tem_Nos_Dados += 1
                                    if (Tem_Nos_Dados > 0):
                                        pinky = True
                                        while (pinky == True):
                                            coddy = str(input("Digite o cliente que deseja alterar:"))
                                            if (coddy == "sair"):
                                                print("Operação cancelada!"+"\n")
                                                cc_Loop = True
                                                pinky = False
                                                pre_lop = False
                                            else:
                                                if coddy in Liscli:
                                                    Tup_Cliente = Data_Dic[coddy]
                                                    Codcli = coddy
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
                                                        print("Código de cliente:",Codcli)
                                                        print("Nome Fantasia:",Nome_Fantasia)
                                                        print("Razão Social:",Razao_Social)
                                                        print("Telefone:",Tele)
                                                        print("Pessoa de contato:",Nom)
                                                        print("Endereço:",Ende)
                                                        print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                                        print("Equipamento / Modelo:",eQp,"   Número de Série:",nSe)
                                                        print("Contrato:",cOntr,"\n")
                                                        print("Selecione qual dado deseja alterar:"+"\n")
                                                        print("1 Nome Fantasia")
                                                        print("2 Razão Social")
                                                        print("3 Telefone")
                                                        print("4 Pessoa de contato")
                                                        print("5 Endereço")
                                                        print("6 Cidade")
                                                        print("7 Estado")
                                                        print("8 CEP")
                                                        print("9 Equipamento / Modelo")
                                                        print("10 Número de Série")
                                                        print("11 Contrato")
                                                        print("12 Alterar todos os dados"+"\n")
                                                        Data_Opt = str(input("OPÇÃO>"))
                                                        if (Data_Opt == "1") or (Data_Opt == "12"):
                                                            Nome_Fantasia = str(input("Nome Fantasia:"))
                                                        if (Data_Opt == "2") or (Data_Opt == "12"):
                                                            Razao_Social = str(input("Razão Social:"))
                                                        if (Data_Opt == "3") or (Data_Opt == "12"):
                                                            Tele = str(input("Telefone:"))
                                                        if (Data_Opt == "4") or (Data_Opt == "12"):
                                                            Nom = str(input("Pessoa de contato:"))
                                                        if (Data_Opt == "5") or (Data_Opt == "12"):
                                                            Ende = str(input("Endereço:"))
                                                        if (Data_Opt == "6") or (Data_Opt == "12"):
                                                            Cida = str(input("Cidade:"))
                                                        if (Data_Opt == "7") or (Data_Opt == "12"):
                                                            Estad = str(input("Estado:"))
                                                        if (Data_Opt == "8") or (Data_Opt == "12"):
                                                            cEp = str(input("CEP.:"))
                                                        if (Data_Opt == "9") or (Data_Opt == "12"):
                                                            eQp = str(input("Equipamento / Modelo:"))
                                                        if (Data_Opt == "10") or (Data_Opt == "12"):
                                                            nSe = str(input("Número de Série:"))
                                                        if (Data_Opt == "11") or (Data_Opt == "12"):
                                                            cOntr = str(input("Contrato:"))
                                                        print("\n"+"Novos dados do cliente:"+"\n")
                                                        print("Código de cliente:",Codcli)
                                                        print("Nome Fantasia:",Nome_Fantasia)
                                                        print("Razão Social:",Razao_Social)
                                                        print("Telefone:",Tele)
                                                        print("Pessoa de contato:",Nom)
                                                        print("Endereco:",Ende)
                                                        print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                                        print("Equipamento / Modelo:",eQp,"   Número de Série:",nSe)
                                                        print("Contrato:",cOntr,"\n")
                                                        ac_yn = str(input("Deseja atualizar os dados? (s/n)"))
                                                        if (ac_yn == "n") or (ac_yn == "N"):
                                                            print("Operação cancelada!"+"\n")
                                                            cc_Loop = True
                                                            pre_lop = False
                                                            pinky = False
                                                            Altera_Dados_Loop = False
                                                        if (ac_yn == "s") or (ac_yn == "S"):
                                                            Tup_Cliente = (Nome_Fantasia,Razao_Social,Tele,Nom,Ende,Cida,Estad,cEp,eQp,nSe,cOntr)
                                                            Data_Dic[Codcli] = Tup_Cliente
                                                            Log_Occur = loGOco(User_Current,6)
                                                            Log_List.append(Log_Occur)
                                                            print("Dados de Cliente atualizados com sucesso!"+"\n")
                                                            cc_Loop = True
                                                            pre_lop = False
                                                            pinky = False
                                                            ppyp = str(input("Deseja alterar mais algum dado? (s/n)"))
                                                            if (ppyp == "s") or (ppyp == "S"):
                                                                Altera_Dados_Loop = True
                                                            else:
                                                                Altera_Dados_Loop = False
                                                                cc_Loop = True
                                                                pre_lop = False
                                                                pinky = False
                                                else:
                                                    print("Cliente iválido!")
                                                    pinky = True
                                    if (Tem_Nos_Dados == 0):
                                        print ("Cliente inexistente na cidade escolhida!"+"\n")
                                        pre_lop = True
                    
                    #REMOVER CLIENTE
                    if (CC_oPtion == "rc"):
                        Loop_Death = True
                        while(Loop_Death == True):
                            print("***Remover Clientes***")
                            print("ESTA OPERAÇÃO REQUER ATENÇÃO!"+"\n")
                            Death_Toll = str(input("Deseja continuar? (s/n)"))
                            if (Death_Toll == "n") or (Death_Toll == "N"):
                                Loop_Death = False
                            if (Death_Toll == "s") or (Death_Toll == "S"):
                                print("\n"+"Escolha por:"+"\n")
                                print("1 - Código de cliente")
                                print("2 - Nome Fantasia")
                                print("3 - Cidade"+"\n")
                                opa = str (input("OPÇÃO>"))
                                if (opa == "1"):
                                    Death_Chosen = str(input("Digite o código de cliente:"))
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
                                        print("Código de cliente:",Codcli)
                                        print("Nome Fantasia:",Nome_Fantasia)
                                        print("Razão Social:",Razao_Social)
                                        print("Telefone:",Tele)
                                        print("Pessoa de contato:",Nom)
                                        print("Endereço:",Ende)
                                        print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                        print("Equipamento / Modelo:",eQp,"   Número de Série:",nSe)
                                        print("Contrato:",cOntr,"\n")
                                        Death_Angel = str(input("Deseja realmente excluir todos os dados do cliente? (s/n)"))
                                        if (Death_Angel == "n") or (Death_Angel == "N"):
                                            print("Operação cancelada!"+"\n")
                                            Loop_Death == False
                                            cc_Loop = True
                                        if (Death_Angel == "s") or (Death_Angel == "S"):
                                            del Data_Dic[Codcli]
                                            Log_Occur = loGOco(User_Current,4)
                                            Log_List.append(Log_Occur)
                                            print("Cliente removido com sucesso!"+"\n")
                                            cc_Loop = True
                                            Loop_Death = False
                                    else:
                                        Loop_Death == True
                                        print("Cliente inexistente!"+"\n")
                                if (opa == "2"):
                                    Fantasy = str(input("Digite o Nome Fantasia:"))
                                    Tem_Nos_Dados = 0
                                    Liscli = []
                                    for val in Data_Dic.items():
                                        vlw = val[1]
                                        if (Mai_Min(Fantasy,vlw[0]) == True):
                                            Liscli.append(val[0])
                                            Codcli = val[0]
                                            Nome_Fantasia = vlw[0]
                                            Razao_Social = vlw[1]
                                            Tele = vlw[2]
                                            Nom = vlw[3]
                                            Ende = vlw[4]
                                            Cida = vlw[5]
                                            Estad = vlw[6]
                                            cEp = vlw[7]
                                            eQp = vlw[8]
                                            nSe = vlw[9]
                                            cOntr = vlw[10]
                                            print("\n"+"Dados do cliente:"+"\n")
                                            print("Código de cliente:",Codcli)
                                            print("Nome Fantasia:",Nome_Fantasia)
                                            print("Razão Social:",Razao_Social)
                                            print("Telefone:",Tele)
                                            print("Pessoa de contato:",Nom)
                                            print("Endereço:",Ende)
                                            print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                            print("Equipamento / Modelo:",eQp,"   Número de Série:",nSe)
                                            print("Contrato:",cOntr,"\n")
                                            Tem_Nos_Dados += 1
                                    if (Tem_Nos_Dados > 0):
                                        Death_Angel = str(input("Deseja realmente excluir todos os dados do cliente? (s/n)"))
                                        if (Death_Angel == "n") or (Death_Angel == "N"):
                                            print("Operação cancelada!"+"\n")
                                            Loop_Death == False
                                            cc_Loop = True
                                        if (Death_Angel == "s") or (Death_Angel == "S"):
                                            pinky = True
                                            while (pinky == True):
                                                coddy = str(input("Digite o código de cliente que deseja remover:"))
                                                if (coddy == "sair"):
                                                    pinky = False
                                                    Loop_Death = False
                                                else:
                                                    if coddy in Liscli:
                                                        del Data_Dic[coddy]
                                                        Log_Occur = loGOco(User_Current,4)
                                                        Log_List.append(Log_Occur)
                                                        print("Cliente removido com sucesso!"+"\n")
                                                        cc_Loop = True
                                                        Loop_Death = False
                                                        pinky = False
                                                    else:
                                                        print("Cliente iválido!")
                                                        pinky = True

                                    if (Tem_Nos_Dados == 0):
                                        print ("Cliente com Nome Fantasia inexistente!"+"\n")
                                        Loop_Death = True

                                if (opa == "3"):
                                    CITY = str(input("Digite a Cidade:"))
                                    Tem_Nos_Dados = 0
                                    Liscli = []
                                    for val in Data_Dic.items():
                                        vlw = val[1]
                                        if (Mai_Min(CITY,vlw[5]) == True):
                                            Liscli.append(val[0])
                                            Codcli = val[0]
                                            Nome_Fantasia = vlw[0]
                                            Razao_Social = vlw[1]
                                            Tele = vlw[2]
                                            Nom = vlw[3]
                                            Ende = vlw[4]
                                            Cida = vlw[5]
                                            Estad = vlw[6]
                                            cEp = vlw[7]
                                            eQp = vlw[8]
                                            nSe = vlw[9]
                                            cOntr = vlw[10]
                                            print("\n"+"Dados do cliente:"+"\n")
                                            print("Código de cliente:",Codcli)
                                            print("Nome Fantasia:",Nome_Fantasia)
                                            print("Razão Social:",Razao_Social)
                                            print("Telefone:",Tele)
                                            print("Pessoa de contato:",Nom)
                                            print("Endereço:",Ende)
                                            print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                            print("Equipamento / Modelo:",eQp,"   Número de Série:",nSe)
                                            print("Contrato:",cOntr,"\n")
                                            Tem_Nos_Dados += 1
                                    if (Tem_Nos_Dados > 0):
                                        Death_Angel = str(input("Deseja realmente excluir todos os dados cliente? (s/n)"))
                                        if (Death_Angel == "n") or (Death_Angel == "N"):
                                            print("Operação cancelada!"+"\n")
                                            Loop_Death == False
                                            cc_Loop = True
                                        if (Death_Angel == "s") or (Death_Angel == "S"):
                                            pinky = True
                                            while (pinky == True):
                                                coddy = str(input("Digite o código de cliente que deseja remover:"))
                                                if (coddy == "sair"):
                                                    pinky = False
                                                    Loop_Death = False
                                                    cc_Loop = True
                                                else:
                                                    if coddy in Liscli:
                                                        del Data_Dic[coddy]
                                                        Log_Occur = loGOco(User_Current,4)
                                                        Log_List.append(Log_Occur)
                                                        print("Cliente removido com sucesso!"+"\n")
                                                        cc_Loop = True
                                                        Loop_Death = False
                                                        pinky = False
                                                    else:
                                                        print("Cliente iválido!")
                                                        pinky = True

                                    if (Tem_Nos_Dados == 0):
                                        print ("Cliente inexistente na cidade escolhida!"+"\n")
                                        Loop_Death = True                                      

                                
            #CONSULTA CLIENTE
            if (oPtion == "cl"):
                CL_Loop = True
                Lista_Consulta = []
                while (CL_Loop == True):
                    print("\n"+"***Consulta Clientes***"+"\n")
                    print("1 - Código de Cliente")
                    print("2 - Nome Fantasia")
                    print("3 - Cidade")
                    print("4 - Estado")
                    print("5 - Todos os clientes")
                    print("sair - SAIR"+"\n")
                    CL_oPtion = str(input("OPÇÃO>"))
                    if (CL_oPtion == "sair"):
                        CL_Loop = False
                        print("Operação cancelada!"+"\n")
                    else:
                        if (CL_oPtion == "1"):
                            Codcli_Entry = str(input("Digite o código de cliente:"))
                            for qw in Data_Dic.keys():
                                if (qw == Codcli_Entry):
                                    Toopy = Data_Dic[Codcli_Entry]
                                    Codcli = Codcli_Entry
                                    Nome_Fantasia = Toopy[0]
                                    Razao_Social = Toopy[1]
                                    Tele = Toopy[2]
                                    Nom = Toopy[3]
                                    Ende = Toopy[4]
                                    Cida = Toopy[5]
                                    Estad = Toopy[6]
                                    cEp = Toopy[7]
                                    eQp = Toopy[8]
                                    nSe = Toopy[9]
                                    cOntr = Toopy[10]
                                    print("\n"+"Dados do cliente:"+"\n")
                                    print("Código de cliente:",Codcli)
                                    print("Nome Fantasia:",Nome_Fantasia)
                                    print("Razão Social:",Razao_Social)
                                    print("Telefone:",Tele)
                                    print("Pessoa de contato:",Nom)
                                    print("Endereço:",Ende)
                                    print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                    print("Equipamento / Modelo:",eQp,"   Número de Série:",nSe)
                                    print("Contrato:",cOntr,"\n")
                                CL_Loop = True
                                Log_Occur = loGOco(User_Current,5)
                                Log_List.append(Log_Occur)
                            if (Codcli_Entry not in Data_Dic.keys()):
                                print ("Cliente inexistente!"+"\n")
                                CL_Loop = True
                        if (CL_oPtion == "2"):
                            Fantasy = str(input("Digite o Nome Fantasia:"))
                            Tem_Nos_Dados = 0
                            for val in Data_Dic.items():
                                vlw = val[1]
                                if (Mai_Min(Fantasy,vlw[0]) == True):
                                    Codcli = val[0]
                                    Nome_Fantasia = vlw[0]
                                    Razao_Social = vlw[1]
                                    Tele = vlw[2]
                                    Nom = vlw[3]
                                    Ende = vlw[4]
                                    Cida = vlw[5]
                                    Estad = vlw[6]
                                    cEp = vlw[7]
                                    eQp = vlw[8]
                                    nSe = vlw[9]
                                    cOntr = vlw[10]
                                    print("\n"+"Dados do cliente:"+"\n")
                                    print("Código de cliente:",Codcli)
                                    print("Nome Fantasia:",Nome_Fantasia)
                                    print("Razão Social:",Razao_Social)
                                    print("Telefone:",Tele)
                                    print("Pessoa de contato:",Nom)
                                    print("Endereço:",Ende)
                                    print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                    print("Equipamento / Modelo:",eQp,"   Número de Série:",nSe)
                                    print("Contrato:",cOntr,"\n")
                                    Tem_Nos_Dados += 1
                            if (Tem_Nos_Dados == 0):
                                print ("Cliente com Nome Fantasia inexistente!")
                                CL_Loop = True
                            else:
                                CL_Loop = True
                                Log_Occur = loGOco(User_Current,5)
                                Log_List.append(Log_Occur)

                        if (CL_oPtion == "3"):
                            CITY = str(input("Digite a Cidade:"))
                            Tem_Nos_Dados = 0
                            for val in Data_Dic.items():
                                vlw = val[1]
                                if (Mai_Min(CITY,vlw[5]) == True):
                                    Codcli = val[0]
                                    Nome_Fantasia = vlw[0]
                                    Razao_Social = vlw[1]
                                    Tele = vlw[2]
                                    Nom = vlw[3]
                                    Ende = vlw[4]
                                    Cida = vlw[5]
                                    Estad = vlw[6]
                                    cEp = vlw[7]
                                    eQp = vlw[8]
                                    nSe = vlw[9]
                                    cOntr = vlw[10]
                                    print("\n"+"Dados do cliente:"+"\n")
                                    print("Código de cliente:",Codcli)
                                    print("Nome Fantasia:",Nome_Fantasia)
                                    print("Razão Social:",Razao_Social)
                                    print("Telefone:",Tele)
                                    print("Pessoa de contato:",Nom)
                                    print("Endereço:",Ende)
                                    print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                    print("Equipamento / Modelo:",eQp,"   Número de Série:",nSe)
                                    print("Contrato:",cOntr,"\n")
                                    Tem_Nos_Dados += 1
                            if (Tem_Nos_Dados == 0):
                                print ("Cliente inexistente na cidade escolhida!")
                                CL_Loop = True
                            else:
                                CL_Loop = True
                                Log_Occur = loGOco(User_Current,5)
                                Log_List.append(Log_Occur)

                        if (CL_oPtion == "4"):
                            STATE = str(input("Digite o Estado:"))
                            Tem_Nos_Dados = 0
                            for val in Data_Dic.items():
                                vlw = val[1]
                                if (Mai_Min(STATE,vlw[6]) == True):
                                    Codcli = val[0]
                                    Nome_Fantasia = vlw[0]
                                    Razao_Social = vlw[1]
                                    Tele = vlw[2]
                                    Nom = vlw[3]
                                    Ende = vlw[4]
                                    Cida = vlw[5]
                                    Estad = vlw[6]
                                    cEp = vlw[7]
                                    eQp = vlw[8]
                                    nSe = vlw[9]
                                    cOntr = vlw[10]
                                    print("\n"+"Dados do cliente:"+"\n")
                                    print("Código de cliente:",Codcli)
                                    print("Nome Fantasia:",Nome_Fantasia)
                                    print("Razão Social:",Razao_Social)
                                    print("Telefone:",Tele)
                                    print("Pessoa de contato:",Nom)
                                    print("Endereço:",Ende)
                                    print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                    print("Equipamento / Modelo:",eQp,"   Número de Série:",nSe)
                                    print("Contrato:",cOntr,"\n")
                                    Tem_Nos_Dados += 1
                            if (Tem_Nos_Dados == 0):
                                print ("Cliente inexistente no Estado escolhido!")
                                CL_Loop = True
                            else:
                                CL_Loop = True
                                Log_Occur = loGOco(User_Current,5)
                                Log_List.append(Log_Occur)

                        if (CL_oPtion == "5"):
                            print("\n"+"Lista de clientes:"+"\n")
                            Codcli_List = []
                            Ordered_List = []
                            for num in Data_Dic.keys():
                                Codcli_List.append(int(num))
                            Codcli_List.sort()
                            for x in Codcli_List:
                                srr = str(x)
                                Ordered_List.append(srr)
                            for qw in Ordered_List:
                                Toopy = Data_Dic[qw]
                                Codcli = qw
                                Nome_Fantasia = Toopy[0]
                                Razao_Social = Toopy[1]
                                Tele = Toopy[2]
                                Nom = Toopy[3]
                                Ende = Toopy[4]
                                Cida = Toopy[5]
                                Estad = Toopy[6]
                                cEp = Toopy[7]
                                eQp = Toopy[8]
                                nSe = Toopy[9]
                                cOntr = Toopy[10]
                                print("Código de cliente:",Codcli)
                                print("Nome Fantasia:",Nome_Fantasia)
                                print("Razão Social:",Razao_Social)
                                print("Telefone:",Tele)
                                print("Pessoa de contato:",Nom)
                                print("Endereço:",Ende)
                                print("Cidade:",Cida,"   Estado:",Estad,"   CEP.:",cEp)
                                print("Equipamento / Modelo:",eQp,"   Número de Série:",nSe)
                                print("Contrato:",cOntr,"\n")
                                CL_Loop = True
                                Log_Occur = loGOco(User_Current,5)
                                Log_List.append(Log_Occur)

            #GERA ARQUIVO DE CLIENTES
            if (oPtion == "im") and (User_Power != 1):
                print ("\n"+"***Impressão de arquivo de clientes***"+"\n")
                lupito = True
                while (lupito == True):
                    yn_Imp = str(input("Deseja gerar arquivo da lista de clientes? (s/n):"))
                    if (yn_Imp == "n") or (yn_Imp == "N"):
                        print ("Operação cancelada!")
                        Menu_Loop = True
                        lupito = False
                    if (yn_Imp == "s") or (yn_Imp == "S"):
                        STR_FILE = ""
                        Codcli_List = []
                        Ordered_List = []
                        for num in Data_Dic.keys():
                            Codcli_List.append(int(num))
                        Codcli_List.sort()
                        for x in Codcli_List:
                            srr = str(x)
                            Ordered_List.append(srr)
                        for sst in Ordered_List:
                            Tup_FILE = Data_Dic[sst]
                            Codcli = sst
                            Nome_Fantasia = Tup_FILE[0]
                            Razao_Social = Tup_FILE[1]
                            Tele = Tup_FILE[2]
                            Nom = Tup_FILE[3]
                            Ende = Tup_FILE[4]
                            Cida = Tup_FILE[5]
                            Estad = Tup_FILE[6]
                            cEp = Tup_FILE[7]
                            eQp = Tup_FILE[8]
                            nSe = Tup_FILE[9]
                            cOntr = Tup_FILE[10]
                            STR_FILE += Dados_Cliente_Imp(Codcli,Nome_Fantasia,Razao_Social,Tele,Nom,Ende,Cida,Estad,cEp,eQp,nSe,cOntr)
                        ELEEXTSTR = ELEISSON(Data_Dic)
                        ELY = open("elementos.txt","w")
                        ELY.write(ELEEXTSTR)
                        ELY.close()
                        IMP = open("impressaoelementos.txt","w")
                        IMP.write(STR_FILE)
                        IMP.close()
                        Log_Occur = loGOco(User_Current,7)
                        Log_List.append(Log_Occur)
                        print("Arquivo gerado com sucesso!"+"\n")
                        Menu_Loop = True
                        lupito = False
                    if (yn_Imp != "s") and (yn_Imp != "S") and (yn_Imp != "n") and (yn_Imp != "N"):
                        lupito = True

            #CONSULTA LOG
            if (oPtion == "cg") and ((User_Power == 4) or (User_Power == 3)):
                loop_Log = True
                while (loop_Log == True):
                    print("***Consulta Log***"+"\n")
                    print("1 - Consultar por usuário")
                    print("2 - Consultar por data"+"\n")
                    oPlog = str(input("OPÇÃO>"))

                    if (oPlog == "1"):
                        loop_user_log = True
                        while (loop_user_log == True):
                            print("\n")
                            usrr = str(input("Digite o usuário:"))
                            if (usrr not in User_Dic):
                                loop_user_log = True
                                print ("Usuário inexistente!"+"\n")
                            if (usrr == "sair"):
                                loop_user_log = False
                                loop_Log = False
                                print ("Operação cancelada!"+"\n")
                            if (usrr in User_Dic):
                                print("\n")
                                ppw = (usrr+":")
                                for tt in Log_List:
                                    if (ppw == tt[0]):
                                        LogOPR(tt)
                                Log_Occur = loGOco(User_Current,71)
                                Log_List.append(Log_Occur)
                                loop_user_log = False
                                loop_Log = False
                    if (oPlog == "2"):
                        loop_Date_log = True
                        while (loop_Date_log == True):
                            print("\n"+"Favor não digitar o número '0' antes do Dia ou Mês."+"\n")
                            DAY = str(input("Digite o Dia:"))
                            if (DAY == "sair"):
                                print("Operação cancelada!"+"\n")
                                loop_Date_log = False
                                loop_Log = False
                            else:
                                MONTH = str(input("Digite o Mês:"))
                                YEAR = str(input("Digite o Ano:"))
                                DMY = DAY+MONTH+YEAR
                                dateok = 0
                                print("\n")
                                for data in Log_List:
                                    dmy = data[1]
                                    dmyexit = ""
                                    conct = 0
                                    for chrt in dmy:
                                        if (chrt != " ") and (chrt != "/") and (conct == 0):
                                            dmyexit += chrt
                                        if (chrt == " "):
                                            conct += 1
                                    if (DMY == dmyexit):
                                        LogOPR(data)
                                        dateok += 1
                                if (dateok == 0):
                                    print("Não há log nesta data!"+"\n")
                                    loop_Date_log = True
                                if (dateok > 0):
                                    Log_Occur = loGOco(User_Current,71)
                                    Log_List.append(Log_Occur)
                                    loop_Date_log = False
                                    loop_Log = False