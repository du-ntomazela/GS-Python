def func_numerico(msg):
    num = input(msg)
    while not num.isnumeric():
        print("Deve ser um número !")
        num = input(msg)
    num = int(num)
    return num


def func_continuar(msg):
    continuar = input(msg)
    while continuar != 's' and continuar != 'n':
        print("Apenas s/n!")
        continuar = input(msg)
    return continuar


paises = ['China', 'Indonésia', 'Estados Unidos']

nome = input("Digite seu nome: ")
senha = func_numerico("Digite sua senha: ")
senhaCorreta = func_numerico("Repita sua senha: ")
while senha != senhaCorreta:
    senha = func_numerico("Digite sua senha: ")
    senhaCorreta = func_numerico("Repita sua senha: ")
print(f"\nOlá {nome} seja bem vindo !\nSomos da BlueBacter !!")
continuar = func_continuar("\nDeseja continuar ?")
if continuar == 'n':
    print("Obrigado pela visita!")
else:
    while True:
        print("\nEstes são os países que mais poluem os oceanos do mundo:")
        for i in range(len(paises)):
            print(f"{paises[i]}")
        info = input("\nDeseja obter informação de qual país ?")
        while info not in paises:
            print("Apenas os países da lista!")
            info = input("Deseja obter informação de qual país ?")
        if info == 'China':
            print("A China é frequentemente apontada como um dos maiores contribuintes para a poluição marinha devido à"
                  "sua grande população, atividade industrial e descargas de esgoto.")
        elif info == 'Indonésia':
            print("Com mais de 17.000 ilhas e uma população significativa, a Indonésia enfrenta desafios significativos"
                  "de gestão de resíduos. O escoamento de resíduos plásticos dos rios\npara o oceano é um problema "
                  "particularmente grave.")
        else:
            print("Com uma grande população costeira e uma economia industrial desenvolvida, os Estados Unidos também "
                  "contribuem significativamente para a poluição dos oceanos,\nespecialmente devido ao escoamento de "
                  "produtos químicos agrícolas, resíduos industriais e plásticos.")
        continuar = func_continuar("\nDeseja continuar vendo as notícias ?")
        if continuar == 'n':
            print("\nCom base nessas informações, nossa empresa consegue atuar melhor com as bactérias que são "
                  "capazes de decompor os plásticos nos oceanos. E fazendo está pesquisa, sabemos por onde começar !")
            break
