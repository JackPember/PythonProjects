alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode" or direction == "decode":
        break

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(text, shift):
    message = ""
    for char in text:
        if (alphabet.index(char) + shift) < len(alphabet):
            message += alphabet[(alphabet.index(char) + shift)]
        else:
            newIndex = ((alphabet.index(char) + shift) - 26)
            message += alphabet[newIndex]
    print(f"The encoded message is : {message}")


def decrypt(text, shift):
    message = ""
    for char in text:
        if (alphabet.index(char) - shift) >= 0:
            message += alphabet[alphabet.index(char) - shift]
        else:
            newIndex = ((alphabet.index(char) - shift) + 26) #python supports negative indexing, so this isn't technically necessary, but I wanted to come up with the logic
            message += alphabet[newIndex]                    #required for this function to work properly if python did not support negative indexing.
    print(f"The decrypted message is: {message}")


def checkDirection():
    if direction == "encode":
        encrypt(text=text, shift=shift)
    else:
        decrypt(text=text, shift=shift)


checkDirection()
