# Simple utility for creating the Cloudinary URL from a
# cloudinary_python.txt file


import re

with open("cloudinary_python.txt") as f:
    content = f.readlines()

cloud_name = re.findall(r"['](.*?)[']",content[15])[0]
api_key = re.findall(r"['](.*?)[']",content[16])[0]
api_secret = re.findall(r"['](.*?)[']",content[17])[0]
