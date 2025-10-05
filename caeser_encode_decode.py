# List of letters in the alphabet (lowercase only)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Get user input
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    # TODO-2: Inside the 'encrypt()', shift each letter forward in the alphabet by shift_amount
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            # Find current position
            position = alphabet.index(letter)
            # Shift forward with wrap-around using modulo
            new_position = (position + shift_amount) % len(alphabet)
            cipher_text += alphabet[new_position]
        else:
            # Keep non-alphabetic characters unchanged (spaces, punctuation, etc.)
            cipher_text += letter
    print(f"Here is the encoded result: {cipher_text}")


# TODO-3: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def decrypt(original_text, shift_amount):
    # TODO-4: Inside the 'decrypt()', shift each letter backward in the alphabet by shift_amount
    plain_text = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            # Shift backward with wrap-around using modulo
            new_position = (position - shift_amount) % len(alphabet)
            plain_text += alphabet[new_position]
        else:
            plain_text += letter  # Keep spaces/punctuation
    print(f"Here is the decoded result: {plain_text}")


# TODO-5: Check the direction variable and call the correct function (encrypt/decrypt)
if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(original_text=text, shift_amount=shift)
else:
    print("Invalid choice. Please type 'encode' or 'decode'.")