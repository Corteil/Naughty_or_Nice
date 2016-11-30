#!/usr/bin/env python
# Print a file to the printer

import cups
import sys
import pprint
from xhtml2pdf import pisa

pp = pprint.PrettyPrinter(indent=4)

def sticker(nRating):
  # Filename for temp file
  filename = "/home/pi/print.pdf"

  # generate content
  xhtml = "<style>"
  xhtml += "  @page {"
  xhtml += "      size: 88mm 35mm landscape;"
  xhtml += "@frame content_frame {"
  xhtml += "            left: 1;"
  xhtml += "            width: 86mm;"
  xhtml += "            top: 1mm;"
  xhtml += "            height: 33mm;"
#  xhtml += "            vertical-align: middle;"
#  xhtml += "            -pdf-frame-border: 1;    /* for debugging the layout */"

  xhtml += "  }"
  xhtml += "  }"
  xhtml += "p { text-align: left;}"
  xhtml += "h1 { text-align: right;}"
  xhtml += "</style>"
  xhtml += "<p>"
  xhtml += "<img src='/home/pi/demon-H.png' style='width:80px;height:104px;'>"
  # xhtml += "<br>"
  xhtml += "My Naughtiness rating is "
  xhtml += str(nRating)
  xhtml += "%"
  xhtml += "</p>"




  # xhtml += "<pdf:nextpage>"

  pdf = pisa.CreatePDF(xhtml, file(filename, "w"))
  if not pdf.err:
      # Close PDF file - otherwise we can't read it
      pdf.dest.close()



      # print the file using cups
  conn = cups.Connection()
  # Get a list of all printers
  printers = conn.getPrinters()
  print_num = 0
  print_loop = 0
  for printer in printers:
    # Print name of printers to stdout
    # (screen)
    print (printer)


    printer_name = "DYMO450"
    pp.pprint(printer_name)
    conn.printFile(printer_name, filename, "Python_Status_print", {})

if __name__ == '__main__':

  sticker(int(55))
