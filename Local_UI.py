import tkinter as tk
from tkinter import ttk

from Skid_Tag_Imposition import generate_pdf

def submit():
    docket_number = docket_entry.get()
    customer_name = customer_entry.get()
    description = description_entry.get()
    form_number = form_entry.get()
    number_of_tags = int(tag_entry.get())
    section_info = section_entry.get()

    generate_pdf(docket_number, customer_name, description, number_of_tags, form_number, section_info)

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
tag_label = ttk.Label(frame, text="Number Of Tags:")
tag_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)

tag_entry = ttk.Entry(frame)
tag_entry.grid(column=1, row=4, sticky=(tk.W, tk.E), padx=5, pady=5)

# Add a label and entry for the section parameter
section_label = ttk.Label(frame, text="Section Info:")
section_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)

section_entry = ttk.Entry(frame)
section_entry.grid(column=1, row=5, sticky=(tk.W, tk.E), padx=5, pady=5)

# Add a button to trigger PDF generation
generate_button = ttk.Button(frame, text="Generate PDF", command=submit)
generate_button.grid(column=0, row=6, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
