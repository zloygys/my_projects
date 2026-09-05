import random
def generate_password(lowercase, numbers, uppercase, symbols):
    password = []
    if lowercase == True:
        for i in range(4):
            lower = random.choice("abcdefghijllmnopqrstuvwxyz")
            password.append(lower)
    if numbers == True:
        for i in range(4):
            number = random.choice("0123456789")
            password.append(number)
    if uppercase == True:
        for i in range(4):
            upper = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            password.append(upper)
    if symbols == True:
        for i in range(4):
            symbol = random.choice("!@#$%^&*()")
            password.append(symbol)
    
    random.shuffle(password)
    return "".join(password)

            
    
    
