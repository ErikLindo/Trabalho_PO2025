from models import Usuario, Tema

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
            opcao = int(input("Informe o id do usuario"))
            usu = Usuario.get_or_none(Usuario.id == opcao)
            
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
            codigo = int(input("Informe o id do usuario"))
            usu = Usuario.get_or_none(Usuario.id == codigo)

            if(usu):
                print("Nome atual:", usu.nome)
                print("Email atual:", usu.email)
                sn = int(input("Digita 1 para deletar ou 2 para não deletar"))

                if(sn == 1):
                    usu.delete_instance()
                

            else:
                print("Não existe")
            pass

    elif(opcao == 2):

        print("1- Cadastrar um tema: ")
        print("2- Mostrar temas já cadastrados ")
        print("3- Editar a lista de temas")
        print("4- Excluir tema")
