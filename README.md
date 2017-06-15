LaTeXProceedings
================
LaTeX class files and tools used to generate proceedings for the AVSP 2011 conference from the EasyChair data

Copyright 2011-2017, Giampiero Salvi, <giampi@kth.se>

This is a set of LaTeX files I created in order to generate the AVSP 2011
Proceedings from the data downloaded from EasyChair. I upload it here in
case it may be useful again. With small modifications, these files can be
used in general to create proceedings when a pdf file is available for each
paper, and a list of titles and authors of the paper is available.

Proceedings created using LaTeXProceedings (that I know of):
* AVSP 2011
* ISADEPT 2012
* GLU 2017

Features:
---------
* title front and back page
* table of contents with links to each paper
* list of authors with links to each paper (using authorindex)
* makes sure papers begin on the right page so that they can be easily printed
* optional offset can be defined for each input PDF to trim the margins
  (PDFs may be generated by different typesetting systems)

The hyperlinks can be suppressed for the printed version (see difference
between `avsp2011_proc_print.tex` and `avsp2011_proc_usb.tex` in `examples/avsp2011`)

Instructions:
-------------
1. Check the examples under examples/avsp2011
2. create the file papers.tex with an `\includepaper` command for each paper you
   wish to include in the proceedings.
   The command takes three arguments: title, authors and PDF file base name of
   the article.
   You may use the `EasyChair2PaperList.py` script to extract this information
   automatically from the http://www.easychair.org List of Submission page. Read
   the instructions inside the script for more information
3. modify title, date and relevant information in main.tex. You might want to
   modify also the text in avsp.cls where we give copyright information.
4. modify abstract for keynote speakers, or if you have PDF files for their
   contribution, include them with the same \includepapers command
5. run make (tested on Linux), this will create two PDF files, one for printing
   and one for the electronic version of the proceedings

NOTE: all the PDF files submitted to AVSP2011 have been substituted with a
      single PDF file to simplify distributing the code. This makes it possible
      to compile the code, but the resulting proceedings will be a bit boring.

If you run an integrated LaTeX evniroment, and can not use make, check in the
file Makefile the list of commands needed to generate the proceedings.

Hope this is useful to researchers, comments and improvements apprechiated
