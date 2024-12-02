morse_code = {
    "A": "._",
    "B": "_...",
    "C": "_._.",
    "D": "_..",
    "E": ".",
    "F": ".._.",
    "G": "__.",
    "H": "....",
    "I": "..",
    "J": ".___",
    "K": "_._",
    "L": "._..",
    "M": "__",
    "N": "_.",
    "O": "___",
    "P": ".__.",
    "Q": "__._",
    "R": "._.",
    "S": "...",
    "T": "_",
    "U": ".._",
    "V": "..._",
    "W": ".__",
    "X": "_.._",
    "Y": "_.__",
    "Z": "__..",
     1 : ".____",
     2 : "..___",
     3 : "...__",
     4 : "...._",
     5 : ".....",
     6 : "_....",
     7 : "__...",
     8 : "___..",
     9 : "____.",
     0 : "_____",
    " ": "   "
}


def text_to_morse():
    text = input("Enter Your Text to be changed to Morse Code: ").upper()
    morse = ""
    for char in text:
        if char in morse_code:
            morse += morse_code[char]
        else:
            pass
    return morse


quit = ""
while quit != 'q':
    print(text_to_morse())
    quit = input("Continue or Exit? enter 'q' to exit.")






