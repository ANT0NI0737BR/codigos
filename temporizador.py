import time as tm

tempo = 2 #duração entre a repetição do codigo

tempoinicio = float(tm.time()) 

numerodevezes = 0

while True:

    tempodesdoinicio = ((tm.time()) - tempoinicio - (tempo * numerodevezes)) #a quanto tempo o programa está rodando

    if tempodesdoinicio > tempo:  #o codigo a ser executado deve ser colocado aqui dentro!
         
        print('olá')

        numerodevezes = numerodevezes + 1

        print(tempodesdoinicio)

#made by https://github.com/ANT0NI0737BR
