# Caesar Cipher

s = input()

def caesarCipher(text): 
    cipherText = ''
    for char in text:
        if ord('a') <= ord(char) <= ord('z'):
            newChar = chr((ord(char) + 3 - ord('a')) % 26 + ord('a'))
        elif ord('A') <= ord(char) <= ord('Z'):
            newChar = chr((ord(char) + 3 - ord('A')) % 26 + ord('A'))
        else:
            newChar = char
        cipherText += newChar 
    return cipherText

def caesarDecipher(text):
    decipherText = ''
    for char in text:
        if ord('d') <= ord(char) <= ord('z'):
            newChar = chr(ord(char) - 3)
        elif ord('a') <= ord(char) <= ord('c'):
            newChar = chr(ord(char) + 23)
        elif ord('D') <= ord(char) <= ord('Z'):
            newChar = chr(ord(char) - 3)
        elif ord('A') <= ord(char) <= ord('C'):
            newChar = chr(ord(char) + 23)
        else:
            newChar = char
        decipherText += newChar
    return decipherText

crypted = caesarCipher(s)
decrypted = caesarDecipher(crypted)

print(f'Original: {s}\nCrypted: {crypted}\nDecrypted: {decrypted}')