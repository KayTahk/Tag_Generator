import tkinter as tk
from tkinter import ttk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import utils
from io import BytesIO

def generate_pdf(docket_number, customer_name, description, number_of_tags, form_number, section_info):

    # PDF Name
    pdf_filename = f"{docket_number}_{customer_name}_skid_tag.pdf"
    
    # PDF file Size
    pdf = canvas.Canvas(pdf_filename, pagesize=letter)
    
    for number in range(number_of_tags):
        # Add Backgound
        image_path = 'background.jpg'
        img = utils.ImageReader(image_path)
        pdf.drawImage(img, 0, 0,width=615, height=795)

        # Add Docket number
        pdf.setFont("Helvetica-Bold", 48)
        pdf.drawString(200, 475, f"{docket_number}")

        # Add Customer Number
        pdf.setFont("Helvetica", 36)
        pdf.drawString(195, 425, f"{customer_name}")
        
        # Split the incoming description into lines
        lines = []
        current_line = ""
        for word in description.split():
            if len(current_line + word) + 1 <= 75: #Last number is the character limit
                current_line += word + " "
            else:
                lines.append(current_line)
                current_line = ""
        lines.append(current_line)
        
        y = 395 # Starting line y cord
        pdf.setFont("Helvetica", 12)
        for line in lines:
            pdf.drawString(215, y, f"{line}")
            y -= 15  # Move to the next line

        # Add Form Number
        pdf.setFont("Helvetica", 36)
        pdf.drawString(140, 335, f"{form_number}")

        # Add Section Info
        pdf.setFont("Helvetica", 16)
        pdf.drawString(115, 305, f"{section_info}")

        # Add Tag Number
        pdf.setFont("Helvetica", 15)
        pdf.drawString(355, 343, f"{number + 1}")
        
        # Move to the next page if not the last iteration
        if number < number_of_tags - 1:
            pdf.showPage()

            
    pdf.save()
    
    print(f"PDF generated: {pdf_filename}")
