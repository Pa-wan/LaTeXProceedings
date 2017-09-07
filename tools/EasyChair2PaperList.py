# EasyChair2PaperList
# Extracts list of authors, title and submission number for each submission
# in a EasyChair Conference and outputs a LaTeX file that can be imported
# by the LaTeXProceedings class to create the conference proceedings.
#
# Usage:
# 1) right click and download the html for the List of Submission page from
#    easychair.org into (for example) ListOfSubmissions.html
# 2) Download submissions and note the pdfBaseName (file name up to submission
#    number), for example, if the file names are in the form
#    papers/GLU2017_paper_10.pdf, then pdfBaseName="papers/GLU2017_paper_"
# 3) run:
#    python EasyChair2PaperList.py ListOfSubmissions.html pdfBaseName > papers.tex
#
# Note: in case of multiple authors, the final " and" is substituted with a ","
#   to comply with the LaTeXProceedings class.
#
# (C) 2017, Giampiero Salvi <giampi@kth.se>
from bs4 import BeautifulSoup
import sys

htmlFileName = sys.argv[1]
pdfBaseName = sys.argv[2]

with open(htmlFileName, 'r') as f:
    htmlpage=f.read()
# parse the whole page
soupObj = BeautifulSoup(htmlpage, "lxml")
# read submission table
table = soupObj.find("table", attrs={"class":"ct_table"})
# get headings
headings = [th.get_text() for th in table.find("tr").find_all("th")]
# Get indexes for relevant columns
subnridx = headings.index("#")
authorsidx = headings.index("Authors")
titleidx = headings.index("Title")
# get data row by row
for row in table.find_all("tr")[1:]:
    elements = [td.get_text() for td in row.find_all("td")]
    title = elements[titleidx]
    authors = elements[authorsidx].replace(" and", ",")
    fileBaseName = pdfBaseName+elements[subnridx]
    print("\includepaper{"+title+"}{"+authors+"}{"+fileBaseName+"}")
