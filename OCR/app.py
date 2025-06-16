import openpyxl
import pytesseract
import cv2

caminho = r"C:\Program Files\Tesseract-OCR"

#1: ler imagem

imagem = cv2.imread(r"C:\Users\tatal\Desktop\projetosContest\OCR\print_magalu.JPG")

#2: tesseract extrair o texto da imagem

pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
texto = pytesseract.image_to_string(imagem, lang='por')

print(texto)
