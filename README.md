# PDF Merger

## Description
This Python script allows you to merge multiple PDF files into a single PDF document. You can either save the merged PDF as a new file or append it to an existing one.

## Requirements
- Python 3.x
- `PyPDF2` library for PDF handling
- `tkinter` for the graphical file dialog

## Setup

1. **Install Python**:
   If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**:
   - To install the required libraries, run:
     ```bash
     pip install PyPDF2
     ```

   - `tkinter` is generally included with Python, so you shouldn’t need to install it separately.

3. **Download or Clone the Repository**:
   - Clone the repo:
     ```bash
     git clone https://github.com/your-username/pdf-merger.git
     ```
   - Or download the ZIP file from the repository and extract it.

## Usage

1. **Run the Script**:
   - In your terminal or command prompt, navigate to the folder where the script is located and run:
     ```bash
     python pdf_merger.py
     ```

2. **Select PDF Files**:
   - A file dialog will appear, allowing you to select multiple PDF files that you want to combine.

3. **Save the Merged PDF**:
   - After selecting the files, you will be asked if you want to save the merged PDF as a new file or append it to an existing file.
     - Choose **1** to save as a new file.
     - Choose **2** to append to an existing file.

4. **Completion**:
   - The script will merge the PDFs and save the combined PDF to the specified location.

## Example

- Run the script, select PDFs, and choose where to save the merged output.
- Example terminal interaction:
  ```bash
  Welcome to the PDF Merger!
  You can select multiple PDF files to combine into one.
  Where do you want to save the merged PDF?
  1. Save as a new file
  2. Append to an existing file
  Enter your choice (1 or 2): 1
  PDFs combined successfully! Saved as /path/to/output/merged.pdf
