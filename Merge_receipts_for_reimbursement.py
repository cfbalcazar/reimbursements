#====================================================================
# Packages
import os
from PyPDF2 import PdfMerger, PdfFileReader, PdfFileWriter
from PIL import Image 

# ====================================================================
# Path - the py-file should go where your folder with the receipts is
path = os.path.dirname(__file__)

#====================================================================
try:
    os.remove(path+'photo_receipts.pdf')
except:
    pass
# Convert images to pdf
img = os.listdir(path)

images = [Image.open(path + f) for f in os.listdir(path) if f.endswith('.jpg')]

pdf_path = path+'photo_receipts.pdf'
    
images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)
#====================================================================
try:
    os.remove(path+'ridshare_receipts.pdf')
except:
    pass
# Clean rideshare receipts
rideshare = [f for f in os.listdir(path) if 'Uber' in f]

# To help tabula we need to create a subsetted pdf
writer = PdfFileWriter()
for receipt in rideshare:
    try:
        reader = PdfFileReader(path+receipt)
        writer.add_page(reader.pages[0])
    except:
        pass
    
# Saving the extracted pages with the table
with open(path+"ridshare_receipts.pdf", 'wb') as output:
    writer.write(output)

#====================================================================
try:
    os.remove(path+'merged_receipts.pdf')
except:
    pass
# Mergining all Pdfs
merger = PdfMerger()
pdfs = [f for f in os.listdir(path) if f.endswith('.pdf') and 'Uber' not in f]

for pdf in pdfs:
    merger.append(path+pdf)

merger.write(path+'merged_receipts.pdf')
merger.close()


