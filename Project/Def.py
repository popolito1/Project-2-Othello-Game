#1 fuction which display the number of pawns, which turn is it, etc...
def resume(turn,X,O,Player1,Player2):
    print ("\nTurn :",turn,"\nX=",X,"\nO=",O)
    if (turn%2==0): #it mean that the number of turn is even, player 1 have to play
        turn=turn+1
        return Player1,'it is your turn. What do you want to do ?'
    else:
        turn=turn+1
        return Player2,'it is your turn. What do you want todo ?'
    
#2 fuction which display the game board
def Gameboard(Table,size,lett,num,lett2,num2):
    if (size<10):
        for i in range(size):            #print the letter
           print(lett[i],end="   ")
        print("\n")
        for i in range(size):
            print(num[i],end='     ')
            for j in range (size):          #print the number and  points
                print(Table[i][j],end='     ')
            print("\n")
    else:
        for i in range(size):            
            print(lett2[i],end="   ")
        print("\n")
        for i in range (size):
            if i<10:
                print(num2[i],end='     ')
            else:
                print(num[i],end='     ')
            for j in range (size):          
                print(Table[i][j],end='     ')
            print("\n")
            
#3 Function which display the position of each pawn at the beginning
def init(size,lett,num,Table):
    for i in range (0,size+1):
        Table[int((size+1)/2)-1][int((size+1)/2)-1]=" O"   #when it's 8X8 : D4
        Table[int((size+1)/2)-1][int((size+1)/2)]=" X"     #                E5
        Table[int((size+1)/2)][int((size+1)/2)-1]=" X"     #                D5
        Table[int((size+1)/2)][int((size+1)/2)]=" O"       #                E4

        
#4 Function for the command
def Command(command,com,com1):
    while command not in com :
        return False
    if command in com1 :
        print("Enter letter and number")
        
#5 Fuction which return if the coordinate or good or not
def movesonboard(pll,placingnum,size,Table):
#Returns True if the coordinates are located on the board.
    if placingnum>=0 and placingnum<= size and  pll<=size:
        return True
    if Table[placingnum][num]==Table[int((size+1)/2)-1][int((size+1)/2)-1] or Table[placingnum][num]==Table[int((size+1)/2)-1][int((size+1)/2)] or Table[placingnum][num]==Table[int((size+1)/2)][int((size+1)/2)-1] or Table[placingnum][num]==Table[int((size+1)/2)][int((size+1)/2)]:
        return False
    else:
        return False
 
#6 All Functions to check the position of the pawn.
def north(Table,placingnum,pll,turn):
    num=placingnum
    if turn%2==0 :
        if (Table[num-1][pll]==" X"):
            return False
        while (Table[num-1][pll]==" O") and (num-1>0) : #while in the boxes above there is a "O", we continue to move up. It will stop when there is no more "O" or when the gameboard limit is reached
            num= num-1 #to continue to move up we subtrate 1
        if num-1==0: #gameboard limit reached
            return False
        else:
            if (Table[num-1][pll]==" X"):
                return True
            return False
    if turn%2==1 :
        if (Table[num-1][pll]==" O"):
            return False
        while (Table[num-1][pll]==" X") and (num-1>0) :
            num= num-1
        if num-1==0:
            return False
        else:
            if (Table[num-1][pll]==" O"):
                return True
            return False
        
def south(Table,placingnum,pll,turn,size):
    num=placingnum
    if turn%2==0 :
        if (Table[num+1][pll]==" X"):
            return False
        while (Table[num+1][pll]==" O") and (num<size) :
            num= num+1
        if num==size:
            return False
        else:
            if (Table[num+1][pll]==" X"):
                return True
            return False
    if turn%2==1 :
        if (Table[num+1][pll]==" O"):
            return False
        while (Table[num+1][pll]==" X") and (num<size) :
            num= num+1
        if num==size:
            return False
        else:
            if (Table[num+1][pll]==" O"):
                return True
            return False
        
def east(Table,placingnum,pll,turn,size):
    pll2=pll
    if turn%2==0 :
        if (Table[placingnum][pll2+1]==" X"):
            return False
        while (Table[placingnum][pll2+1]==" O") and (pll2<size) :
            pll2= pll2+1
        if pll2==size:
            return False
        else:
            if (Table[placingnum][pll2+1]==" X"):
                return True
            return False
    if turn%2==1 :
        if (Table[placingnum][pll2+1]==" O"):
            return False
        while (Table[placingnum][pll+1]==" X") and (pll2<size) :
            pll2 = pll2 +1
        if pll2==size:
            return False
        else:
            if (Table[placingnum][pll2+1]==" O"):
                return True
            return False

def west(Table,placingnum,pll,turn):
    pll2=pll
    if turn%2==0 :
        if (Table[placingnum][pll2-1]==" X"):
            return False
        while (Table[placingnum][pll2-1]==" O") and (pll2-1>0) :
            pll2= pll2-1 
        if pll2-1==0:
            return False
        else:
            if (Table[placingnum][pll2-1]==" X"):
                return True
            return False
    if turn%2==1 :
        if (Table[placingnum][pll2-1]==" O"):
            return False
        while (Table[placingnum][pll2-1]==" X") and (pll2-1>0) :
            pll2= pll2-1
        if pll2-1==0:
            return False
        else:
            if (Table[placingnum][pll2-1]==" O"):
                return True
            return False
        
def northeast(Table,placingnum,pll,turn,size):
    num=placingnum
    pll2=pll
    if turn%2==0:
        if (Table[num-1][pll2+1]==" X"):
            return False
        while (Table[num-1][pll2+1]==" O") and (num-1>0) and (pll2<size) :
            num= num-1
            pll2=pll2+1
        if num-1==0 or pll2==size:
            return False
        else:
            if (Table[num-1][pll2+1]==" X"):
                return True
            return False
    elif turn%2==1 :
        if (Table[num-1][pll2+1]==" O"):
            return False
        while (Table[num-1][pll2+1]==" X") and (num-1>0) and (pll2<size) :
            num= num-1
            pll2=pll2 +1
        if (num-1==0) or (pll2==size):
            return False
        else:
            if (Table[num-1][pll2+1]==" O"):
                return True
            return False
        
def nortwest(Table,placingnum,pll,turn):
    num=placingnum
    pll2=pll
    if turn%2==0:
        if (Table[num-1][pll2-1]==" X"):
            return False
        while (Table[num-1][pll2-1]==" O") and (num-1>0) and (pll2-1>0) :
            num= num-1
            pll2=pll2-1
        if num-1==0 or pll2-1==0:
            return False
        else:
            if (Table[num-1][pll2-1]==" X"):
                return True
            return False
    if turn%2==1 :
        if (Table[num-1][pll2-1]==" O"):
            return False
        while (Table[num-1][pll2-1]==" X") and (num-1>0) and (pll2-1>0) :
            num= num-1
            pll2 = pll2-1
        if (num-1==0) or (pll2-1==0):
            return False
        else:
            if (Table[num-1][pll2-1]==" O"):
                return True
            return False
        
        
def southeast(Table,placingnum,pll,turn,size):
    num=placingnum
    pll2=pll
    if turn%2==0:
        if (Table[num+1][pll2+1]==" X"):
            return False
        while (Table[num+1][pll2+1]==" O") and (num<size) and (pll2<size) :
            num= num+1
            pll2=pll2+1
        if num==size or pll2==size:
            return False
        else:
            if (Table[num+1][pll2+1]==" X"):
                return True
            return False
    if turn%2==1 :
        if (Table[num+1][pll2+1]==" O"):
            return False
        while (Table[num+1][pll2+1]==" X") and (num<size) and (pll2<size) :
            num= num+1
            pll2 = pll2 +1
        if (num==size) or (pll2==size):
            return False
        else:
            if (Table[num+1][pll2+1]==" O"):
                return True
            return False
        
def southwest(Table,placingnum,pll,turn,size):
    num=placingnum
    pll2=pll
    if turn%2==0:
        if (Table[num+1][pll2-1]==" X"):
            return False
        while (Table[num+1][pll2-1]==" O") and (num<size) and (pll2-1>0) :
            num= num+1
            pll2=pll2-1
        if num==size or pll2-1==0:
            return False
        else:
            if (Table[num+1][pll2-1]==" X"):
                return True
            return False
    if turn%2==1 :
        if (Table[num+1][pll2-1]==" O"):
            return False
        while (Table[num+1][pll2-1]==" X") and (num<size) and (pll2-1>0) :
            num= num+1
            pll2 = pll2-1
        if (num==size) or (pll2-1==0):
            return False
        else:
            if (Table[num+1][pll2-1]==" O"):
                return True
            return False

#Function 6 check if we can place the pawn
def invalidmoves (Table,placingnum,pll,turn,size):
    if north(Table,placingnum,pll,turn) == True:
        return True
    elif south(Table,placingnum,pll,turn,size) == True:
        return True
    elif east(Table,placingnum,pll,turn,size) == True:
        return True
    elif west(Table,placingnum,pll,turn) == True:
        return True
    elif northeast(Table,placingnum,pll,turn,size) == True:
        return True
    elif nortwest(Table,placingnum,pll,turn) == True:
        return True
    elif southeast(Table,placingnum,pll,turn,size) == True:
        return True
    elif southwest(Table,placingnum,pll,turn,size) == True:
        return True
    return False #it mean no one is good so the coordinates are invalids

    
# Function 8 flip the pawn
def flip (turn,Table,placingnum,pll,size):
    if north(Table,placingnum,pll,turn)==True:
        if turn%2==1:
            y=placingnum-1
            while Table[y][pll] == " X":
                Table[y][pll] = " O"
                y = y-1
        if turn%2==0:
            y=placingnum-1
            while Table[y][pll] == " O":
                Table[y][pll] = " X"
                y = y-1
                
    if northeast(Table,placingnum,pll,turn,size)==True:
        if turn%2==1:
            y=placingnum-1
            x=pll+1
            while Table[y][x] == " X":
                Table[y][x]= " O"
                x += 1
                y -= 1          
        if turn%2==0:
            y=placingnum-1
            x=pll+1
            while Table[y][x] == " O" :
                Table[y][x]=" X"
                x += 1
                y -= 1
            
    if nortwest(Table,placingnum,pll,turn)==True: 
        if turn%2==1:
            y=placingnum-1
            x=pll-1
            while Table[y][x] == ' X' :
                Table[y][x]= ' O'
                x -= 1
                y -= 1
        if turn%2==0:
            y=placingnum-1
            x=pll-1
            while Table[y][x] == " O":
                Table[y][x]=" X"
                x -= 1
                y -= 1
                
    if south(Table,placingnum,pll,turn,size)==True:
        if turn%2==1:
            y=placingnum+1
            while Table[y][pll] == " X":
                Table[y][pll]=" O"
                y += 1
        if turn%2==0:
            y=placingnum+1
            while Table[y][pll] == " O":
                Table[y][pll]= " X"
                y += 1
                      
    if southwest(Table,placingnum,pll,turn,size)==True :
        if turn%2==1:
            y=placingnum+1
            x=pll-1
            while Table[y][x] == " X":
                Table[y][x]= " O"                  
                x -= 1
                y += 1
        if turn%2==0:
            y=placingnum+1
            x=pll-1
            while Table[y][x] == " O" :
                Table[y][x]= " X"
                x -= 1
                y+= 1
            
    if southeast(Table,placingnum,pll,turn,size)==True :
        if turn%2==1:
            y=placingnum+1
            x=pll+1
            while Table[y][x] == " X":
                Table[y][x]= " O"
                x += 1
                y += 1
        if turn%2==0:
            y=placingnum+1
            x=pll+1
            while Table[y][x] == " O":
                Table[y][x]= " X"
                x += 1
                y += 1
          
    if east(Table,placingnum,pll,turn,size)==True :
        if turn%2==1:
            x=pll+1
            while Table[placingnum][x] == " X": 
                Table[placingnum][x]= " O"
                x += 1
            Table[placingnum][x]= " O"
        if turn%2==0:
            x=pll+1
            while Table[placingnum][x] == " O": 
                Table[placingnum][x]=" X"              
                x += 1
            Table[placingnum][x]=" X"
               
    if west(Table,placingnum,pll,turn)==True:
        if turn%2==1:
            x=pll-1
            while Table[placingnum][x] == " X":
                Table[placingnum][x]=" O"
                x -= 1
        if turn%2==0:
            x=pll-1
            while Table[placingnum][x] == " O":
                Table[placingnum][x]=" X"
                x -= 1
               
              
#8 Place a pawn anywhere
def placingpawns(size,pll,placingnum,Table,turn):
        if turn%2==0:
            Table[placingnum][pll]=" X"
        else:
            Table[placingnum][pll]=" O"
        
#9 Function to stop the game
def Continue(X,O,size,command):
    if X== size*size or O==size*size:
        return False
    if command == ("A"):
        return False
    if X+O == size*size:
        return False
    return True


#10Count the score
def score(size,Table,X,O):
# Determine the score by counting the X and O. Returns a dictionary with keys 'X' and 'O'.
    for x in range(size):
        for y in range(size):
            if Table[x][y] == '      X':
                X += 1
            if Table[x][y] == '      O':
                O += 1
    return X,O


#11 valid moves on request
def request1(Table,size):
    listvalidmoves = []
#12 we are going to put all the valid moves in a list
    for placingnum in range(size):
        for pll in range(size):
            #la si tous les checker sont True et bah on met les validmoves dans une liste 
                listvalidmoves.append([placingnum,pll])
    return listvalidmoves

def request2(size,Table):
    #we copy a new board without the initial position because we don't care of it 
    copygameboard=Gameboard(Table,size,lett,num,lett2,num2)
    # we change the points in _ for all the valid moves inserted in the list : listvalidmoves by the fonction request1
    for placingnum, pll in getValidMoves(copyboard):
        copyboard[x][y] = '-'
    return copyboard

#12 Function which display the winner
def winner (O,X,Player1,Player2,command, turn,com2):
    if command in com2:
        if turn %2==0:
            print (Player1, "you choose to abandon the game, you loose.", Player2, "is the winner ! ")
        else:
            print (Player2, "you choose to abandon the game, you loose.", Player1, "is the winner ! ")
    elif O<X:
        print ("Congratulation", Player1, "! You won !")
    elif X==O:
        print ("No winner, play again !")
    else:
        print ("Congratulation", Player2, "! You won !")