def indetificarEL(x):


    c = 0                                                                             #guarda a posição do cursor na string Aidentificar
    contador = 0                                                                      #conta quantos elementos foram detectados


    Aidentificar = x
    numeros = ('0' ,'1', '2', '3', '4', '5', '6', '7', '8', '9')
    elementos = ('H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og')
    pesos =     (  1,    4,    7,    9,  11,  12,  14,  16,  19,   20,   23,   24,   27,   28,  31,  32,  35 ,  40 ,  39,  40 ,  45 ,  48 ,  51,   52,   55,   56,   59,   59,   64,   65,   70,   73,   75,   79,   80,   84,   85,   88,   89,   91,   93,  96,   98,  101,  103,  106,  108,  112,  115,  119,  122,  128, 127,  131,  133,  137,  139,  140,  141,  144,  145,  150,  152,  157,  159,  162,  165,  167,  168,  169,  173,  175,  178,  181, 184,  187,  190,  192,  195,  197,  201,  204,  207,  209,  209,  210,  222,  223,  226,  227,  232, 231,  238,  237,  244,  243,  247,  247,  251,  252,  257,  258,  259,  262,  267,  270,  271,  270,  277,  276,  281,  282,  285,  286,  289,  290,  293,  294)
    
    identificados = [                                                                 #matris (onde os resultados vão)
    [],                                                                               #elemento
    [],                                                                               #quantidade
    [],                                                                               #pesos equivalentes
    [],                                                                               #pesos
    ]


    while c<len(Aidentificar):

#-------------------------------------------------------------------------------------

        #elemetos----
        
        if Aidentificar[c:c+1] in elementos and Aidentificar[c:c+2] not in elementos: #verifica se a primeira letra depois do contador está na tabela de elementos e se a segunda não está lá.

            identificados[0].append(Aidentificar[c:c+1])

            c += 1 

        elif Aidentificar[c:c+2] in elementos:

            identificados[0].append(Aidentificar[c:c+2])

            c += 2

        else:

            return('ERRO\n(há um atómo ou valor ilegivel)')
            break

        a = 1

        while True:

            if Aidentificar[c+0+a:c+1+a] in numeros:

                a += 1

            elif Aidentificar[c+a:c+1+a] not in numeros:

                break

        #elemento====

#-------------------------------------------------------------------------------------            

        #quantidade----

        identificados[1].append(int(Aidentificar[c:c+a]))

        c += a

        #quantidade====
        
#-------------------------------------------------------------------------------------

        #pesos----

        identificados[2].append( int(pesos[elementos.index(identificados[0][contador])]) * int(identificados[1][contador]) )

        identificados[3].append( int(pesos[elementos.index(identificados[0][contador])]) )

        #pesos====
        
#-------------------------------------------------------------------------------------
                
        contador += 1

    return(identificados)

#made by https://github.com/ANT0NI0737BR
