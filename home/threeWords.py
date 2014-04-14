# You are given a string with words and numbers separated by whitespaces (one space). 
# The words contains only letters. You should check if the string contains three words in succession. 

def checkio(data):
    count = 0
    for i in data.split():
        if i.isalpha():
            count+=1
        else:
            count = 0   
        if count == 3:
            return True
    return False
    
def checkio2(data):
    return 'www' in ''.join('d' if w.isdigit() else 'w' for w in data.split())
