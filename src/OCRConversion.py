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


    custom_config = r'--psm 6 --oem 3'

    # print(custom_config)

    
    text = pytesseract.image_to_string(img)
    print("\n\n" + text + "\n\n")
    
    # print(Fore.GREEN+ "\nOutput Text:\n" + Fore.RESET)
    # print(text)
    
    return text


if "__main__" == __name__:
    actualConversion("test.jpg")
    '''parser = argparse.ArgumentParser(description='Image to Text OCR')
    parser.add_argument('filename', type=argparse.FileType('r'))
    args = parser.parse_args()
    actualConversion(args.filename.name)'''

    '''
    dragDropElement.addEventListener("drop", function (event) {
        var boxText = document .getElementById("texts")
        boxText. innerHTML = "Processing...";
        boxText.style.color = "black"
        event. stopPropagation () ; event.preventDefault () ;
    '''