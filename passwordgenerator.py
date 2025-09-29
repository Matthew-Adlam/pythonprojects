import random
import string

def choosePassword(characterNumber, specialCharacters=True, capitals=True, smalls=True, numbers=True):
    pool = ""
    
    if smalls:
        pool += string.ascii_lowercase
    if capitals:
        pool += string.ascii_uppercase
    if numbers:
        pool += string.digits
    if specialCharacters:
        pool += string.punctuation
    
    if not pool:
        raise ValueError("No character sets selected for password generation.")
    
    # Randomly choose characters from the pool
    password = "".join(random.choice(pool) for _ in range(characterNumber))
    return password

def main():
    a = choosePassword(12, True, True, True, True)
    print(a)

main()
