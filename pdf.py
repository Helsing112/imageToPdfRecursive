import os
from fpdf import FPDF
from PIL import Image
import pygame

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("."):
    pdf = FPDF()
    path = root.split(os.sep)
    for file in files:
        #print(os.path.join(dirs, file))
        fpath = os.path.join(root)+"\\"+str(file)
        wpath = ".\\pdfs\\"+str(file)+".pdf"
        if(file != "pdf.py" and not file.endswith(".pdf")):
            print(fpath)

            cover = pygame.image.load(fpath)
            width = cover.get_width()
            height = cover.get_height()

    # convert pixel in mm with 1px=0.264583 mm
            width, height = float(width * 0.18), float(height * 0.18)

            pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
            pdf.add_page()
            pdf.image(fpath,0,0,width,height)
            pdf.output(wpath, "F")


wait = input("PRESS ENTER TO CONTINUE.")
