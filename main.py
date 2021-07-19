from vigenere import Vigenere


def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    cleartext = "hello world"
    key = "hello"

    ciphertext = Vigenere.vigenere(cleartext, key, alphabet, True)
    print("clear text: " + cleartext)
    print("encrypted: " + ciphertext)
    print("decrypted: " + Vigenere.vigenere(ciphertext, key, alphabet, False))


main()
