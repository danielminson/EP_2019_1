# EP 2019-1: Escape Insper
#
# Alunos: 
# - Aluno A: Daniel Minson Pucciariello, danielp6@al.insper.edu.br
# - aluno B: Enrico Damiani, enricofd@al.insper.edu.br
# - Aluno C: Giulia Castro, giuliaac@al.insper.edu.br


import random
import json
hp = 100
 
with open('Monstros.json', 'r', encoding="utf8") as file:
    monstros=json.load(file)
def carregarmonstros():
    x = random.randint ( 0, len(monstros)-1)
    listademonstros = []
    for e in monstros:
        listademonstros.append(e)
    monstro = listademonstros[x]    
    return listademonstros, x, monstro
print (carregarmonstros()) 
with open('Cenario.json', 'r', encoding="utf8") as f:
    cenario=json.load(f)
    
def carregar_cenarios():
    cenarios = cenario
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def combate():
    monstro = carregarmonstros()
    vidam = monstros[monstro]["vida"]
    vidap = hp
    danom = monstros[monstro]["dano"]
    print ("Batalha")
    print (f "No caminho você se deparou com o {monstro}")
    print (f "Esse monstro possui {vidam} e realiza um ataque de {danom} de dano")
    print (f "Você pode {monstros[monstro]["opcoes"]["fugir]} ou {monstros[monstro]["opcoes"]["enfrentar"]} (para tentar correr, digite: fugir; para batalhar, digite: enfrentar)")
    danopi = input("Você quer tentar um ataque fraco - Dano = 2 (75%), médio - Dano = 5 (50%), ou forte - Dano = 10 (25%)? (respoda com a força do ataque): ") 



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