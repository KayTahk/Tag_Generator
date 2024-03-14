import tkinter as tk
from tkinter import ttk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import utils

# PDF Generation Code

def generate_pdf():
    docket_number = docket_entry.get()
    customer_name = customer_entry.get()
    description = description_entry.get()
    form_number = form_entry.get()
    tag_number = tag_entry.get()
    section_info = section_entry.get()

    # Number of skid tags
    num_tags = 2
    
    # PDF Name
    pdf_filename = f"{docket_number}_{customer_name}_skid_tag.pdf"
    
    # PDF file Size
    pdf = canvas.Canvas(pdf_filename, pagesize=letter)
    
    # Set initial font and size
    pdf.setFont("Helvetica", 12)

    # Loop to duplicate pages according to number of skid tags required
    for _ in range(num_tags):

        # Add Logo
        image_path = 'Mi5_Logo.png'
        img = utils.ImageReader(image_path)
        pdf.drawImage(img, 193, 530, width=225, height=41)

        # Draw lines
        pdf.setLineWidth(2)
        pdf.line(601, 11, 601, 580) # Vertical
        pdf.line(11, 11, 11, 580)
        pdf.line(11, 11, 601, 11) # Horizontal
        pdf.line(11, 580, 601, 580)
        pdf.line(11, 520, 601, 520)
        pdf.line(11, 460, 601, 460)
        pdf.line(11, 415, 601, 415)
        pdf.line(11, 370, 601, 370)

        # Draw text for Docket
        pdf.setFont("Helvetica-Bold", 48)
        pdf.drawString(25, 475, f"Docket: {docket_number}")

        # Draw text for Customer
        pdf.setFont("Helvetica", 36)
        pdf.drawString(25, 425, f"Customer: {customer_name}")

        # Draw text for Description
        pdf.setFont("Helvetica", 16)
        pdf.drawString(25, 400, f"Description: {description}")
        
        # Move to the next page if not the last iteration
        if _ < num_tags - 1:
            pdf.showPage()

            
    pdf.save()
    
    print(f"PDF generated: {pdf_filename}")

# UI Code

# Create the main window
root = tk.Tk()
root.title("PDF Generator")

# Create and pack a frame
frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Add a label and entry for the docket parameter
docket_label = ttk.Label(frame, text="Docket:")
docket_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

docket_entry = ttk.Entry(frame)
docket_entry.grid(column=1, row=0, sticky=(tk.W, tk.E), padx=5, pady=5)

# Add a label and entry for the customer parameter
customer_label = ttk.Label(frame, text="Customer:")
customer_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

customer_entry = ttk.Entry(frame)
customer_entry.grid(column=1, row=1, sticky=(tk.W, tk.E), padx=5, pady=5)

# Add a label and entry for the description parameter
description_label = ttk.Label(frame, text="Description:")
description_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

description_entry = ttk.Entry(frame)
description_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=5, pady=5)

# Add a label and entry for the form parameter
form_label = ttk.Label(frame, text="Form Number:")
form_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

form_entry = ttk.Entry(frame)
form_entry.grid(column=1, row=3, sticky=(tk.W, tk.E), padx=5, pady=5)

# Add a label and entry for the tag parameter
tag_label = ttk.Label(frame, text="Tag Number:")
tag_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)

tag_entry = ttk.Entry(frame)
tag_entry.grid(column=1, row=4, sticky=(tk.W, tk.E), padx=5, pady=5)

# Add a label and entry for the section parameter
section_label = ttk.Label(frame, text="Section Info:")
section_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)

section_entry = ttk.Entry(frame)
section_entry.grid(column=1, row=5, sticky=(tk.W, tk.E), padx=5, pady=5)

# Add a button to trigger PDF generation
generate_button = ttk.Button(frame, text="Generate PDF", command=generate_pdf)
generate_button.grid(column=0, row=6, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()

