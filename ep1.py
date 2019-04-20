# EP 2019-1: Escape Insper
#
# Alunos: 
# - Aluno A: Daniel Minson Pucciariello, danielp6@al.insper.edu.br
# - aluno B: Enrico Damiani, enricofd@al.insper.edu.br
# - Aluno C: Giulia Castro, giuliaac@al.insper.edu.br

#import json
import random

hp = 100

monstros = {
            "Pateta":{
                    "descricao": "Esse monstro possui o poder de te hipnotizar",
                    "vida":"50", 
                    "dano":"5",
                    "opcoes": {
                            "fugir":"tentar correr",
                            "enfrentar":"mostrar para ele quem é que manda"
                            }
                        },
            "Pluto":{
                    "descricao": "Esse monstro repete incessantemente que voce precisa prestar mais atenção na aula",
                    "vida":"35", 
                    "dano":"8",
                    "opcoes": {
                            "fugir":" tentar correr",
                            "enfrentar":"mostrar para ele quem é que manda"
                            }
                    }
            }
#return monstros

#def escolhadosmonstros(carregarmonstros):
#    x=random.randint(1, len(monstros[]))
#    monstros=monstro
 
#with open('Cenario.json', 'r', encoding="utf8") as f:
#    cenario=json.load(f)

    
def carregarmonstros():
    x = random.randint ( 0, len(monstros)-1)
    listademonstros = []
    for e in monstros:
        listademonstros.append(e)
    monstro = listademonstros[x]    
    return monstro

cenario = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "tomar o elevador para o andar do professor",
                "biblioteca": "ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "tomar o elevador para o saguao de entrada",
                "professor": "falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. \n O professor revelou que é um monstro disfarçado,\n e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "voltar para o saguao de entrada",
                "sala secreta": "entrar em uma passagem secreta que encontrou dentro do aquário 33"
            }
        },
        "sala secreta": {
            "titulo": "...",
            "descricao": "Para entrar na sala secreta, acerte a senha....",
            "opcoes": {
                "biblioteca": "voltar para a biblioteca"
            }
        }
    }
    
def carregar_cenarios():
    cenarios = cenario
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def combate():
    monstro = carregarmonstros()
    vidam = monstros[monstro]["vida"]
    vidap = hp
    danom = monstros[monstro]["dano"]
    print (7*"-")
    print ("Batalha")
    print (7*"-")
    print (f"Sua vide é de {hp} HP")
    print (30*"-")
    print (f"Você encontrou o {monstro}")
    print (monstros[monstro]["descricao"])
    print (f"Além disso conta com {vidam} HP e realiza ataques de {danom} de dano")
    escolhaf = monstros[monstro]["opcoes"]["fugir"]
    escolhae = monstros[monstro]["opcoes"]["enfrentar"]
    pergunta = input (f"Você quer {escolhaf} ou {escolhae} (responda com : fugir ou enfrentar): ")
    while pergunta != "fugir" and pergunta != "enfrentar":
        print ("responda corretamente")
        pergunta = input (f"Você quer {escolhaf} ou {escolhae} (responda com: fugir ou enfrentar): " )
    if pergunta == "fugir":
        a = random.randint(0,10)
        if a > 5:
            print (30*"-")
            print("Você não conseguiu fugir...")
            #------------------------------------------------------ arrumar:
            while vidam != 0 and vidap != 0:
                danopi = input("Você quer tentar um ataque fraco - Dano = 2 (75%), médio - Dano = 5 (50%), ou forte - Dano = 10 (25%)? (respoda com fraco, medio ou forte): ") 
                while danopi != "fraco" and danopi != "medio" and danopi != "médio" and danopi != "forte":
                    print ("responda corretamente")
                    danopi = input("Você quer tentar um ataque fraco - Dano = 2 (75%), médio - Dano = 5 (50%), ou forte - Dano = 10 (25%)? (respoda com fraco, medio ou forte): ") 
                if danopi == "fraco":
                    p = random.randint(0,100)
                    if p < 76:
                        danox = int(danom)
                        danox = danox - 2
                        print (f"A vida do monstro é {danom} HP")       
                        danopi = input("Você quer tentar um ataque fraco - Dano = 2 (75%), médio - Dano = 5 (50%), ou forte - Dano = 10 (25%)? (respoda com fraco, medio ou forte): ") 
                elif danopi == "medio" or danopi == "médio":
                    p = random.randint(0,100)
                    if p < 51:
                        danox = int(danom)
                        danox = danox - 5
                        print (f"A vida do monstro é {danom} HP")
                        danopi = input("Você quer tentar um ataque fraco - Dano = 2 (75%), médio - Dano = 5 (50%), ou forte - Dano = 10 (25%)? (respoda com fraco, medio ou forte): ")                            
                else:
                    p = random.randint(0,100)
                    if p < 26:
                        danox = int(danom)
                        danox = danox - 10
                        print (f"A vida do monstro é {danom} HP")
                        danopi = input("Você quer tentar um ataque fraco - Dano = 2 (75%), médio - Dano = 5 (50%), ou forte - Dano = 10 (25%)? (respoda com fraco, medio ou forte): ") 
        #---------------------------------------------------------------                    
        else:
            print (30*"-")
            print ("Você conseguiu fugir")
    else:
        danopi = input("Você quer tentar um ataque fraco - Dano = 2 (75%), médio - Dano = 5 (50%), ou forte - Dano = 10 (25%)? (respoda com fraco, medio ou forte): ") 
        while danopi != "fraco" and danopi != "medio" and danopi != "médio" and danopi != "forte":
                    print ("responda corretamente")
                    danopi = input("Você quer tentar um ataque fraco - Dano = 2 (75%), médio - Dano = 5 (50%), ou forte - Dano = 10 (25%)? (respoda com fraco, medio ou forte): ") 
                    if danopi == "fraco":
              #          p = random.randint(0,100)
              #          if p < 76:
                            danox = int(danom)
                            danox = danox - 2
                            print (f"A vida do monstro é {danom} HP")       
                            danopi = input("Você quer tentar um ataque fraco - Dano = 2 (75%), médio - Dano = 5 (50%), ou forte - Dano = 10 (25%)? (respoda com fraco, medio ou forte): ") 
                    elif danopi == "medio" or danopi == "médio":
                        p = random.randint(0,100)
                        if p < 51:
                            danox = int(danom)
                            danox = danox - 5
                            print (f"A vida do monstro é {danom} HP")
                            danopi = input("Você quer tentar um ataque fraco - Dano = 2 (75%), médio - Dano = 5 (50%), ou forte - Dano = 10 (25%)? (respoda com fraco, medio ou forte): ")                            
                    else:
                        p = random.randint(0,100)
                        if p < 26:
                            danox = int(danom)
                            danox = danox - 10
                            print (f"A vida do monstro é {danom} HP")
                            danopi = input("Você quer tentar um ataque fraco - Dano = 2 (75%), médio - Dano = 5 (50%), ou forte - Dano = 10 (25%)? (respoda com fraco, medio ou forte): ") 
# copiara o que esta entre ------ aqui
def main():
    nome_cenario_atual = "inicio"
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()
    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        print(cenario_atual["titulo"])
        print(len(cenario_atual["titulo"])*"-")
        print (f"Sua vida é de {hp} HP")
        print(20 * "-")
        print(cenario_atual["descricao"])
        print()
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            for e in opcoes:
                opcao = opcoes[e]
                print (f"Você pode {opcao} (para essa opção escreva: {e})")
            escolha = input ("O que você quer fazer? ")
            aparicaodemonstro = random.choice([True, False])
            ganharpremio = random.choice([True, False])
            acao = False
            if aparicaodemonstro == True or ganharpremio == True:
                acao = True
            while acao == True:   
                if aparicaodemonstro == True and ganharpremio == True:
                    print('começa  a batalha e sim, você ganhou um prêmio')
                    x= combate()
                    #vida do monstro - talvez fazer uma funcao para as batalhas
                    #premios - basicamente alterar hp do personagem, no inicio, mas depois queremos implementar
                    #adicionar itens no inventário, que ainda PRECISA SER FEITO.
                    # OBS: os premios que voce ganhar aqui, voce nao podera pegar no cenário
                    break
                elif aparicaodemonstro == True and ganharpremio == False:
                    x = combate()
                    break
                elif aparicaodemonstro == False and ganharpremio == True:
                    print('você ganhou um prêmio')
                    break
            if escolha in opcoes:
                if escolha == "sala secreta":
                    x = input ("Você quer tentar a senha da sala ou voltar para a biblioteca enquanto há tempo? (para tentar a senha digite: tentar a senha; para retornar para a biblioteca digite: biblioteca): ")
                    if x == "tentar a senha":
                        r = input("fala ai a senha meu filho: ")
                        t =  0
                        while r != "Disney" and t <10:
                           t = t+1
                           print (f"restam {10 - t} tentativas")
                           r = input("fala ai a senha meu filho: ")
                           if t==10:
                               break
                        if t==10:
                            game_over = True
                        else:
                            print("você ganhou o direito de se teletranportar, entretanto não erre o local....")
                            y = input ("Para onde você deseja ir? ")
                            if y not in cenarios:
                                print ("Aquele que não sabe para onde ir merece a morte")
                                game_over = True
                            else:
                                nome_cenario_atual = y
                    else:
                        print ("Você perdeu sua oportunidade...")
                        nome_cenario_atual = "biblioteca"
                else:
                    nome_cenario_atual = escolha
            else:
                #arrumar
                print("Sua indecisão foi sua ruína!")
                game_over = True
    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()