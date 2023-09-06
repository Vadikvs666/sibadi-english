import csv
import logging
import pathlib
from urllib import request, error
import argparse
import logging
import datetime
import sys
import time


logger = logging.getLogger("FileLog")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler = logging.FileHandler(datetime.date.today().__str__() + ".log")
handler_sys = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
handler_sys.setFormatter(formatter)
logger.addHandler(handler)
logger.addHandler(handler_sys)
logger.setLevel("INFO")

parser = argparse.ArgumentParser()
parser.add_argument("--dest_file", required=False, help="Файл с карточками ")
parser.add_argument("--tab", required=False, help="Символ разделить ", default="    ")
args = parser.parse_args()

with open('glossary.tex', 'w') as f:
    f.write()
    with open('/home/vadim/Рабочий стол/Выделенные записи.txt', newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter='\t')
        for row in reader:
            if row.extend:
                if 1 < len(row):
                    f.write(row[0]+" "+row[1]+"\n")
    