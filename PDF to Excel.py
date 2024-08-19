#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import os
import requests
import shutil

# The authentication key (API Key)
API_KEY = "abubakar343@gmail.com_dda4dbca7d7757833349f62d6dab1c19ce70ca9ee2a8fd103e4ddaab35dc9114840cd22d"

# Base URL for PDF.co Web API requests
BASE_URL = "https://api.pdf.co/v1"

# Source PDF file
SourceFile = "Weekly frozen pricing for WE 09-02-23.pdf"
# Comma-separated list of page indices (or ranges) to process. Leave empty for all pages. Example: '0,2-5,7-'.
Pages = ""
# PDF document password. Leave empty for unprotected documents.
Password = ""
# Destination Excel file name
DestinationFile = "result.xlsx"

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


# In[3]:


pip install tabula-py


# In[5]:


import tabula
# Read a PDF File
df = tabula.read_pdf("Weekly frozen pricing for WE 09-02-23.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("Weekly frozen pricing for WE 09-02-23.pdf", "result.csv", output_format="csv", pages='all')


# In[ ]:




