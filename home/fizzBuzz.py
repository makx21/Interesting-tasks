# You should write a function that will receive a positive integer and return:
# "Fizz Buzz" if the number is divisible by 3 and by 5;
# "Fizz" if the number is divisible by 3;
# "Buzz" if the number is divisible by 5;

def checkio(num):
    if not num % 15:
        s = "Fizz Buzz"    
    elif not num % 3:
        s = 'Fizz'
    elif not num % 5:
        s = 'Buzz'
    else:
        s = str(num)                
    return s

    
def checkio2(num):
   return { 
        0: str(num), 
        num % 3: 'Fizz', 
        num % 5: 'Buzz',  
        num % 15: 'Fizz Buzz' 
    }[0]
    
    
def checkio3(num):
    fizz_buzz = bool(num % 3), bool(num % 5)
    return {(False, False): "Fizz Buzz",
            (False, True): "Fizz",
            (True, False): "Buzz",
            (True, True): str(num)}[fizz_buzz]     
