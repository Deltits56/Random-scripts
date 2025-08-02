import os
from PIL import Image
from tqdm import tqdm

imgpath = ""
endpath = ""

def obtener_img(imgpath, initialdate, enddate):
    return [
        file for file in os.listdir(imgpath)
        if os.path.isfile(os.path.join(imgpath, file)) 
        and file.lower().endswith((".jpg", ".jpeg", ".png"))
        and file[:8].isdigit()
        and initialdate <= int(file[:8]) <= enddate
    ]

def compress(cimgpath, cendpath, calidad):
    with Image.open(cimgpath) as image:
        image.convert("RGB").save(cendpath, optimize = True, quality = calidad)

try:
    initialdate = int(input("Fecha inicial(YYYYMMDD): "))
    enddate = int(input("Fecha final(YYYYMMDD): "))
    if initialdate > enddate:
        print("Fechas inválidas")
        exit()
except ValueError:
    print("Fechas inválidas")
    exit()

img = obtener_img(imgpath, initialdate, enddate)

if len(img) == 0:
    print("No hay imágenes que comprimir en este rango")
    exit()

confirm = input("¿Quieres comprimir " + str(len(img)) + " imágenes? (y/n): ").strip().lower()
if confirm != "y":
    print("Compresión cancelada")
    exit()

try:
    calidad = int(input("Selecciona la calidad del 1-95, Recomendado 20-60"))
    if not (1 <= calidad <= 95):
        print("Rango incorrecto")
        exit()
except ValueError:
    print("Rango incorrecto")
    exit()

os.makedirs(endpath, exist_ok=True)
for filename in tqdm(img, desc="Comprimiendo"):
    cimgpath = os.path.join(imgpath, filename)
    cendpath = os.path.join(endpath, filename)
    compress(cimgpath, cendpath, calidad)

