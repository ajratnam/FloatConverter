import os.path
from struct import unpack as convert
import sys, pandas as pd

encode = bytes.fromhex
hex_to_double = lambda hex: convert('!d', encode(hex))[0]

if len(sys.argv) < 2:
    print("Please run this program with a file....")
    input("Press any key to exit....")
    exit()

data = pd.read_csv(sys.argv[1])
hexadecimal_values = data.iloc[:, 0]

for index, hex_value in enumerate(hexadecimal_values):
    data.iat[index, 0] = hex_to_double(hex_value)

file_path, extension = os.path.splitext(sys.argv[1])
data.to_csv(f"{file_path}_converted.{extension}")
