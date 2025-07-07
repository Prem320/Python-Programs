"""
Mini Project
TIC_TAC_TOE
"""
li = [1,2,3,4,5,6,7,8,9]
player = 'X'
flag = False
step = []
wins = [(0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8)]
while True:
    print("\n\n\t\t***** TIC-TAC-TOE *****")
    print("\n\t\t      ",li[0],"|",li[1],"|",li[2])
    print("\t\t     -------------")
    print("\t\t      ",li[3],"|",li[4],"|",li[5])
    print("\t\t     -------------")
    print("\t\t      ",li[6],"|",li[7],"|",li[8])
    if flag:
        break
    print("\n\t\t    PLAYER",player,"TURNS : ",end="")
    ch = int(input())
    if ch not in step:
        step.append(ch)
        li[ch-1] = player
        for tu in wins:
            if li[tu[0]]==li[tu[1]] and li[tu[1]]==li[tu[2]]:
                print("\n\n\t\t    PLAYER",player,"WINS!")
                flag = True
        if player=='X':
            player='O'
        else:
            player='X'
    else:
        print("\n\t\t   DO NOT REPEAT ANY VALUE\n\t\t   TRY AGAIN!")