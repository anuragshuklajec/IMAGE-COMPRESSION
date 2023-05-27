from convert import ConvertToBinary
from compression import AlgorithmBuilding
from upload import UploadFileToDrive
from add_noise import AddNoise
import numpy as np
import pandas as pd
import csv
import json

path = r"C:\Users\Asus\OneDrive\Desktop\Major\Assets\test5.tiff"

# convertion
convert = ConvertToBinary(path)
binary = convert.showConvertion()

algo = AlgorithmBuilding(binary)
compressed_image, compression_ratio = algo.runAlgorithm()
print(compression_ratio)


# Convert matrix in json format
json_object = json.dumps(compressed_image)

# create file
with open("compressed.json", "w") as file:
    file.write(json_object)
    file.close()



# uploading to drive
upload = UploadFileToDrive()
boole = upload.uploadFile()
print(boole)


 


