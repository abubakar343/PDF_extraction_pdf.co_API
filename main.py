#!/usr/bin/env python
# coding: utf-8

#import necessary libraries
import pandas as pd
import os
import requests
import shutil

# The authentication key (API Key)
API_KEY = "your_api_key"

# Base URL for PDF.co Web API requests
BASE_URL = "https://api.pdf.co/v1"

# Source PDF file
SourceFile = "your_pdf_file.pdf"
# Comma-separated list of page indices (or ranges) to process. Leave empty for all pages. Example: '0,2-5,7-'.
Pages = ""
# PDF document password. Leave empty for unprotected documents.
Password = ""
# Destination Excel file name
DestinationFile = "excel_file.xlsx"

def main(args=None):
    uploadedFileUrl = uploadFile(SourceFile)
    if uploadedFileUrl is not None:
        convertPdfToExcel(uploadedFileUrl, DestinationFile)

def convertPdfToExcel(uploadedFileUrl, destinationFile):
    """Converts PDF To Excel using PDF.co Web API"""
    parameters = {
        "name": os.path.basename(destinationFile),
        "password": Password,
        "pages": Pages,
        "url": uploadedFileUrl
    }

    url = f"{BASE_URL}/pdf/convert/to/xlsx"

    response = requests.post(url, data=parameters, headers={"x-api-key": API_KEY})

    if response.status_code == 200:
        json = response.json()

        if not json["error"]:
            resultFileUrl = json["url"]
            r = requests.get(resultFileUrl, stream=True)

            if r.status_code == 200:
                with open(destinationFile, 'wb') as file:
                    for chunk in r:
                        file.write(chunk)
                print(f"Result file downloaded as \"{destinationFile}\"")
            else:
                print(f"Request error: {response.status_code} {response.reason}")
        else:
            print(json["message"])
    else:
        print(f"Request error: {response.status_code} {response.reason}")

def uploadFile(fileName):
    """Uploads file to the cloud"""
    url = f"{BASE_URL}/file/upload/get-presigned-url?contenttype=application/octet-stream&name={os.path.basename(fileName)}"

    response = requests.get(url, headers={"x-api-key": API_KEY})

    if response.status_code == 200:
        json = response.json()

        if not json["error"]:
            uploadUrl = json["presignedUrl"]
            uploadedFileUrl = json["url"]

            with open(fileName, 'rb') as file:
                requests.put(uploadUrl, data=file, headers={"x-api-key": API_KEY, "content-type": "application/octet-stream"})

            return uploadedFileUrl
        else:
            print(json["message"])
    else:
        print(f"Request error: {response.status_code} {response.reason}")

    return None

if __name__ == '__main__':
    main()
