#!/usr/bin/env python
import pathlib

def split_by_id(S, list_of_indices):
     left, right = 0, list_of_indices[0]
     yield S[left:right]
     left = right
     for right in list_of_indices[1:]:
         yield S[left:right]
         left = right
     yield S[left:]

def getMorseCode(image):
    from PIL import Image
    im = Image.open(image, 'r')
    chars = []
    background = im.getdata()[0]
    for i, v in enumerate(list(im.getdata())):
        if v == background:
            chars.append(" ")
        else:
            chars.append("*")
    x = []
    blank = " "
    output =  "".join(chars)
    output = output.replace("***","-")
    output = output.replace("*",".")
    output = output.strip()
    if [n for n in range(len(output)) if output.find('  ', n) == n]:
        index = [n for n in range(len(output)) if output.find('  ', n) == n]
        outputs = [i for i in split_by_id(output, index)]
        outputs = [i for i in outputs if i != blank]
        for k in outputs:
            k = str(k).replace(' ','')
            x.append(k)
    else:
        output = output.replace(" ","")
        x.append(output)
    return x

def morseToPassword(morse):
    MORSE_CODE_DICT = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
        '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
        '..---': '2', '...--': '3', '....-': '4', '.....': '5',
        '-....': '6', '--...': '7', '---..': '8', '----.': '9',
        '-..-.': '/', '.-.-.-': '.', '-.--.-': ')', '..--..': '?',
        '-.--.': '(', '-....-': '-', '--..--': ','
    }
    for item in morse:
        password = "".join([MORSE_CODE_DICT.get(item) for item in morse]).lower()
        return password

def main():
  print(morseToPassword(getMorseCode( pathlib.Path('pwd.png').absolute().as_posix())))
if __name__ == "__main__":
  main()
