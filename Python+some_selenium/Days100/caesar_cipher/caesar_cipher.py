import art
def caesar(text, shift, direction):
    alphabet_length = len(alphabet) - 1
    if direction == 'encode':
        text = list(text)
        for i in range(len(text)):
            letter_pozition = alphabet.index(text[i])
            if letter_pozition + shift <= alphabet_length:
                text[i] = alphabet[letter_pozition + shift]
            if letter_pozition + shift > alphabet_length:
                text[i] = alphabet[shift - (alphabet_length - letter_pozition) - 1]
        print('The encoded text is: ' + ''.join(text))

    elif direction == 'decode':
        text = list(text)
        for i in range(len(text)):
            letter_pozition = alphabet.index(text[i])
            if letter_pozition - shift >= 0:
                text[i] = alphabet[letter_pozition - shift]
            if letter_pozition - shift < 0:
                text[i] = alphabet[letter_pozition - shift]
        print('The encoded text is: ' + ''.join(text))


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

play = 'yes'
while play == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    play = input("Do you want to proceed? Type 'yes' to proceed, type 'no' to terminate.").lower()
