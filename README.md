# PDF to Excel Conversion using pdf.co API

This project is designed to convert PDF files to Excel format using the pdf.co API. The script automates the process of uploading a PDF file, converting it to an Excel file, and then downloading the converted file.

## Features

- **PDF to Excel Conversion**: Converts PDF files into Excel spreadsheets while preserving the structure and content.
- **API Integration**: Utilizes pdf.co's robust API for seamless PDF processing and conversion.
- **File Handling**: Automatically handles file uploads and downloads from the cloud, ensuring a smooth workflow.

## Files

- `main.py`: The main script responsible for converting PDFs to Excel format using the pdf.co API.

## Dependencies

The following Python libraries are required:

- `pandas`
- `os`
- `requests`
- `shutil`

Install the necessary libraries using:

```bash
pip install pandas requests
```

## Usage

1. **API Key Configuration**: Set your pdf.co API key in the `API_KEY` variable within the script.
2. **Source PDF File**: Specify the path to the PDF file you want to convert by setting the `SourceFile` variable.
3. **Destination File**: Define the name and path for the resulting Excel file by setting the `DestinationFile` variable.
4. **Run the Script**: Execute `main.py` to start the conversion process.

## Notes

- The code was developed with the help of the pdf.co API documentation.
- Ensure your pdf.co API key is valid and that you have sufficient API credits for the conversion process.
- You can customize the pages to be converted by adjusting the `Pages` variable.
