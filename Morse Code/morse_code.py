MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

morse_code_dict = {v: k for k, v in MORSE_CODE_DICT.items()}

proceed = True
while proceed:
    operation = input('Enter "Encode" to convert text to Morse code or "Decode" to convert Morse code to text: ')
    if operation.capitalize() == 'Encode':
        text = input('Enter the text to convert into Morse Code: ')
        output_list = []
        for letter in text:
            if letter.upper() in MORSE_CODE_DICT:
                output_list.append(MORSE_CODE_DICT[letter.upper()])
            else:
                output_list.append(letter)
        morse_code = " ".join(output_list)
        print(f'Morse Code of the entered text is: {morse_code}')

    elif operation.capitalize() == 'Decode':
        morse_code = input("Enter the Morse code: ")
        words = morse_code.split(' / ')
        decoded_message = ''
        for word in words:
            characters = word.split()
            decoded_word = ''
            for char in characters:
                if char in morse_code_dict:
                    decoded_word += morse_code_dict[char]
            decoded_message += decoded_word + ' '
        print("Decoded Text: ", decoded_message.strip())

    else:
        print('Incorrect Operation!')

    perform = input('Do you want to perform another operation? Enter "Yes" or "No": ')
    while perform.capitalize() != 'Yes' and perform.capitalize() != 'No':
        perform = input('Please enter "Yes" or "No": ')

    if perform.capitalize() == 'Yes':
        proceed = True
    else:
        proceed = False
