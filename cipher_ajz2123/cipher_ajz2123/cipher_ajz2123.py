def cipher(text, shift, encrypt=True):
    """
    This is a function used to encipher or decipher keyboard text input using the Casesar cipher.

    Inputs:
    (1) Text: alphabetical strings to encrypt or decrypt;
    (2) Shift: integer input to replace plaintext letter with a different one with fixed number of places up or down the alphabet;
    (3) Encrypt: Boolean value (e.g., True, False);
        If the encrypt parameter is set to True, the text will be encrypted;
        If the encrypt parameter is set to False, the text will be decrypted.

    Output:
    The output is text that shows the result of the encipher or decipher.

    Examples:
    
    from cipher_ajz2123 import cipher_ajz2123

    cipher('abc', 5, True)
    'fgh'

    cipher('abc', 5, False)
    'VWX'

    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
