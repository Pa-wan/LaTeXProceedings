# CEUR-WSToc2Papers.py
# Takes as input an xml file with the table of content and the pdf file with
# the complete proceedings and extracts the single papers so that they can be
# included in the ceur-ws.org website.
#
# Usage:
#    python CEUR-WSToc2Papers.py toc.xml proceedings.pdf destination_dir
#
# (C) 2017, Giampiero Salvi <giampi@kth.se>
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import os

preamblepages = 6 # this should be extracted from the pdf somehow

xmlFileName = sys.argv[1]
pdfFileName = sys.argv[2]
destDir = sys.argv[3]

pdfProceedings = PdfFileReader(open(pdfFileName, "rb"))


with open(xmlFileName, 'r') as f:
    xmlpage=f.read()
soupObj = BeautifulSoup(xmlpage, "lxml")

def writePageRange(reader, pageRange, outputFileName):
    output = PdfFileWriter()
    for pageid in pageRange:
        output.addPage(reader.getPage(pageid))
    with open(outputFileName, "wb") as outputStream:
        output.write(outputStream)

writePageRange(pdfProceedings, range(preamblepages), os.path.join(destDir, "GLU2017_frontmatter.pdf"))

paperid = 1
for paper in soupObj.toc.findAll("paper"):
    frompage = int(paper.pages["from"])+preamblepages-1
    topage = int(paper.pages["to"])+preamblepages-1
    outputFileName = os.path.join(destDir, "GLU2017_paper-{:02d}.pdf".format(paperid))
    writePageRange(pdfProceedings, range(frompage,topage+1), outputFileName)
    paperid=paperid+1

# write author index
pageid = pdfProceedings.getNumPages()-1
writePageRange(pdfProceedings, range(pageid, pageid+1), os.path.join(destDir, "GLU2017_authorindex.pdf"))
