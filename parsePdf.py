from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal

document = open('pdf.pdf', 'rb')
#Create resource manager
rsrcmgr = PDFResourceManager()
# Set parameters for analysis.
laparams = LAParams()
# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
for page in PDFPage.get_pages(document):
    interpreter.process_page(page)
    # receive the LTPage object for the page.
    layout = device.get_result()
    x0 = y0 = x1 = y1 = 0
    tableColumns = []
    for element in layout:
        if isinstance(element, LTTextBoxHorizontal):
            #print(x0, y0, x1, y1)
            if(y0==element.bbox[1] and y1==element.bbox[3]):
                if(len(tableColumns)==0):
                    tableColumns.append(x0)
                tableColumns.append(element.bbox[0])

            elif(x0 not in tableColumns):
                if(len(tableColumns)!=0):
                    tableColumns.clear()
                print('>>>>',element.bbox[0], element.bbox[1])
                print('->',element.get_text())    
            x0,y0,x1,y1=element.bbox        
            
