#Função para verificar se o usuário digitou um número
def func_numerico(msg):
    num = input(msg)
    while not num.isnumeric():
        print("Deve ser um número !")
        num = input(msg)
    num = int(num)
    return num

#Função para compara o input do usuário com as opções disponiveis
def compare_list(l1, msg):
    x = input(msg)
    while x not in l1:
        x = input(msg)
    return x



# Lista dos paises presentes no projeto:
paises = ['China', 'Indonésia', 'Estados Unidos']

# Login do usuário:
nome = input("Digite seu usuário: ")
senha = func_numerico("Digite sua senha(apenas números): ")
senhaCorreta = func_numerico("Repita sua senha(apenas números): ")
while senha != senhaCorreta:
    print("As senhas devem coincidir! Digite-as novamente.")
    senha = func_numerico("Digite sua senha(apenas números): ")
    senhaCorreta = func_numerico("Repita sua senha(apenas números): ")

# Inicio do código com um "bem vindo"
print(f"\nOlá {nome} seja bem vindo !\nSomos da BlueBacterium !!")
continuar = "s"


# Pergunta ao usuário sobre qual pais deseja ter as informações compartilhasdas.
while continuar == "s":
    print("\nEstes são os países que mais poluem os oceanos do mundo:")

    #Mostrando os paises ao usuário:
    for i in range(len(paises)):
        print(f"{paises[i]}")
    info = compare_list(paises, "\nDeseja obter informação de qual país ?")

    # Informações sobre a China:
    if info == 'China':
        print("A China é frequentemente apontada como um dos maiores contribuintes para a poluição marinha devido à"
                " sua grande população, atividade industrial e descargas de esgoto.")
        print("")

    #Informações sobre a Indonésia
    elif info == 'Indonésia':
        print("Com mais de 17.000 ilhas e uma população significativa, a Indonésia enfrenta desafios significativos"
                "de gestão de resíduos. O escoamento de resíduos plásticos dos rios\npara o oceano é um problema "
                "particularmente grave.")
        print("")

    #Informações sobre os Estados Unidos:
    else:
        print("Com uma grande população costeira e uma economia industrial desenvolvida, os Estados Unidos também "
                "contribuem significativamente para a poluição dos oceanos,\nespecialmente devido ao escoamento de "
                "produtos químicos agrícolas, resíduos industriais e plásticos.")
        print("")
    #Perguntando ao usuário se deseja continuar vendo as informações:
    continuar = compare_list(["s", "n"], "Deseja continuar? \n(responda com s/n)\n ->")

print("\nCom base nessas informações, nossa empresa consegue atuar melhor com as bactérias que são "
      "capazes de decompor os plásticos nos oceanos. E fazendo esta pesquisa, sabemos por onde começar !")
print("Obrigado pela visita!")

