#importa bibliotecas para limpar tela e para contagem de tempo
import os, time

#Comando para limpar tela
os.system('cls')

#Como na primeira vez em que o programa é rodado ainda não temos ninguém cadastrado, 
#As variaveis 'usuario_cadastrado' e 'senha_cadastrada' iniciam vazias
usuario_cadastrado = ''
senha_cadastrada = ''

#Para que não tenha o problema de adivinhação de senha, será iniciado um contador para limitar as tentativas
tentativas = 0

#Para iniciar o programa em loop
i = 0
#valor iniciodo é 0
ganhos = 0
perdas = 0
valor_total = 0
metaMes = 0
metaAno = 0
#O programa é iniciado dentro de uma estrutura de repetição, 

while i == 0:


    #Começo
    print('----Controle de Finanças Pessoais / C.F.P.----')

    #Opções do usuário
    print('Digite: \n(1) Para Entrar \n(2) Para Cadastrar Usuário \n(3) Para Sair\n ')

    #Vai validar a opção do usuário
    opcao = int(input('Opção: '))

    #Utilizando match para executar uma ação de acordo com a escolha do usuário
    match opcao:

        #Se escolha for 1. Entrar 
        case 1:
            #Informar usuário que ele está fazendo um login
            print('Digite usuário e senha para ter acesso as suas informações')
            #Inputação dos dados
            usuario = input('Usuário: ')
            senha = int(input('Senha: '))

            #Validação de Usuário e Senha

            #Se o usúario inputado pelo usuário bater com um usuário já cadastrado, o usuário entra para usuario_valido
            usuario_valido = (usuario_cadastrado == usuario)
            #Se a senha inputada pelo usuário bater com a senha já cadastrada, vinculada com o usuário, a senha entra para senha_valida
            senha_valida = (senha_cadastrada == senha)

            #Para senha usuario não valido OU senha não valida, o programa volta para opções do usuário 
            if  (not usuario_valido) or (not senha_valida):

                #Pausa de 2 segundos
                time.sleep(1)
                #Limpa a tela
                os.system('cls')

                #Volta pro match case
                print('Usuário ou senha invalidos, tente novamente!')

                #Soma 1 a tentativas
                tentativas += 1

                #Quando tentativas chega a 3 o programa finaliza 
                if tentativas == 3:
                    #Encerra programa por excesso de tentativas
                    print('Limite de tentativas excedido! Encerrando o programa...')
                    #Pausa de 2 segundos
                    time.sleep(1)
                    #Limpa a tela
                    os.system('cls')
                    #Sai do script
                    break

                #Pausa de 2 segundos
                time.sleep(1)
                #Limpa a tela
                os.system('cls')

            #Para senha usuario valido E senha valida, o programa 'Controle de Finanças Pessoais', ou 'C.F.P.' é iniciado
            elif  usuario_valido and senha_valida:
                #Pausa de 2 segundos
                time.sleep(1)
                #Limpa a tela
                os.system('cls')


                def extrato():
                    print('---------------------Inicio do Programa--------------------------')
                    # Valor inicial da conta
                     #Deixar global para quando sair do while ficar salvo
                    global valor_total
                    global perdas
                    global ganhos
                    
                    while True:
                        # Começo
                        print('Controle de Finanças Pessoais / C.F.P.')

                        # Opções do usuário
                        print('Digite: \n(1) Ver Extrato \n(2) Adicionar ganhos e perdas \n(3) Metas do usuario \n(4) Para Tela Inicial\n')

                        # Valida a opção do usuário
                        number = int(input('Opção: '))

                        if number == 1:
                            print(f"Ganhos: R$ {ganhos}")
                            print(f"Perdas: R$ {perdas}\n")
                            print(f"Valor total na conta: R$ {valor_total}\n")

                        elif number == 2:
                            print("\nDigites os valores use ( . ou , )\n")
                            ganhos = float(input("Digite o valor dos ganhos do mês: ").replace(',', '.'))
                            perdas = float(input("Digite o valor das perdas do mês: ").replace(',', '.'))

                            # Calcula o extrato
                            valor_total += ganhos - perdas
                            print("Extrato do mês:")
                            print(f"Ganhos: R$ {ganhos}")
                            print(f"Perdas: R$ {perdas}")
                            print(f"Valor total na conta: R$ {valor_total}")
                        
                        elif number == 3:
                            def meta():
                                #Deixar global para quando sair do while ficar salvo
                                global metaAno
                                global metaMes

                                while True:
                                    print('\nDigite: \n(1) Ver Meta \n(2) Adicionar Meta\n(3) Voltar')
                                    number = int(input('Opção: '))

                                    if number == 1:
                                        print(f"Meta para a conta:\nMês: R$ {metaMes},\nAno: R$ {metaAno}")
                                        print(f"Valor na conta: R$ {valor_total}\n")
                                        resultadoMes = valor_total - metaMes
                                        resultadoAno = valor_total - metaAno
                                        print(f"Diferença do valor para a meta:\nMês: R$ {resultadoMes},\nAno: R$ {resultadoAno}")
                                        
                                    elif number == 2:
                                        print("\nDigite os valores (use ponto ou vírgula para casas decimais)\n")
                                        metaMes = float(input("Digite a meta do mês: ").replace(',', '.'))
                                        metaAno = float(input("Digite a meta do ano: ").replace(',', '.'))

                                        print("---- Metas ----")
                                        print(f"Meta para a conta:\nMês: R$ {metaMes},\nAno: R$ {metaAno}\n")

                                    elif number == 3:
                                        break

                            meta()
                        elif number == 4:
                            time.sleep(1)
                            # Limpa a tela
                            os.system('cls')
                            break

                        # Opções do usuário
                        print('\nDigite: (0) Para Voltar\n')
                        voltar = int(input('Opção: '))

                        if voltar == 0:
                            time.sleep(1)
                            # Limpa a tela
                            os.system('cls')
                        else:
                            #Alerta o usuário de que escolheu uma opção inexistente 
                            print('Opção inválida!')
                            #Pausa de 2 segundos
                            time.sleep(1)
                            #Limpa a tela
                            os.system('cls')

                extrato()

         #Se escolha for 2. Cadastrar Usuário 
        case 2:
            #Informar usuário que ele está fazendo um cadastro de usuário
            print('Faça o cadastro para ter acesso ao programa!')
            #Inputação dos dados
            usuario = input('Crie um Usuário: ')
            senha = int(input('Crie uma Senha (Só números):'))

            #Salvar os dados cadastrados em variaveis, para validar a opção 1. Entrar
            usuario_cadastrado = usuario
            senha_cadastrada = senha

            #Pausa de 2 segundos
            time.sleep(1)
            #Limpa a tela
            os.system('cls')

        #Se escolha for 3. Sair 
        case 3:
            #Pausa de 2 segundos
            time.sleep(1)
            #Limpa a tela
            os.system('cls')
            #Sai do script
            break

        #Um case que abrange caracteres quaisquer, diferentes dos três especificados
        case _:
            #Alerta o usuário de que escolheu uma opção inexistente 
            print('Opção inválida!')
            #Pausa de 2 segundos
            time.sleep(1)
            #Limpa a tela
            os.system('cls')