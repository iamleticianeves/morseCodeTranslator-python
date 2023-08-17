morseCode = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                   'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                   '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
                   '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
                   ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
                   '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'}

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += morseCode[letter] + ' '
        else:
            cipher += ' '
    return cipher

def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    i = 0
    
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(morseCode.keys())[list(morseCode.values()).index(citext)]
                citext = ''
    return decipher

def main():
    print("*************************************************")
    print("*        Morse Code Translator                  *")
    print("*************************************************")
    
    message = input("\nDigite a mensagem a ser traduzida para código morse: ")
    result = encrypt(message.upper())
    print("\nCódigo Morse: " + result)
    print("\n\n-------------------------------------------------")
    
    message = input("\nDigite o código morse: ")
    result = decrypt(message)
    print("\nTradução: " + result)
    print("\n*************************************************")

if __name__ == '__main__':
    main()