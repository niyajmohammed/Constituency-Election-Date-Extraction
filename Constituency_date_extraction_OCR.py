import pandas as pd
import re
from pdf2image import convert_from_path
import pytesseract
import cv2
import numpy as np
from PIL import Image

# Set Tesseract path (Update if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load the PDF and convert pages to images
pdf_path = "C:/User/files.pdf" # replace with your original pdf file path here
images = convert_from_path(pdf_path)

# Function to preprocess the image (Enhances OCR accuracy)
def preprocess_image(img):
    img = np.array(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    processed = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY, 31, 2)  # Adaptive thresholding
    return Image.fromarray(processed)

# Define regex patterns
date_pattern = re.compile(r"(\d{2}-[A-Za-z]+-\d{4})")  # Extracts dates
constituency_pattern = re.compile(r"CONSTITUENCY\s*[:-]\s*(.+)")  # Extracts constituency name

# Storage for extracted data
data = []

# Process each page
for page_num, img in enumerate(images, start=1):
    processed_img = preprocess_image(img)
    text = pytesseract.image_to_string(processed_img, config="--psm 6 --oem 3")
    
    # Extract constituency name
    constituency_match = constituency_pattern.search(text)
    if constituency_match:
        raw_name = constituency_match.group(1).strip()
        constituency_name = re.sub(r"^[^a-zA-Z]+", "", raw_name)  # Remove unwanted characters
    else:
        constituency_name = f"Unknown_{page_num}"

    # Extract dates
    matches = date_pattern.findall(text)
    polling_date = matches[0] if len(matches) > 0 else "Not Found"
    counting_date = matches[1] if len(matches) > 1 else "Not Found"
    result_date = matches[2] if len(matches) > 2 else "Not Found"
    
    data.append([constituency_name, polling_date, counting_date, result_date])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Constituency", "Polling Date", "Counting Date", "Declaration of Result"])

# Save to CSV
output_csv = "C:/Users/election_dates_1.csv" # replace with your output file directory
df.to_csv(output_csv, index=False)

print(f"✅ Extracted dates saved to: {output_csv}")