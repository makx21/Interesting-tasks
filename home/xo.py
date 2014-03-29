# Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) 
# who take turns marking the spaces in a 3×3 grid.
# You will be the referee for this games results. 
# You are given a result of a game and you must determine if the game ends in a win or a draw as well as who will be
# the winner. Make sure to return "X" if the X-player wins and "O" if the O-player wins.
# If the game is a draw, return "D." 

# Input: A game's result. A list of strings (Unicode). 
# Output: "X", "O" or "D". A string. 


def checkio(data):
    list = []   
    list.extend(data)
    
    for i in range(3):
        temp = ''
        for x in data: 
            temp += x[i]
        list.append(temp)
    list.append(data[0][0]+data[1][1]+data[2][2])
    list.append(data[0][2]+data[1][1]+data[2][0])
    
    for row in list:
        for s in 'XO':
            if row.count(s) == 3:
                return s
    return 'D'  

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

