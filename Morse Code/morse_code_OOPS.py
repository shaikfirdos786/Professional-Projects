class MorseCodeConverter:
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
    }

    def __init__(self):
        self.morse_code_dict = {v: k for k, v in self.MORSE_CODE_DICT.items()}

    def encode_text(self, text):
        output_list = []
        for letter in text:
            if letter.upper() in self.MORSE_CODE_DICT:
                output_list.append(self.MORSE_CODE_DICT[letter.upper()])
            else:
                output_list.append(letter)
        return " ".join(output_list)

    def decode_morse_code(self, morse_code):
        words = morse_code.split(' / ')
        decoded_message = ''
        for word in words:
            characters = word.split()
            decoded_word = ''
            for char in characters:
                if char in self.morse_code_dict:
                    decoded_word += self.morse_code_dict[char]
            decoded_message += decoded_word + ' '
        return decoded_message.strip()

    def run_program(self):
        proceed = True
        while proceed:
            operation = input('Enter "Encode" to convert text to Morse code or "Decode" to convert Morse code to text: ')
            if operation.capitalize() == 'Encode':
                text = input('Enter the text to convert into Morse Code: ')
                morse_code = self.encode_text(text)
                print(f'Morse Code of the entered text is: {morse_code}')

            elif operation.capitalize() == 'Decode':
                morse_code = input("Enter the Morse code: ")
                decoded_message = self.decode_morse_code(morse_code)
                print("Decoded Text: ", decoded_message)

            else:
                print('Incorrect Operation!')

            perform = input('Do you want to perform another operation? Enter "Yes" or "No": ')
            while perform.capitalize() != 'Yes' and perform.capitalize() != 'No':
                perform = input('Please enter "Yes" or "No": ')

            if perform.capitalize() == 'Yes':
                proceed = True
            else:
                proceed = False


# Create an instance of MorseCodeConverter class
converter = MorseCodeConverter()

# Run the program
converter.run_program()
