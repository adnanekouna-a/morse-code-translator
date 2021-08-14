import time
from playsound import playsound

morse_code = {' ':'/', 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.' , 'O':'---' , 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', '?':'..--..', '!':'-.-.--', '.':'.-.-.-', ',':'--..--', ';':'-.-.-.', ':':'---...', '+':'.-.-.', '-':'-....-', '/':'-..-.', '=':'-...-'}

def morsify(text):
    letters_in_morse = []
    for letter in text:
        letters_in_morse.append(morse_code[letter.upper()])
    return ''.join(letters_in_morse)

def morse_sound(text):
    for d in text:
        if d == '.':
            playsound('sounds/dot.wav')
            time.sleep(0.05)
        elif d == '-':
            playsound('sounds/dash.wav')
            time.sleep(0.05)
        elif d == '/':
            time.sleep(0.15)

print('==>  Welcome to Morse Code Translator (Version 1.0)!  <==')
print('Enter your text :')
text = input('-->  ')

print('The Output:')
print(f'--> {morsify(text)}')

for letter in text:
    morse_sound(morsify(letter))
    time.sleep(0.10)
