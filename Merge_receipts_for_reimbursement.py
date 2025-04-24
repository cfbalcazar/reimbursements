#====================================================================
# Packages
import os
from PyPDF2 import PdfMerger, PdfFileReader, PdfFileWriter
from PIL import Image 

# ====================================================================
# Path - the py-file should go where your folder with the receipts is
path = os.path.dirname(__file__) + '/'

#====================================================================
try:
    os.remove(path+'food_receipts.pdf')
except:
    pass
# Convert images to pdf
img = [f for f in os.listdir(path+'food/') if f.endswith('.jpg')]
img = sorted(img)

images = [Image.open(path +'food/' + f) for f in img]

pdf_path = path+'food_receipts.pdf'
    
images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)

#====================================================================
try:
    os.remove(path+'conference_receipts.pdf')
except:
    pass
# Convert images to pdf
conference = [f for f in os.listdir(path + 'conferences/') if f.endswith('.pdf')]
conference = sorted(conference)

# To help tabula we need to create a subsetted pdf
writer = PdfFileWriter()
for receipt in conference:
    try:
        reader = PdfFileReader(path+ 'conferences/'+receipt)
        writer.add_page(reader.pages[0])
    except:
        pass
    
# Saving the extracted pages with the table
with open(path+"conference_receipts.pdf", 'wb') as output:
    writer.write(output)
    
#====================================================================
try:
    os.remove(path+'flights_receipts.pdf')
except:
    pass
# Clean rideshare receipts
flights = [f for f in os.listdir(path+'flights/') if f.endswith('.pdf')]
flights = sorted(flights)

# To help tabula we need to create a subsetted pdf
writer = PdfFileWriter()
for receipt in flights:
    try:
        reader = PdfFileReader(path+'flights/'+receipt)
        for p in range(0,len(reader.pages)-2) :
            writer.add_page(reader.pages[p])
    except:
        pass
    
# Saving the extracted pages with the table
with open(path+"flights_receipts.pdf", 'wb') as output:
    writer.write(output)
#====================================================================
try:
    os.remove(path+'train_receipts.pdf')
except:
    pass
# Clean rideshare receipts
train = [f for f in os.listdir(path+'train/') if 'MTA'  in f or 'Amtrak' in f]
train = sorted(train)

# To help tabula we need to create a subsetted pdf
writer = PdfFileWriter()
for receipt in train:
    try:
        reader = PdfFileReader(path+'train/'+receipt)
        writer.add_page(reader.pages[0])
    except:
        pass
    
# Saving the extracted pages with the table
with open(path+"train_receipts.pdf", 'wb') as output:
    writer.write(output)

#====================================================================
try:
    os.remove(path+'uber_receipts.pdf')
except:
    pass
# Clean rideshare receipts
uber = [f for f in os.listdir(path+'rideshare/') if 'uber' in f]
uber = sorted(uber)

# To help tabula we need to create a subsetted pdf
writer = PdfFileWriter()
for receipt in uber:
    try:
        reader = PdfFileReader(path+ 'rideshare/'+receipt)
        writer.add_page(reader.pages[0])
    except:
        pass
    
# Saving the extracted pages with the table
with open(path+"uber_receipts.pdf", 'wb') as output:
    writer.write(output)

#====================================================================
try:
    os.remove(path+'lyft_receipts.pdf')
except:
    pass
# Clean rideshare receipts
lyft = [f for f in os.listdir(path + 'rideshare/') if 'ride with' in f ]
lyft = sorted(lyft)

# To help tabula we need to create a subsetted pdf
writer = PdfFileWriter()
for receipt in lyft:
    try:
        reader = PdfFileReader(path+'rideshare/'+receipt)
        writer.add_page(reader.pages[0])
    except:
        pass
    
# Saving the extracted pages with the table
with open(path+"lyft_receipts.pdf", 'wb') as output:
    writer.write(output)

#====================================================================
    try:
        os.remove(path+'Bank_statements.pdf')
    except:
        pass
    # Clean rideshare receipts
    boa = [f for f in os.listdir(path+'statements/') if 'eStmt' in f ]
    boa = sorted(boa)

    # To help tabula we need to create a subsetted pdf
    writer = PdfFileWriter()
    for receipt in boa:
        try:
            reader = PdfFileReader(path+'statements/'+receipt)
            for p in range(0,len(reader.pages)-2) :
                writer.add_page(reader.pages[p])
        except:
            pass
        
    # Saving the extracted pages with the table
    with open(path+"Bank_statements.pdf", 'wb') as output:
        writer.write(output)

#====================================================================
try:
    os.remove(path+'merged_receipts.pdf')
except:
    pass
# Mergining all Pdfs
[f for f in os.listdir(path) if f.endswith('.pdf')]
merger = PdfMerger()
pdfs = ['flights_receipts',
        'train_receipts',
        'conference_receipts',
        'food_receipts',
        'uber_receipts',
        'lyft_receipts',
        'Bank_statements'
        ]

for pdf in pdfs:
    merger.append(path+pdf+'.pdf')

merger.write(path+'merged_receipts.pdf')
merger.close()


