import time

from playsound import playsound

morse_code = {' ':'/', 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.' , 'O':'---' , 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', '?':'..--..', '!':'-.-.--', '.':'.-.-.-', ',':'--..--', ';':'-.-.-.', ':':'---...', '+':'.-.-.', '-':'-....-', '/':'-..-.', '=':'-...-'}

def morsify(text:str) -> str:
    '''Transforms each character of a given text to its morse equivalent'''
    letters_in_morse = []
    for char in text:
        letters_in_morse.append(morse_code[char.upper()])
    return ''.join(letters_in_morse)

def morse_sound(text:str) -> None:
    '''Translates morse code into sounds'''
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
input_text = input('-->  ')

print('The Output:')
print(f'--> {morsify(input_text)}')

for letter in input_text:
    morse_sound(morsify(letter))
    time.sleep(0.10)
