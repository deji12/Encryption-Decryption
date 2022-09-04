import random

EncryptionCharacters = [
                    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                    '_',  '-', '=', '+', '[', ']', '{', '}', ';', ':',
                    '|', '<',  '>', ',', '.', '?'
] 

EncryptionCharactersForNumbers = [
                    '`', "'",  '"', '/', '§', '±', '~', '€', '₺'
]

PossibleAlphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
                    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
random.shuffle(PossibleAlphabets)

PossibleNumbers = [
                    '1', '2', '3', '4', '5', '6', '7', '8', '9',
]
random.shuffle(PossibleNumbers)

key = ''
for i in PossibleAlphabets:
    key += i
key += '|'
for j in PossibleNumbers:
    key += j

def Encrypt():
    while True:
        UserInput = input('> Enter Text to be encrypted: ') # user input
        if UserInput:
            break

    FinalEncryptedText = ''

    for i in UserInput:
        if i.isnumeric():
            IndexOfNumber = PossibleNumbers.index(i)
            MapNumberIndexToEncryptionCharactersIndex = EncryptionCharactersForNumbers[IndexOfNumber]
            FinalEncryptedText += MapNumberIndexToEncryptionCharactersIndex
        else:
            IndexOfLetter = PossibleAlphabets.index(i) 
            MapLetterIndexToEncryptionCharactersIndex = EncryptionCharacters[IndexOfLetter]
            FinalEncryptedText += MapLetterIndexToEncryptionCharactersIndex

    print(f'Encrypted Text:  {FinalEncryptedText}')
    print(f'Secret Key: {key} \n Make sure you keep this key as it will be used to decrypt encrypted text. If lost, excrypted text will be lost.')



def Decrypt():
    while True:
        TextToBeDecrypted = input('Enter text: ')
        Key = input('Enter key: ')
        if TextToBeDecrypted and Key:
            break

    DecryptedText = ''

    for i in TextToBeDecrypted:
        if i in EncryptionCharactersForNumbers:
            SplittedKey = Key.split('|')[1]
            IndexOfEncryptedNumber = EncryptionCharactersForNumbers.index(i)
            MapEncryptedNumberToKey = SplittedKey[IndexOfEncryptedNumber]
            DecryptedText += MapEncryptedNumberToKey

        else:
            IndexOfEncryptedCharacter = EncryptionCharacters.index(i)
            MapEncryptedCharacterToKey = Key[IndexOfEncryptedCharacter]
            DecryptedText += MapEncryptedCharacterToKey

    print()
    print(f'Decrypted Text: {DecryptedText}')

def main():
    print('> What operation do you want to perform? ')
    print('> 1. Encrypt')
    print('> 2. Decrypt')
    while True:
        print()
        Operation = input('Enter operation number: ')
        print()
        if Operation == '1':
            Encrypt()
        elif Operation == '2':
            Decrypt()
        else:
            print('> Unknown operation')
main()