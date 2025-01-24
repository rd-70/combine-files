from PyPDF2 import PdfReader, PdfWriter
from tkinter import Tk, filedialog
import os

# Function to merge multiple PDFs into one
def merge_pdfs(pdf_files, output_pdf):
    pdf_writer = PdfWriter()

    # Loop through the selected PDF files
    for pdf_file in pdf_files:
        with open(pdf_file, 'rb') as file:
            pdf_reader = PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

    # Write the combined PDF to the specified file
    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

# Main function to interact with the user
def main():
    print("Welcome to the PDF Merger!")
    print("You can select multiple PDF files to combine into one.")

    # Open a file dialog for the user to select multiple PDF files
    root = Tk()
    root.withdraw()  # Hide the root window
    root.attributes('-topmost', True)  # Ensure dialog is on top
    pdf_files = filedialog.askopenfilenames(
        title="Select PDF Files to Combine",
        filetypes=[("PDF Files", "*.pdf")],
    )

    if not pdf_files or len(pdf_files) < 2:
        print("You need to select at least two PDF files to combine.")
        return

    # Ask the user if they want to save the merged file to a new file or an existing file
    print("\nWhere do you want to save the merged PDF?")
    print("1. Save as a new file")
    print("2. Append to an existing file")
    save_choice = input("Enter your choice (1 or 2): ")

    if save_choice == "1":
        # Save to a new file
        output_pdf = filedialog.asksaveasfilename(
            title="Save Merged PDF As",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
        )
        if not output_pdf:
            print("No output file specified. Exiting...")
            return
    elif save_choice == "2":
        # Append to an existing file
        output_pdf = filedialog.askopenfilename(
            title="Select an Existing PDF File to Append To",
            filetypes=[("PDF Files", "*.pdf")],
        )
        if not output_pdf or not os.path.exists(output_pdf):
            print("No valid file selected. Exiting...")
            return
    else:
        print("Invalid choice. Exiting...")
        return

    # Merge the selected PDFs
    try:
        merge_pdfs(pdf_files, output_pdf)
        print(f"\nPDFs combined successfully! Saved as {output_pdf}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()