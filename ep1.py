# EP 2019-1: Escape Insper
#
# Alunos: 
# - Aluno A: Daniel Minson Pucciariello, danielp6@al.insper.edu.br
# - aluno B: Enrico Damiani, enricofd@al.insper.edu.br
# - Aluno C: Giulia Castro, giuliaac@al.insper.edu.br
global hp
hp =100
import json
import random
global game_over
game_over = False

with open('monstros.json', 'r', encoding="utf8") as file:
    monstros=json.load(file)

with open('Cenario.json', 'r', encoding="utf8") as f:
    cenario=json.load(f)

def carregar_cenarios():
    cenarios = cenario
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual
    
def carregarmonstros():
    x = random.randint ( 0, len(monstros)-1)
    listademonstros = []
    for e in monstros:
        listademonstros.append(e)
    monstro = listademonstros[x]    
    return monstro
            
def combate():
    monstro = carregarmonstros()
    vidam = monstros[monstro]["vida"]
    global hp
    global game_over
    vidap = int(hp)
    saiudabatalha = False
    danom = monstros[monstro]["dano"]
    print (7*"-")
    print ("Batalha")
    print (7*"-")
    print (f"Sua vida é de {vidap} HP")
    print (30*"-")
    print (f"Você encontrou o {monstro}")
    print (monstros[monstro]["descricao"])
    print (f"Além disso conta com {vidam} HP e realiza ataques de {danom} de dano")
    escolhaf = monstros[monstro]["opcoes"]["fugir"]
    escolhae = monstros[monstro]["opcoes"]["enfrentar"]
    pergunta = input (f"Você quer {escolhaf} ou {escolhae} (responda com : fugir ou enfrentar): ")
    vidam = int(vidam)
    danom = int(danom)
    while pergunta != "fugir" and pergunta != "enfrentar":
        #impedir que o jogador dê uma resposta inválida
        print ("responda corretamente")
        pergunta = input (f"Você quer {escolhaf} ou {escolhae} (responda com: fugir ou enfrentar): " )
        
    if pergunta == "fugir":
        a = random.randint(0,10)
        #sistema randomico que determina se o jogador irá conseguir fugir ou nao
        if a > 5:
            print (30*"-")
            print("Você não conseguiu fugir...")

            while vidam > 0 and vidap > 0:
                danopi = input("Você quer tentar um ataque fraco - Dano = 2 (75%), médio - Dano = 5 (50%), ou forte - Dano = 10 (25%)? (respoda com fraco, medio ou forte): ") 
                while danopi != "fraco" and danopi != "medio" and danopi != "médio" and danopi != "forte":
                    print ("responda corretamente")
                    danopi = input("Você quer tentar um ataque fraco - Dano = 2 (75%), médio - Dano = 5 (50%), ou forte - Dano = 10 (25%)? (respoda com fraco, medio ou forte): ") 
                #sistema que determina se o dano que o jogador definiu realmente vai ser efetuado 
                
                #if com "p" e outro if com "y" para determinar se as ações serão realizadas
                if danopi == "fraco":
                    p = random.randint(0,100)
                    y = random.randint(0,100)
                    if p < 76:
                        vidam = vidam - 5
                        print (f"A vida do monstro agora é {vidam} HP")   
                        while vidam>0:
                            print ("Vez do monstro atacar")
                            if y < 51:
                                vidap = vidap - danom
                                print(f"o monstro tirou {danom} de dano")
                                print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                                print ("Sua vez")
                                danopi = ""
                            else:
                                print (" Para sua sorte o monstro errou o ataque...")
                                print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                                print ("Sua vez")
                                danopi = ""
                            break
                    else:
                        print("Nenhum dano foi dado no monstro, agora é a vez dele")
                        if y < 51:
                            vidap = vidap - danom
                            print(f"o monstro tirou {danom} de dano")
                            print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                            print ("Sua vez")
                            danopi = ""
                        else:
                            print (" Para sua sorte o monstro errou o ataque...")
                            print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                            print ("Sua vez")
                            danopi = ""    
                elif danopi == "medio" or danopi == "médio":
                    p = random.randint(0,100)
                    y = random.randint(0,100)
                    if p < 51:
                        vidam = vidam - 10
                        print (f"A vida do monstro agora é {vidam} HP")   
                        while vidam>0:
                            print ("Vez do monstro atacar")
                            if y < 51:
                                vidap = vidap - danom
                                print(f"o monstro tirou {danom} de dano")
                                print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                                print ("Sua vez")
                                danopi = ""
                            else:
                                print (" Para sua sorte o monstro errou o ataque...")
                                print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                                print ("Sua vez")
                                danopi = ""   
                            break
                    else:
                        print("Nenhum dano foi dado no monstro, agora é a vez dele")
                        print (f"A vida do monstro agora é {vidam} HP") 
                        if y < 51:
                            vidap = vidap - danom
                            print(f"o monstro tirou {danom} de dano")
                            print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                            print ("Sua vez")
                            danopi = ""
                        else:
                            print (" Para sua sorte o monstro errou o ataque...")
                            print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                            print ("Sua vez")
                            danopi = ""    

                elif danopi == "forte":
                    p = random.randint(0,100)
                    y = random.randint(0,100)
                    if p < 26:
                        vidam = vidam - 20
                        print (f"A vida do monstro agora é {vidam} HP")   
                        while vidam>0:
                            print ("Vez do monstro atacar")
                            if y < 51:
                                vidap = vidap - danom
                                print(f"o monstro tirou {danom} de dano")
                                print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                                print ("Sua vez")
                                danopi = ""
                            else:
                                print (" Para sua sorte o monstro errou o ataque...")
                                print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                                print ("Sua vez")
                                danopi = ""    
                            break
                    else:
                        print("Nenhum dano foi dado no monstro, agora é a vez dele")
                        print (f"A vida do monstro agora é {vidam} HP") 
                        if y < 51:
                            vidap = vidap - danom
                            print(f"o monstro tirou {danom} de dano")
                            print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                            print ("Sua vez")
                            danopi = ""
                        else:
                            print (" Para sua sorte o monstro errou o ataque...")
                            print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                            print ("Sua vez")
                            danopi = ""
            if vidam < 0:
                print("Você matou o monstro")
                saiudabatalha = True
                return saiudabatalha
            elif vidap <0:
                game_over=True
        else:        
            print (30*"-")
            print ("Você conseguiu fugir")
            saiudabatalha = True
            hp=vidap
            return saiudabatalha

    else:
        while vidam > 0 and vidap > 0:
            danopi = input("Você quer tentar um ataque fraco - Dano = 2 (75%), médio - Dano = 5 (50%), ou forte - Dano = 10 (25%)? (respoda com fraco, medio ou forte): ") 
            while danopi != "fraco" and danopi != "medio" and danopi != "médio" and danopi != "forte":
                print ("responda corretamente")
                danopi = input("Você quer tentar um ataque fraco - Dano = 5 (75%), médio - Dano = 10 (50%), ou forte - Dano = 20 (25%)? (respoda com fraco, medio ou forte): ") 
            if danopi == "fraco":
                p = random.randint(0,100)
                y = random.randint(0,100)
                if p < 76:
                   vidam = vidam - 5
                   print (f"A vida do monstro agora é {vidam} HP")   
                   while vidam>0:
                       print ("Vez do monstro atacar")
                       if y < 51:
                           vidap = vidap - danom
                           print(f"o monstro tirou {danom} de dano")
                           print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                           print ("Sua vez")
                           danopi = ""
                       else:
                           print (" Para sua sorte o monstro errou o ataque...")
                           print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                           print ("Sua vez")
                           danopi = ""    
                       break
                else:
                    print("Nenhum dano foi dado no monstro, agora é a vez dele")
                    print (f"A vida do monstro agora é {vidam} HP") 
                    if y < 51:
                        vidap = vidap - danom
                        print(f"o monstro tirou {danom} de dano")
                        print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                        print ("Sua vez")
                        danopi = ""
                    else:
                        print (" Para sua sorte o monstro errou o ataque...")
                        print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                        print ("Sua vez")
                        danopi = ""    
            elif danopi == "medio" or danopi == "médio":
                p = random.randint(0,100)
                y = random.randint(0,100)
                if p < 51:
                    vidam = vidam - 10
                    print (f"A vida do monstro agora é {vidam} HP")   
                    while vidam>0:
                        print ("Vez do monstro atacar")
                        if y < 51:
                            vidap = vidap - danom
                            print(f"o monstro tirou {danom} de dano")
                            print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                            print ("Sua vez")
                            danopi = ""
                        else:
                            print (" Para sua sorte o monstro errou o ataque...")
                            print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                            print ("Sua vez")
                            danopi = "" 
                        break
                else:
                    print("Nenhum dano foi dado no monstro, agora é a vez dele")
                    print (f"A vida do monstro agora é {vidam} HP") 
                    if y < 51:
                        vidap = vidap - danom
                        print(f"o monstro tirou {danom} de dano")
                        print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                        print ("Sua vez")
                        danopi = ""
                    else:
                        print (" Para sua sorte o monstro errou o ataque...")
                        print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                        print ("Sua vez")
                        danopi = ""
            elif danopi == "forte":
                p = random.randint(0,100)
                y = random.randint(0,100)
                if p < 26:
                    vidam = vidam - 20
                    print (f"A vida do monstro agora é {vidam} HP")   
                    while vidam>0:
                        print ("Vez do monstro atacar")
                        if y < 51:
                            vidap = vidap - danom
                            print(f"o monstro tirou {danom} de dano")
                            print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                            print ("Sua vez")
                            danopi = ""
                        else:
                            print (" Para sua sorte o monstro errou o ataque...")
                            print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                            print ("Sua vez")
                            danopi = ""
                        break
                else:
                    print("Nenhum dano foi dado no monstro, agora é a vez dele")
                    print (f"A vida do monstro agora é {vidam} HP") 
                    if y < 51:
                        vidap = vidap - danom
                        print(f"o monstro tirou {danom} de dano")
                        print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                        print ("Sua vez")
                        danopi = ""
                    else:
                        print (" Para sua sorte o monstro errou o ataque...")
                        print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
                        print ("Sua vez")
                        danopi =""            
                #---------------------------------------------------------------  
            hp=vidap
        if vidam < 0:
            print("Você matou o monstro")
            saiudabatalha = True
            return saiudabatalha
        elif vidap <0:
            game_over=True

def main():
    global hp
    global game_over
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
        global hp
        #dados que monstram a situação do jogo e do jogador.
        cenario_atual = cenarios[nome_cenario_atual]
        print(cenario_atual["titulo"])
        print(len(cenario_atual["titulo"])*"-")
        print (f"Sua vida é de {hp} HP")
        print(20 * "-")
        print(cenario_atual["descricao"])
        print()
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("você morrrreeeuuu")
            game_over = True
        else:
            #escolha do cenario
            for e in opcoes:
                opcao = opcoes[e]
                print (f"Você pode {opcao} (para essa opção escreva: {e})")
            escolha = input ("O que você quer fazer? ")
            #definição se os monstros e/ou premios irão existir em determinado momento.
            a = random.randint(0,100)
            b = random.randint(0,100)
            aparicaodemonstro = False
            ganharpremio = False
            if a < 26:
                aparicaodemonstro = True
            if b < 26:
                ganharpremio = True
            acao = False
            saiudabatalha = combate()
            if aparicaodemonstro == True or ganharpremio == True:
                acao = True
            
            while acao == True:   
                if aparicaodemonstro == True and ganharpremio == True and saiudabatalha==False:
                    print("20 hps pra voce")
                    hp = hp+20
                    print('Você encontrou um monstro!')
                    x= combate()
                
                    if hp <0:
                         game_over = True
                    break
                elif aparicaodemonstro == True and ganharpremio == False and saiudabatalha==False:
                    print("Você encontrou um monstro")
                    x= combate()
                
                    if hp <0:
                        game_over = True
                    break
                elif aparicaodemonstro == False and ganharpremio == True:
                    print("20 hps pra voce")
                
                    hp=hp +20 
                    break
                else:
                    break
            if escolha in opcoes:
                #se o jogador escolher ir para a sala secreta, ele precisa acertar a senha (Disney)
                #com menos de 10 tentativas para poder ir para qualquer uma das salas do jogo.
                saiudabatalha = False
                if escolha == "sala secreta":
                    x = input ("Você quer tentar a senha da sala ou voltar para a biblioteca enquanto há tempo?\n(para tentar a senha digite: 'tentar a senha' e 'biblioteca' para retornar para a biblioteca): ")
                    if x == "tentar a senha":
                        r = input("fala ai a senha meu filho (dica: lugar onde algum de nossos personagens habitam): ")
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
                game_over = True
    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()