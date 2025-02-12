# Constituency-Election-Date-Extraction
This repository contains a Python script to extract election dates (Polling Date, Counting Date, and Declaration of Result) along with constituency names from a PDF file using Optical Character Recognition (OCR).

**Features:**
Converts PDF pages to images, Uses Tesseract OCR for text extraction, Extracts constituency names and election dates using regex, Saves extracted data into a CSV file

**Prerequisites**
Ensure you have the following installed:
-Python 3.x
-Tesseract OCR (Download from this link: "https://github.com/UB-Mannheim/tesseract/wiki"), download file: "tesseract-ocr-w64-setup-5.5.0.20241111.exe (64 bit)"
Download this software and locate it in your "C:\Program Files\Tesseract-OCR\tesseract.exe"

**Required Python libraries:**

pip install pandas pdf2image pytesseract opencv-python numpy pillow

