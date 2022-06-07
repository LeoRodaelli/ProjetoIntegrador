def presentation():
    print("*" * 57)
    print("Bem Vindo ao programa do Calculo de Ingestão de Calorias!")
    print("*" * 57, '\n')
    print("Digite as informações a seguir: ")
    print('OBS: Substitua as vírgulas(,) por ponto(.) \n')


def user():
    digitouCerto = False
    while not digitouCerto:
        try:
            age = int(input('Insira sua idade: '))
            gener = input('Qual seu gênero: Masculino ou Feminino (digite M ou F): ').upper()
            weight = float(input('Insira seu peso(em Kg): '))
            height = float(input('Insira sua altura(em Metros): '))

            if age <= 0:
                print('Idade impossível! tente novamente! \n')

            else:
                digitouCerto = True

            if gener == 'M':
                n1 = 66.5
                p = 13.75 * weight
                at = 5.003 * height
                e = 6.77 * age
            elif gener == 'F':
                n1 = 655.1
                p = 9.56 * weight
                at = 1.85 * height
                e = 4.68 * age

        except ValueError:
            print("Ocorreu um erro, digite somente informações que foram pedidas!...")

    calculo_resultado = n1 + at + p - e
    return(int(calculo_resultado))

def CalAtv(calculo_resultado):
    FreqAtividade = input('Quantos dias da semana voce pratica atividades físicas? (1, 2, 3, 4, 5, 6, 7)?: ')

    if FreqAtividade == '1':
        FreqAtividade = (30 * calculo_resultado /100) + calculo_resultado

    elif FreqAtividade == '2':
        FreqAtividade = (50 * calculo_resultado /100) + calculo_resultado

    elif FreqAtividade == '3':
        FreqAtividade = (75 * calculo_resultado /100) + calculo_resultado

    elif FreqAtividade == '4' or '5' or '6' or '7':
        FreqAtividade = (100 * calculo_resultado /100) + calculo_resultado

    return(int(FreqAtividade))


def CalCaloria(atividade_nivel):

    result = input('Voce deseja perder peso? (digite perder): \n'
                   'Voce deseja manter peso? (digite manter): \n'
                   'Voce deseja ganhar peso? (digite ganhar): \n').lower()

    nome = input('Poxa, esqueci de perguntar, qual o seu nome mesmo? \n')

    if result == 'perder':
        kcal = atividade_nivel - 500

    elif result == 'manter':
        kcal = atividade_nivel

    elif result == 'ganhar':
        kcal = atividade_nivel + 500

    print(f'Olá {nome}, diante do desejado de {result} peso, as calorias diárias necessarias são {kcal}')


presentation()

CalCaloria(CalAtv(user()))


    #Anotation
    #Calculo-> mulher= 665.1 + (9.56 x p) + (1.85 x cm) – (4.7 x anos) + atividade
    #Calculo-> homem = 66.5 + (13.75 x p) + (5.003 x cm) - (6.77 x anos) + atividade
