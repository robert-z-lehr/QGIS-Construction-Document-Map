if __name__ == "__main__":
    # Start debugger
    breakpoint()
    
    # Import dependencies
    import cv2
    import numpy as np
    import PyPDF2
    from pdf2image import convert_from_path
    
    # Declare global constants and variables

    # Declare classes, methods, and functions

    # Main execution block or main logic
    ## ----------------------------------------------------------
    # Locate Map Boundary
    ## ----------------------------------------------------------
    for i, image in enumerate(images):
        # Convert PIL Image to NumPy array
        image_np = np.array(image)
        
        # Convert to grayscale
        gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
        
        # Use Canny edge detection
        edges = cv2.Canny(gray, 50, 150)
        
        # Find contours
        contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        # Sort contours by area and keep the largest one (assuming it's the map)
        sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]
        
        # Get bounding box for the largest contour
        x, y, w, h = cv2.boundingRect(sorted_contours[0])
        
        # Crop the image
        cropped_map = image_np[y:y+h, x:x+w]
        
        # Save as PNG
        cv2.imwrite(f"cropped_page_{i + 1}.png", cropped_map)

      ## ----------------------------------------------------------
      # Extract PDF pages as images
      ## ----------------------------------------------------------
#     images = convert_from_path("your_pdf_file.pdf", first_page=6, last_page=7)
    
#     ## Read the PDF File
#     with open("your_pdf_file.pdf", "rb") as f:
#         pdf_reader = PyPDF2.PdfFileReader(f)
#         total_pages = pdf_reader.numPages
        
#     ## Extract Specific Pages: If your map is on specific pages, you can create a new PDF containing only those pages.
#     pdf_writer = PyPDF2.PdfWriter()
#     for page_num in [5, 6]:  # Assuming maps are on page 6 and 7
#         page = pdf_reader.getPage(page_num)
#         pdf_writer.addPage(page)
    
#     with open("cropped_pdf.pdf", "wb") as out_pdf:
#         pdf_writer.write(out_pdf)

#     ## Convert PDF Pages to Images
#     from pdf2image import convert_from_path

#     images = convert_from_path("cropped_pdf.pdf")
#     for i, image in enumerate(images):
#         image.save(f"page_{i + 1}.png", "PNG")

    
#     # Error handling and File handling

    ## ----------------------------------------------------------
    # Convert to GeoTIFF using GDAL
    ## ----------------------------------------------------------

    # from osgeo import gdal, osr

    # # Open the image file
    # input_image = "map.png"
    # dataset = gdal.Open(input_image, gdal.GA_ReadOnly)

    # # Create a GeoTIFF file
    # output_file = "map_geotiff.tiff"
    # driver = gdal.GetDriverByName('GTiff')
    # dst_ds = driver.CreateCopy(output_file, dataset, 0)

    # # Define the spatial reference system (WGS84 in this example)
    # srs = osr.SpatialReference()
    # srs.ImportFromEPSG(4326)  # WGS84
    # dst_ds.SetProjection(srs.ExportToWkt())

    # # Define the geotransformation (replace with your own coordinates)
    # # (top left x, w-e pixel resolution, rotation, top left y, rotation, n-s pixel resolution)
    # geotransform = [longitude, 1, 0, latitude, 0, -1]
    # dst_ds.SetGeoTransform(geotransform)

    # # Close files
    # dataset = None
    # dst_ds = None
