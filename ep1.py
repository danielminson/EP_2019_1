# EP 2019-1: Escape Insper
#
# Alunos: 
# - Aluno A: Daniel Minson Pucciariello, danielp6@al.insper.edu.br
# - aluno B: Enrico Damiani, enricofd@al.insper.edu.br
# - Aluno C: Giulia Castro, giuliaac@al.insper.edu.br
hp =100
import json
import random

with open('monstros.json', 'r', encoding="utf8") as file:
    monstros=json.load(file)


#def escolhadosmonstros(carregarmonstros):
#    x=random.randint(1, len(monstros[]))
#    monstros=monstro
 
with open('Cenario.json', 'r', encoding="utf8") as f:
    cenario=json.load(f)

def carregar_cenarios():
    cenarios = cenario
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual
    
def carregarmonstros():
    x = random.randint (0, len(monstros)-1)
    listademonstros = []
    for e in monstros:
        listademonstros.append(e)
    monstro = listademonstros[x]    
    return monstro

descricao_inventario= {
            'sorvete do mickey':{
                    'descricao':"Coma esse item para aumentar seu hp em 20",
                    'hp':20, 
                    'utilizar':"Seu hp aumentará 20 pontos"
                        },
            'turkey leg':{
                    'descricao':"Coma esse item para aumentar seu hp em 50 pontos",
                    'hp':50,
                    'utilizar':"Seu hp aumentará 50 pontos", 
                    },
            'pipoca':{
                    'descricao':"Coma esse item para aumentar seu hp em 30 pontos",
                    'hp':30,
                    'utilizar':"Seu hp aumentará 50 pontos", 
            'chave secreta':{
                    'descricao':"A palavra secreta é Disney! Utilize-a para ter acesso à sala secreta"
                    }
            }
        }
            
def luta(y, vidap, danom):
    if y < 51:
        vidap = vidap - danom
        print(f"o montro tirou {danom} de dano")
        print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
        print ("Sua vez")
        danopi = input("Você quer tentar um ataque fraco - Dano = 5 (75%), médio - Dano = 10 (50%), ou forte - Dano = 20 (25%)? (respoda com fraco, medio ou forte): ") 
    else:
        print (" Para sua sorte o monstro errou o ataque...")
        print(f"Depois do ataque do monstro sua vida é de {vidap} HP")
        print ("Sua vez")
        danopi = input("Você quer tentar um ataque fraco - Dano = 5 (75%), médio - Dano = 10 (50%), ou forte - Dano = 20 (25%)? (respoda com fraco, medio ou forte): ")            
            
def combate():
    monstro = carregarmonstros()
    vidam = monstros[monstro]["vida"]
    vidap = int(hp)
    danom = monstros[monstro]["dano"]
    print (7*"-")
    print ("Batalha")
    print (7*"-")
    print (f"Sua vida é de {hp} HP")
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
            #------------------------------------------------------ arrumar:
            while vidam > 0 and vidap > 0:
                danopi = input("Você quer tentar um ataque fraco - Dano = 2 (75%), médio - Dano = 5 (50%), ou forte - Dano = 10 (25%)? (respoda com fraco, medio ou forte): ") 
                while danopi != "fraco" and danopi != "medio" and danopi != "médio" and danopi != "forte":
                    print ("responda corretamente")
                    danopi = input("Você quer tentar um ataque fraco - Dano = 2 (75%), médio - Dano = 5 (50%), ou forte - Dano = 10 (25%)? (respoda com fraco, medio ou forte): ") 
                #sistema que determina se o dano que o jogador definiu realmente vai ser efetuado
                
                if danopi == "fraco":
                    p = random.randint(0,100)
                    y = random.randint(0,100)
                    if p < 76:
                        vidam = vidam - 5
                        print (f"A vida do monstro agora é {vidam} HP")       
                        print ("Vez do monstro atacar")
                        luta(y, vidap, danom)
                    else:
                        print("Nenhum dano foi dado no monstro, agora é a vez dele")
                        luta(y, vidap, danom)
                elif danopi == "medio" or danopi == "médio":
                    p = random.randint(0,100)
                    y = random.randint(0,100)
                    if p < 51:
                        vidam = vidam - 10
                        print (f"A vida do monstro agora é {vidam} HP")       
                        print ("Vez do monstro atacar")
                        luta(y, vidap, danom)
                    else:
                        print("Nenhum dano foi dado no monstro, agora é a vez dele")
                        print (f"A vida do monstro agora é {vidam} HP") 
                        luta(y, vidap, danom)
                elif danopi == "forte":
                    p = random.randint(0,100)
                    y = random.randint(0,100)
                    if p < 26:
                        vidam = vidam - 20
                        print (f"A vida do monstro agora é {vidam} HP")       
                        print ("Vez do monstro atacar")
                        luta(y, vidap, danom)
                    else:
                        print("Nenhum dano foi dado no monstro, agora é a vez dele")
                        print (f"A vida do monstro agora é {vidam} HP") 
                        luta(y, vidap, danom)
        print (30*"-")
        print ("Você conseguiu fugir")
        
    else:
        while vidam > 0 and vidap > 0:
            danopi = input("Você quer tentar um ataque fraco - Dano = 5 (75%), médio - Dano = 10 (50%), ou forte - Dano = 20 (25%)? (respoda com fraco, medio ou forte): ") 
            while danopi != "fraco" and danopi != "medio" and danopi != "médio" and danopi != "forte":
                print ("responda corretamente")
                danopi = input("Você quer tentar um ataque fraco - Dano = 5 (75%), médio - Dano = 10 (50%), ou forte - Dano = 20 (25%)? (respoda com fraco, medio ou forte): ") 
            if danopi == "fraco":
                p = random.randint(0,100)
                y = random.randint(0,100)
                if p < 76:
                    vidam = vidam - 5
                    print (f"A vida do monstro agora é {vidam} HP")       
                    print ("Vez do monstro atacar")
                    luta(y, vidap, danom)
                else:
                    print("Nenhum dano foi dado no monstro, agora é a vez dele")
                    print (f"A vida do monstro agora é {vidam} HP") 
                    luta(y, vidap, danom)
            elif danopi == "medio" or danopi == "médio":
                p = random.randint(0,100)
                y = random.randint(0,100)
                if p < 51:
                    vidam = vidam - 10
                    print (f"A vida do monstro agora é {vidam} HP")       
                    print ("Vez do monstro atacar")
                    luta(y, vidap, danom)
                else:
                    print("Nenhum dano foi dado no monstro, agora é a vez dele")
                    print (f"A vida do monstro agora é {vidam} HP") 
                    luta(y, vidap, danom)
            elif danopi == "forte":
                p = random.randint(0,100)
                y = random.randint(0,100)
                if p < 26:
                    vidam = vidam - 20
                    print (f"A vida do monstro agora é {vidam} HP")       
                    print ("Vez do monstro atacar")
                    luta(y, vidap, danom)
                else:
                    print("Nenhum dano foi dado no monstro, agora é a vez dele")
                    print (f"A vida do monstro agora é {vidam} HP") 
                    luta(y, vidap, danom)
            
                #---------------------------------------------------------------  
        if vidam < 0:
            print("Você matou o monstro")
            return vidap
        elif vidap <0:
            return vidap
        
lista_inventario=[]
def criar_inventario():
    dicionario_inventario=descricao_inventario
    a = random.randint ( 0, len(dicionario_inventario)-1)
    lista=[]
    for q in dicionario_inventario:
        lista.append(q)
    item = lista[a]
    inventario=lista_inventario
    inventario.append(item)
    return item

def utilizar_dicionario(lista, dicionario): 
    pergunta=input("Qual item você deseja utilizar?")
    if pergunta not in lista:
        print("Você não possui esse item, responda corretamente")
        pergunta=input("Qual item você deseja utilizar?") 
    elif pergunta=="chave secreta":
        print("A chave secreta não é um item utilizavél em batalhas")
        if len(lista)>0:
            pergunta2=input("Deseja usar outro item?")
            if pergunta2!=sim or pergunta2!=nao or pergunta2!=não:
                print("Responda corretamente")
                pergunta2=input("Deseja usar outro item?")
            elif pergunta2==sim:
                pergunta=input("Qual item você deseja utilizar?")
            elif pergunta2==nao or pergunta2==não: 
                lista_final=lista
        else:
            lista_final=lista
    else: 
        i=0
        while i<len(lista):
            if lista[i]==pergunta:
                del lista[i]
                lista_final=lista
                break
            else: 
                i+=1
        print(dicionario[pergunta]["utilizar"])
        print("Seu inventario agora é:", lista_final)
    return lista_final
        
def main():
    hp=100
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
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            #escolha do cenario
            for e in opcoes:
                opcao = opcoes[e]
                print (f"Você pode {opcao} (para essa opção escreva: {e})")
            escolha = input ("O que você quer fazer? ")
            #definição se os monstros e/ou premios irão existir em determinado momento.
            aparicaodemonstro = random.choice([True, False])
            ganharpremio = random.choice([True, False])
            acao = False
            if aparicaodemonstro == True or ganharpremio == True:
                acao = True
            while acao == True:   
                if aparicaodemonstro == True and ganharpremio == True:
                    premio=criar_inventario()
                    print("voce ganhou", premio)
                    print("seu inventario agora é:", lista_inventario)
                    print(descricao_inventario[premio]["descricao"])
                    print('Você encontrou um monstro!')
                    utilizar=input("Antes de iniciar a batalha você deseja utilizar algum item do seu inventário?")
                    if utilizar=="sim":
                        y=utilizar_dicionario(lista_inventario, descricao_inventario)
                        x= combate()
                    elif utilizar=="nao" or utlizar=="não":
                        x=combate()

                    #vida do monstro - talvez fazer uma funcao para as batalhas
                    #premios - basicamente alterar hp do personagem, no inicio, mas depois queremos implementar
                    #adicionar itens no inventário, que ainda PRECISA SER FEITO.
                    
                    #hp=hp +20  ----------------------- ARRUMAR
                    hp = combate()
                    if hp <0:
                         game_over = True
                    break
                elif aparicaodemonstro == True and ganharpremio == False:

                    x = combate()
                    hp = combate()
                    if hp <0:
                        game_over = True

                    print("Você encontrou um monstro")
                    utilizar=input("Antes de iniciar a batalha você deseja utilizar algum item do seu inventário?")
                    if utilizar=="sim":
                        y=utilizar_dicionario(lista_inventario, descricao_inventario)
                        x= combate()
                    elif utilizar=="nao" or utlizar=="não":
                        x=combate()
                   # hp = combate()
                   # if hp <0:
                   #     game_over = True

                    break
                elif aparicaodemonstro == False and ganharpremio == True:
                    premio=criar_inventario()
                    print('você ganhou', premio)
                    print("seu inventario agora é:", lista_inventario)
                    print(descricao_inventario[premio]["descricao"])
                  #  hp=hp +20 ------------------------ ARRUMAR
                    break
            if escolha in opcoes:
                #se o jogador escolher ir para a sala secreta, ele precisa acertar a senha (Disney)
                #com menos de 10 tentativas para poder ir para qualquer uma das salas do jogo.
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
                #arrumar
                #se possivel colocar a frase abaixo para aparecer, caso contrario, relevar e deixar somente o "voce morreu"
                #print("Sua indecisão foi sua ruína!")
                game_over = True
    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()