'''
**Installation**
Mac - brew install tesseract
Ubuntu - sudo apt install tesseract-ocr
pip install opencv-python for cv2

'''

import pytesseract
import cv2
from colorama import Fore

def actualConversion(image1):
    img = cv2.imread(image1)



    print(Fore.GREEN+ "\nOutput Text:\n" + Fore.RESET)
    print(pytesseract.image_to_string(img))
    return pytesseract.image_to_string(img)


if "__main__" == __name__:
    actualConversion("../static/img.png")
    '''parser = argparse.ArgumentParser(description='Image to Text OCR')
    parser.add_argument('filename', type=argparse.FileType('r'))
    args = parser.parse_args()
    actualConversion(args.filename.name)'''