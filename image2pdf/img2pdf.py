from os import listdir
from fpdf import FPDF


path="/home/vivek/Pictures/Wallpapers/"

imagelist=listdir(path)
imagelist.sort()

pdf=FPDF('P','mm','A4')

x=0
y=0
w=210
h=297

for image in imagelist:
	pdf.add_page()
	pdf.image(path+image,x,y,w,h)

pdf.output("output.pdf","F")