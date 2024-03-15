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
    
    # Set initial font and size
    pdf.setFont("Helvetica", 12)

    # Add Logo
    image_path = 'Mi5_Logo.png'
    img = utils.ImageReader(image_path)
    pdf.drawImage(img, 193, 530, width=225, height=41)

    # Draw lines
    pdf.setLineWidth(2)
    pdf.line(601, 11, 601, 580) # Vertical
    pdf.line(11, 11, 11, 580)
    pdf.line(301, 370, 301, 325)
    pdf.line(301, 295, 301, 260)
    pdf.line(11, 11, 601, 11) # Horizontal
    pdf.line(11, 580, 601, 580)
    pdf.line(11, 520, 601, 520)
    pdf.line(11, 460, 601, 460)
    pdf.line(11, 415, 601, 415)
    pdf.line(11, 370, 601, 370)
    pdf.line(11, 325, 601, 325)
    pdf.line(11, 325, 601, 325)
    pdf.line(11, 295, 601, 295)
    pdf.line(11, 260, 601, 260)
    pdf.line(11, 110, 601, 110)

    # Draw text for Docket
    pdf.setFont("Helvetica-Bold", 48)
    pdf.drawString(25, 475, f"Docket: {docket_number}")

    # Draw text for Customer
    pdf.setFont("Helvetica", 36)
    pdf.drawString(25, 425, f"Customer: {customer_name}")

    # Draw text for Description
    pdf.drawString(25, 380, f"Description:")
    
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

    # Draw text for Form
    pdf.setFont("Helvetica", 36)
    pdf.drawString(25, 335, f"Form # {form_number}")

    # Draw text for Section Info
    pdf.setFont("Helvetica", 16)
    pdf.drawString(25, 305, f"Section Info: {section_info}")

    # Draw text for Initials:
    pdf.drawString(25, 270, f"Print Operator Initials:")

    # Draw text for Date
    pdf.setFont("Helvetica", 15)
    pdf.drawString(315, 270, f"Date:")

    # Draw text for Process Sequence
    pdf.setFont("Helvetica-Bold", 32)
    pdf.drawString(80, 230, f"Production Process Sequence")

    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(150, 215, f"Operators MUST Initial the Symbol of any Task Completed.")

    # Draw text for Notes
    pdf.setFont("Helvetica-Bold", 33)
    pdf.drawString(25, 50, f"Notes:")

    # Add Color Codes
    image_path = 'Mi5_Logo.png'
    img = utils.ImageReader(image_path)
    pdf.drawImage(img, 193, 530, width=225, height=41)


    for number in range(number_of_tags):

        # Draw text for Tag#
        pdf.setFont("Helvetica", 15)
        pdf.drawString(315, 343, f"Tag# {number + 1}")
        
        # Move to the next page if not the last iteration
        if number < number_of_tags - 1:
            pdf.showPage()

            
    pdf.save()
    
    print(f"PDF generated: {pdf_filename}")
