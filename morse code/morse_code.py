morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ',': '--..--', ':': '---...', "'": '.----.', '.': '.-.-.-', 
    '!': '-.-.--', '?': '..--..', ' ': '/'
}

def text_to_morse(text):
    text = text.upper()
    morse_code = []

    for char in text:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append(char)

    return ' '.join(morse_code)

def morse_to_text(morse_code):

    reverse_morse_dict = {v: k for k, v in morse_code_dict.items()}

    morse_code = morse_code.split()
    text = []

    for code in morse_code:
        if code in reverse_morse_dict:
            text.append(reverse_morse_dict[code])
        else:
            text.append(code)

    return ''.join(text)

def save_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n') 

while True:
    print("Options:")
    print("1: Encode text to Morse code and save to file")
    print("2: Decode Morse code to text and save to file")
    print("3: Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        input_text = input("Enter text to encode to Morse code: ")
        morse_result = text_to_morse(input_text)
        print("Morse code:", morse_result)
        save_to_file("encoded_morse_codes.txt", morse_result)
    elif choice == '2':
        morse_code = input("Enter Morse code to decode to text (use spaces between Morse code symbols): ")
        text_result = morse_to_text(morse_code)
        print("Decoded text:", text_result)
        save_to_file("decoded_texts.txt", text_result)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
