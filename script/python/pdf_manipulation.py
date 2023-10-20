# Debugger
## Commonly used pdb commands:
## n (next): Continue execution until the next line in the current function is reached.
## s (step): Execute the current line and stop at the first possible occasion.
## c (continue): Continue execution until a breakpoint is encountered.
## q (quit): Exit the debugger and terminate the program.
## l (list): Display 11 lines around the current line or continue the previous listing.
## u (up): Move one level up in the stack trace.
## d (down): Move one level down in the stack trace.
## p (print): Evaluate and print the expression.
## pp (pretty-print): Pretty-print the value of the expression.
## w (where): Print a stack trace, with the most recent frame at the bottom.
breakpoint()

# ===================
# Import dependencies
# ===================

from pdf2image import convert_from_path, exceptions
import cv2
import numpy as np

# ======================================
# Declare global constants and variables
# ======================================

# =======================================
# Declare classes, methods, and functions
# =======================================

# ============================
# Main Logic / Execution Block
# ============================
if __name__ == "__main__":
    try:
# Convert PDF to image
        images = convert_from_path('../../source_documents/pdf/construction_document_1.pdf', first_page=1, last_page=1)
    except exceptions.PdfFileDoesNotExist:
        print("Error: PDF file not found.")
        exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading the PDF: {e}")
        exit(1)

    if len(images) == 0:
        print("Error: No images were extracted from the PDF.")
        exit(1)

    image = images[0]

# Convert PIL Image to NumPy array
    image_np = np.array(image)

# Convert to grayscale
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# Use Canny edge detection
    edges = cv2.Canny(gray, 50, 150)

# Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        print("Error: No contours were found.")
        exit(1)

# Sort contours by area and keep the largest one (assuming it's the map)
    sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]

    if len(sorted_contours) == 0:
        print("Error: No sorted contours are available.")
        exit(1)

# Get bounding box for the largest contour
    x, y, w, h = cv2.boundingRect(sorted_contours[0])

# Crop the image
    cropped_map = image_np[y:y + h, x:x + w]

    try:
# Save as PNG
        cv2.imwrite("cropped_map.png", cv2.cvtColor(cropped_map, cv2.COLOR_RGB2BGR))
    except Exception as e:
        print(f"Error: An error occurred while saving the PNG: {e}")
        exit(1)

    print("Cropped map has been successfully saved as 'cropped_map.png'.")
# ==============
# Error Handling
# ==============

# =============
# File Handling
# =============