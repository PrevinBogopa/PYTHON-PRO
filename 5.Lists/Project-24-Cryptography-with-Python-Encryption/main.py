message = input("Enter your message:\n").upper()
shift_number = int(input("Enter the shift number:\n"))

def encrypt(message, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    encrypted_message = message.translate(table)
    return encrypted_message

print(encrypt(message,shift_number))
