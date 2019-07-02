sudoku = [
    [1,0,0,0,0,6,8,3,0],
    [0,8,0,5,7,3,0,9,0],
    [0,0,0,0,2,8,0,0,0],
    [0,7,0,3,0,1,9,8,0],
    [5,4,9,0,8,7,6,1,0],
    [8,0,0,4,0,9,2,0,0],cd
    [0,0,0,0,0,2,3,0,0],
    [7,6,3,0,0,0,0,0,9],
    [9,2,8,7,0,0,5,0,0],
    ]






def draw_board (s):
    
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j == 8 :
                print(s[i][j])
            else:
                print(s[i][j],end="  ")



def finde_null (s):
    for i in range(len(s)):
        for j in range(len(s[i])):     
            
            if s[i][j] == 0   :
                return i , j
    return None
   
    

def solution(s)   : 
    null = finde_null(s)

    if not null :
        return True
    else :
        i , j = null
    for num in range (1,10):
        if check(s,i,j,num):
            s[i][j] = num
            
            if solution(s):
                
                return True
            
            s[i][j] = 0
            
    return False
      
    

def check (s,i,j,num):
    

    # kol
    for l in range(len(s)) :
        
        if s[l][j] == num and l !=i:
            return False
            
            
    #row
    for l in range(len(s[0])):
        
        if s[i][l] == num and l != j:
            return False
           
    ##square   
    x =int( j // 3 )
    y = int(i // 3 )
    for l in range(y*3,y*3+3):
        for z in range(x*3,x*3+3):
            if s[l][z] == num and l != i and z != j :
                return False
                
    return True      
    

def main(s):
    
    draw_board(s)
    solution(s)
    print("")
    print("")

    draw_board(s)

    

main(sudoku)