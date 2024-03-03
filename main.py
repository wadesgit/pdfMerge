import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger

# Function to merge two PDFs
def merge_two_pdfs(pdf_1, pdf_2):
    merger = PdfMerger()
    merger.append(pdf_1)
    merger.append(pdf_2)
    merger.write("merged_pdf.pdf")
    merger.close()

# Function to open the file dialog and select the PDFs
def open_file_dialogs():
    root = tk.Tk()   # Creates a Tkinter application window.
    root.withdraw()  # Hide the main window

    pdf_1 = filedialog.askopenfilename(title="Select First PDF File", filetypes=[("PDF Files", "*.pdf")])
    pdf_2 = filedialog.askopenfilename(title="Select Second PDF File", filetypes=[("PDF Files", "*.pdf")])

    if pdf_1 and pdf_2:
        merge_two_pdfs(pdf_1, pdf_2)
        print("PDF files merged successfully!")

# Call the function to open file dialogs
open_file_dialogs()