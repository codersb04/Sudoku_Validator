def valid_solution(board):
    print(board)
    a=[]
    b1=[]
    b=0
    #check for row
    for idx,i in enumerate(board):
        print (board[idx])
        if len(i) > len(set(i)):  
#             print("not a sudoku, contain's double")
            return False
        else:
            for id,d in enumerate(board[idx]):
#                 print(d)

                if d in range(1,10):
                      continue
#                     print("sudoku")
                    
                else:
#                     print("not a sudoku,contains 0")
                    return False

    print("---------------------------------")        
#     check for column
    for i in range(0,9):
        for row in board:
            for elem in range(i,len(row)):
                    a.append(row[i])
                    break
        print(a)
        if len(a)>len(set(a)):
#             print("not a sudoko,contains double")
            return False
        else:
            for s in a:
                if s in range(1,10):
                      continue
#                     print("sudoku")
                else:
#                     print("not sudoku, contains 0")
                    return False
        a=[]
#         check for block
    print("----------------------------------")
    for j in range(0,9,3):
        for i in range(0,9,3):
            for row in board[j:j+3]:
#                 print(row)
                for elem in range(i,i+3):
        #              print(row[elem])
#                      print(row[elem])
                     b1.append(row[elem])
            print(b1)
            if len(b1)>len(set(b1)):
#                 print("not a sudoko,contains double")
                return False
            else:
                for s in b1:
                    if s in range(1,10):
                          continue
#                         print("sudoku")
                    else:
#                         print("not sudoku, contains 0")
                        return False
            b1=[]
    return True     
