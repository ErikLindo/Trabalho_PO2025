from models import Usuario, Tema

opcao = True
while(opcao !=4):
    print("-------Menu--------")
    print("1 -Usuarios")
    print("2- Temas")
    print("3- Artes")
    print("4- Sair")
    opcao = int(input("Opção desejada: "))

    if(opcao == 1):
        print(".1 cadastro")
        print("2 - Listar")
        print("3- Editar")
        print("4 - Excluir")
        opcao = int(input("Opção desejada: "))

        if(opcao == 1):
            # Cadastrar o Usuario
            print("Cadastrando um usuario...")
            nome_completo = input("Nome: ")
            ra = input("Email: ")
            se = input("Senha: ")
            est1 = Usuario.create(nome=nome_completo, email=ra, senha=se)
    
        elif(opcao == 2):
            #Listar
            lista=Usuario.select()
            if(len(lista) > 0):
                for u in lista:
                    print(u)
            else:
                print("Nenhum usuario")

        elif(opcao == 3):
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

        elif(opcao == 4): 
            #Excluir
            opcao = int(input("Informe o id do usuario"))
            usu = Usuario.get_or_none(Usuario.id == opcao)

            if(usu):
                print("Nome atual:", usu.nome)
                print("Email atual:", usu.email)
                sn = int(input("Digita 1 para deletar ou 2 para não deletar"))

                if(sn == 1):
                    usu.delete_instance()
                

            else:
                print("Não existe")
            pass