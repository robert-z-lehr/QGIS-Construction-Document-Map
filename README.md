# [QDIS-Construction-Document-Map](https://robert-z-lehr.github.io/QGIS-Construction-Document-Map/)
Script to generate a map tile layer of construction documents

### High-level Overview of Workflow

1. **PDF Preprocessing**:
    - Extract the map portion from the PDF files.

2. **Convert to Geo-Referenced Images**:
    - Convert the map portion to a geo-referenced image (like GeoTIFF).

3. **QGIS Import**:
    - Import the geo-referenced image to QGIS and add OpenStreetMap (OSM) or a Leaflet layer as a base layer.

4. **Embed Data in Pop-ups**:
    - Add attribute data and set up pop-up configurations within QGIS.

5. **Export as Web Map**:
    - Export the map from QGIS to HTML, JavaScript, and CSS files.

6. **Github Pages Deployment**:
    - Push the files to a GitHub repository and enable GitHub Pages.

### File Structure

Here's what your GitHub repository might look like:

```
|-- your_project/
|---- source_documents/
|------------ pdf/
|---------------- construction_doc1.pdf
|---------------- construction_doc2.pdf
|---- assets/
|-------- geo-tiff-files/
|------------ map1.tif
|------------ map2.tif
|---- css/
|-------- styles.css
|---- js/
|-------- main.js
|-------- package.json
|---- python/
|-------- pdf_manipulation.py
|-------- requirements.txt
|---- index.html
|---- README.md
```

### Technical Steps

#### Step 1: PDF Preprocessing

1. Open the PDFs and crop out the map area manually using a tool like Adobe Acrobat or an open-source PDF editor.

#### Step 2: Convert to Geo-Referenced Images

1. Convert the cropped PDF to an image (PNG, JPG).
2. Use GDAL or a similar tool to convert it to a geo-referenced image format like GeoTIFF.

#### Step 3: QGIS Import

1. Open QGIS.
2. Import the GeoTIFF images as layers.
3. Add a base layer using OSM or a Leaflet layer.

#### Step 4: Embed Data in Pop-ups

1. In QGIS, use the attribute table to attach the relevant information.
2. Configure the layer properties to show this data in pop-ups.

#### Step 5: Export as Web Map

1. Use the QGIS plugin "qgis2web" to export the map as a web map, including HTML, JavaScript, and CSS files.

#### Step 6: GitHub Pages Deployment

1. Initialize a GitHub repository.
2. Push all the exported files to this GitHub repository.
3. Enable GitHub Pages from the repository settings.

That should give you a proof of concept with all the functionalities you've described. Feel free to ask for further details on any of these steps.


Certainly. The PDF Preprocessing step can be done in multiple ways. I'll give you two approaches: one using Python with the `PyPDF2` and `pdf2image` libraries, and another using an open-source PDF editor.

### Method 1: Using Python Libraries

**Pre-requisites**: 
- Install Python and pip if not already installed.
- Install `PyPDF2` for PDF manipulation and `pdf2image` for PDF to image conversion.

    ```bash
    pip install PyPDF2 pdf2image
    ```

**Steps**:

1. **Read the PDF File**

    ```python
    import PyPDF2

    with open("your_pdf_file.pdf", "rb") as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        total_pages = pdf_reader.numPages
    ```

2. **Extract Specific Pages**

    If your map is on specific pages, you can create a new PDF containing only those pages.

    ```python
    pdf_writer = PyPDF2.PdfWriter()
    for page_num in [5, 6]:  # Assuming maps are on page 6 and 7
        page = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page)
        
    with open("cropped_pdf.pdf", "wb") as out_pdf:
        pdf_writer.write(out_pdf)
    ```

3. **Convert PDF Pages to Images**

    ```python
    from pdf2image import convert_from_path

    images = convert_from_path("cropped_pdf.pdf")
    for i, image in enumerate(images):
        image.save(f"page_{i + 1}.png", "PNG")
    ```

### Method 2: Using Open-Source PDF Editor

**Software Option**: PDFsam (PDF Split and Merge)

1. **Download and Install**: Download PDFsam from its [official website](https://pdfsam.org/download-pdfsam-basic/).

2. **Open the Software**: Launch PDFsam and choose the "Split" or "Extract pages" option.

3. **Select PDF**: Browse and select the PDF file you want to manipulate.

4. **Define Pages**: Specify which pages you want to extract (the ones containing the map).

5. **Execute**: Click “Run” to extract the pages.

6. **Export as Image**: You can then use another software like GIMP to convert the PDF pages to images (PNG, JPG).

You can then proceed to the next step, which involves converting these images to GeoTIFF format. Would you like to know more about that?

## Dependencies

### JavaScript

- Leaflet 1.7.1 [Website](https://leafletjs.com/)

Run `npm install` to install all JavaScript dependencies.

### Python

- PyPDF2 1.26.0
- pdf2image 1.16.0

Run `pip install -r requirements.txt` to install all Python dependencies.

### Open-Source Apps

- [PDFsam](https://pdfsam.org/)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.
