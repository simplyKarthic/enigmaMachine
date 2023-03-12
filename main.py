
from keyboard import Keyboard
from pluckboard import PluckBoard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma

constLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

KB = Keyboard()
PB = PluckBoard(["AR","GK","OX"])

ENIGMA = Enigma(A,I,II,III,PB,KB)

ENIGMA.set_rings((5,26,2))

ENIGMA.set_key("CAT")

message = "hi im karthic".upper()

code="VL UZ MCXRQVA"
cipherText = ""
for i in code:
    if i.isalpha():
        cipherText = cipherText + ENIGMA.encipher(i) 
    else:
        cipherText = cipherText + ' '
        
print(cipherText)

