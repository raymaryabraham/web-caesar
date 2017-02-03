import helpers

def encrypt(message, rot):
    """
    Ceaser encryption.
    """


    retText = ''
    for char in message:
        retText += helpers.rotate_character(char, rot)
    return retText
