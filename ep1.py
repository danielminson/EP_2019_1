# EP 2019-1: A vida no insper
#
# Alunos: 
# - Aluno A: Daniel Minson Pucciariello, danielp6@al.insper.edu.br
# - aluno B: Enrico Damiani, enricofd@al.insper.edu.br
# - Aluno C: Giulia Castro, giuliaac@al.insper.edu.br

print("Bem vindo ao jogo")
"\n"
modo_jogo = input("Qual modo de jogo você quer? Fácil, Médio ou Difícil: ")
while modo_jogo != "Fácil" and modo_jogo != "Médio" and modo_jogo != "Difícil" and modo_jogo != "facil" and modo_jogo != "medio" and modo_jogo != "dificil" and modo_jogo != "fácil" and modo_jogo != "médio" and modo_jogo != "difícil" and modo_jogo != "Facil" and modo_jogo != "Medio" and modo_jogo != "Dificil":
    print ("\n" "Favor digitar corretamente!")
    modo_jogo = input("\n" "Qual modo de jogo você quer? Fácil, Médio ou Difícil: ")
while modo_jogo == "Fácil" or modo_jogo == "fácil" or modo_jogo == "facil" or modo_jogo =="Facil":
    print ("\n" "Modo Fácil selecionado")
    break
while modo_jogo == "Médio" or modo_jogo == "médio" or modo_jogo == "medio" or modo_jogo =="Medio":
    print ("\n" "Modo Médio selecionado")
    break
while modo_jogo == "Difícil" or modo_jogo == "Dificil" or modo_jogo == "difícil" or modo_jogo == "dificil":
    print ("\n" "Modo Difícil selecionado")
    modo_jogo = input("Você goastaria de tentar o modo Poloni (Impossível até de compreender o que esta acontencendo)? Caso prefira, continue no difícil respondendo não. Responda com Sim ou Não: ")
    break
