print('hello world \n um pouquinho mais')
print("exu67678")

#grande primeira anotação

#add 1 ou 2 primeiro teste de treino :)

#primeiro o ideal é tentar antes de fazer o jogo da mão o jogo que voce tem que escolher aumentar 1 ou 2 e ver se consegue pegar o ultimo numero
#deu pra entender é aquele q um joga 1 dai o outro pega dois e ai quem pega o ultimo ganha
#a logica do jogo é basica o ideal é tentar fazer o computador entender a logica fds
#:)


import random
#pro limite não ser sempre o mesmo, vamos fazer ele variar entre 5 e 15
#eu não sei como desativar a ia que fica completando minhas frases dai essa frase de cima saiu com virgula

def getlimit():
    limit = range(5,15)
    return random.choice(limit)

def escrever(string):
    with open("textodeexuvis.txt", 'w') as txtgoat:
        txtgoat.write(string)

def separ(ints):
    if isinstance(ints, int):
        if ints//2 == ints/2:
            return '0'
        else:
            return '1'

#aqui ela tipo retorna algo que eu escreva pra ficar guardado :)
 
def game() -> str:
    limit = getlimit()
    stringtodapoderosa = ''
    print(stringtodapoderosa)
    #stringtodapoderosa += str(limit) + 'l'
    index = 0
    limi = limit
    while limit > 0:
        index += 1
        r = random.choice([1,2])
        limit -= r
        stringtodapoderosa += separ(index) + 'R' + str(r)
    return str(limi) + 'l' + separ(index) + 'V' + stringtodapoderosa


#base while só pq eu aprendi a fazer assim

#es ue raçemoc a revercse oa oirartnoc a ai n agep gg ysae ):

while True:
    a = input(': ')
    if a in ['sair', 'exit', 'quit']:
        break
    if a == 'game':
        oquevaiserescrito = ''
        for _ in range(10000):
            print('ok') 
            oquevaiserescrito += game() + '\n'
        escrever(oquevaiserescrito)
