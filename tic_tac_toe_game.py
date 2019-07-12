print ("_________________***WELCOM TO TIC TAC TOE GAME***___________________")

board = [0,1,2,
 3,4,5,
 6,7,8]
def show():
    print board[0],'|',board[1],'|',board[2]
    print "___________"
    print board[3],'|',board[4],'|',board[5]
    print "___________"
    print board[6],'|',board[7],'|',board[8]
show()
def checkline(char,spot1,spot2,spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
       return True

def checkAll(char):
    if checkline(char,0,1,2):
        return True
    if checkline(char,2,5,8):
        return True
    if checkline(char,6,7,8):
        return True
    if checkline(char,3,4,5):
        return True
    if checkline(char,2,4,6):
        return True
    if checkline(char,0,4,8):
        return True
    if checkline(char,0,3,6):
        return True
    if checkline(char,1,4,7):
        return True
i = 0
while i<4:

    user_input1 = int(raw_input("choice a one char "))
    user_input = int(user_input1)
    
    if board[user_input] != 'x' and board[user_input] !='o':
        board[user_input] = 'x'
        if checkAll('x') == True:
	    show()
            print ("----X win----")
            # break
    user_input2 = int(raw_input("choice a one more char  "))
    user_input3 = int(user_input2)
    if board[user_input3] != 'o' and board[user_input3] !='x':
        board[user_input3] = 'o'
        if checkAll('o') == True:
	    show()
            print ("----0 win----")
            break
    
    #i = i+1

    else:
        print ("USER ALREDY TOOK THIS NUMBER")
    i = i+1
    show()
