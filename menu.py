from models import Usuario, Tema, Arte

opcao = True
while(opcao !=4):
    print(" Seja bem vindo a ")
    print("-------Menu--------")
    print("1 - Cadastrar-se no sistema")
    print("2- Temas")
    print("3- Selecionar artes")
    print("4- Sair")
    opcao = int(input("Digite a opção desejada: "))

    if(opcao == 1):
        print(".1 cadastrar um cliente")
        print("2 - Listar cadastros")
        print("3- Editar dados")
        print("4 - Excluir dados do usuario")
        opcao_1 = int(input("Selecione a opção desejada: "))

        if(opcao_1 == 1):
            # Cadastrar o Usuario
            print("Realizando o cadastro do usuario...")
            nome_completo = input("Digite seu Nome: ")
            ra = input(" Informe o Email: ")
            se = input(" Insira a Senha: ")
            est1 = Usuario.create(nome=nome_completo, email=ra, senha=se)
    
        elif(opcao_1 == 2):
            #Listar
            lista=Usuario.select()
            if(len(lista) > 0):
                for u in lista:
                    print(u)
            else:
                print("Nenhum usuario cadastrado ainda")

        elif(opcao_1 == 3):
            #Editar
            codigo = int(input("Informe o id do usuario: "))
            usu = Usuario.get_or_none(Usuario.id == codigo)
            cont = 0
            while(cont != 1):
                print("Nome atual:", usu.nome)
                print("Email atual:", usu.email)
                print("Senha atual:", usu.senha)
                cont = int (input("Esse usuario que você quer?(Digita 1 para confimar ou deixe vazio para não confimar): "))
            if(usu):    
                
                print("Nome atual:", usu.nome)
                nome_completo = input("Deixe vazio ou informe o novo nome: ")
                if(nome_completo != ""):
                    usu.nome = nome_completo
                
                print("Email atual:", usu.email)
                ra = input("Deixe vazio ou informe o novo email: ")
                if(ra != ""):
                    usu.email = ra
                
                print("Senha atual:", usu.senha)
                se = input("Deixe vazio ou informe o novo senha: ")
                if(ra != ""):
                    usu.senha = se
                
                usu.save()

            else:
                print("Não existe")

        elif(opcao_1 == 4): 
            #Excluir
            codigo = int(input("Informe o id do usuario: "))
            usu = Usuario.get_or_none(Usuario.id == codigo)

            if(usu):
                print("Nome atual:", usu.nome)
                print("Email atual:", usu.email)
                sn = int(input("Digita 1 para deletar ou 2 para não deletar:"))

                if(sn == 1):
                    usu.delete_instance()
                

            else:
                print("Não existe")
            pass

    elif(opcao == 2):

        print("1- Cadastrar um tema")
        print("2- Mostrar temas já cadastrados")
        print("3- Editar a lista de temas")
        print("4- Excluir tema")
        opcao_2 = int(input("Selecione a opção desejada: "))

        if(opcao_2 == 1):
            # Cadastrar o Tema
            print("Realizando o cadastro do tema...")
            nome_completo = input("Digite seu tema: ")
            est2 = Tema.create(nome=nome_completo)
    
        elif(opcao_2 == 2):
            #Listar
            lista=Tema.select()
            if(len(lista) > 0):
                for u in lista:
                    print(u)
            else:
                print("Nenhum tema cadastrado ainda")

        elif(opcao_2 == 3):
            #Editar
            codigo = int(input("Informe o id do tema: "))
            usu = Tema.get_or_none(Tema.id == codigo)
            
            if(usu):    
                
                print("Nome do tema atual: ", usu.nome)
                nome_completo = input("Deixe vazio ou informe o novo tema: ")
                if(nome_completo != ""):
                    usu.nome = nome_completo
                
                usu.save()

            else:
                print("Não existe")

        elif(opcao_2 == 4): 
            #Excluir
            codigo = int(input("Informe o id do tema: "))
            usu = Tema.get_or_none(Tema.id == codigo)

            if(usu):
                print("Nome do tema atual: ", usu.nome)
                sn = int(input("Digita 1 para deletar ou 2 para não deletar: "))

                if(sn == 1):
                    usu.delete_instance()

            else:
                print("Não existe")
            pass

    elif(opcao == 3):
        print("1- Cadastrar o artista")
        print("2- Mostrar arte já cadastrados")
        print("3- Editar a descrição de arte")
        print("4- Excluir a descrição")
        opcao_3 = int(input("Selecione a opção desejada: "))

        if(opcao_3==1):
            #usuario
            cont=0
            while(cont != 1):
                codi = int(input("Informe o id do usuario: "))
                us = Usuario.get_or_none(Usuario.id == codi)
                
                if(us):
                    print("Nome atual:", us.nome)
                    print("Email atual:", us.email)
                    cont = int (input("Esse usuario que você quer?(Digita 1 para confimar ou 2 para não): "))
                else:
                    print("Usuário não encontrado...")
                

            #tema
            cont2=0
            while(cont2 != 1):
                codi2 = int(input("Informe o id do tema: "))
                us2 = Tema.get_or_none(Tema.id == codi2)
                
                if(us2):
                    print("Nome do tema: ", us2.nome)
                    cont2 = int (input("Esse tema que você quer?(Digita 1 para confimar ou 2 para não): "))
                else:
                    print("Tema não encontrado..")

                         
            descricao = input("Digita a descrição da arte: ")

            arte = Arte.create(artista = us, tipo= us2, descricao= descricao)
        
        elif(opcao_3 == 2):

            lista= Arte.select()
            if(len(lista) > 0):
                for u in lista:
                    print(u)
            else:
                print("Nenhuma artista cadastrada ainda")

        elif(opcao_3 == 3):
            #Editar
            codigo = int(input("Informe o id da arte relacionada ao usuario: "))
            arte = Arte.get_or_none(Arte.id == codigo)

            if(arte):    
                
                print("Descrição do artista: ", arte.descricao)
                d_completo = input("Deixe vazio ou informe a nova descrição: ")
                if(d_completo != ""):
                    arte.descricao= d_completo
                

                arte.save()

            else:
                print("Não existe")

        elif(opcao_3 == 4): 
            #Excluir
            codigo = int(input("Informe o id da arte: "))
            arte = Arte.get_or_none(Arte.id == codigo)

            if(arte):
                print("Nome da arte desejada: ", arte.descricao)
                sn = int(input("Digita 1 para deletar ou 2 para não deletar: "))

                if(sn == 1):
                    arte.delete_instance()

            else:
                print("Não existe")
            pass        