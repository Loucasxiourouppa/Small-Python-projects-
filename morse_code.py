MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.",
    "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-", '"': ".-..-.", "$": "...-..-", "@": ".--.-.", "?": "..--..",
    "!": "-.-.--", ".": ".-.-.-", ",": "--..--", "'": ".----."
}

def print_intro():
    print("Welcome to Wolmore")
    print("This program encodes and decodes Morse Code.")

def get_input():
    mode = input("Would you like to encode (e) or decode (d): ").lower()
    while mode != "e" and mode != "d":
        print("Invalid mode.")
        mode = input("Would you like to encode (e) or decode (d): ").lower()
    message = input("What message would you like to encode/decode: ").upper()
    return mode, message

def encode(message):
    morse_code = ""
    for char in message:
        if char == " ":
            morse_code += " "
        elif char in MORSE_CODE:
            morse_code += MORSE_CODE[char] + " "
        else:
            morse_code += char
    return morse_code

def decode(message):
    morse_code = message.split(" ")
    decoded_message = ""
    for symbol in morse_code:
        if symbol == "":
            decoded_message += " "
        elif symbol in MORSE_CODE.values():
            decoded_message += [char for char, code in MORSE_CODE.items() if code == symbol][0]
    return decoded_message

def main():
    print_intro()
    while True:
        mode, message = get_input()
        if mode == "e":
            result = encode(message)
            print(f"Encoded message: {result}")
        else:
            result = decode(message)
            print(f"Decoded message: {result}")

        another = input("Would you like to encode/decode another message (y/n): ").lower()
        while another != "y" and another != "n":
            print("Invalid input.")
            another = input("Would you like to encode/decode another message (y/n): ").lower()
        
        if another == "n":
            break

if __name__ == '__main__':
    main()
