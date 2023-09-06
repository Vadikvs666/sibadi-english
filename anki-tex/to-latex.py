import csv
import pathlib
from urllib import request, error
import argparse
import datetime
import sys
import time
import logging

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
parser.add_argument("--destfile", required=False, help="Файл с карточками ",default="Выделенные записи.txt")
parser.add_argument("--tab", required=False, help="Символ разделить ", default="\t")
parser.add_argument("--texfile", required=False, help="Файл tex ", default="glossary.tex")
args = parser.parse_args()

logger.info("Старт работы скрипта...")
logger.info("Файл с карточками - "+args.destfile)
logger.info("Символ табуляции - "+args.tab)

def createTex(dest_file,delimiter,file_tex):
    logger.info("Создание файла tex..."+ file_tex)
    with open(file_tex, 'w') as f:
        f.writelines(create_gloss_tex_head())
        with open(dest_file, newline='') as csvfile:
            reader = csv.reader(csvfile,delimiter=delimiter)
            for row in reader:
                if row.extend:
                    if 1 < len(row):
                        f.writelines(create_glossary_entry(row[0].title(),row[1]))
        f.writelines(create_gloss_tex_end())

def create_glossary_entry(name,description):
    lines = list()
    lines.append("\t\\item["+name+"]"+description+"\n") 
    return lines

def create_gloss_tex_head():
    lines = list()
    lines.append("\\documentclass[12pt]{article}\n") 
    lines.append("\\usepackage[T1,T2A]{fontenc}\n") 
    lines.append("\\usepackage[utf8]{inputenc}\n") 
    lines.append("\\usepackage[english,russian]{babel}\n") 
    lines.append("\\usepackage[a4paper,left=2.5cm, right=1.5cm, top=2.0cm, bottom=2.0cm]{geometry}\n") 
    lines.append("\\usepackage{listings}\n") 
    lines.append("\\begin{document}\n") 
    lines.append("\\section*{Глоссарий}\n") 
    lines.append("\\begin{description}\n") 
    return lines

def create_gloss_tex_end():
    lines = list()
    lines.append("\\end{description}\n")
    lines.append("\\end{document}\n")
    return lines



if pathlib.Path(args.destfile).is_file:
        try:
            logger.info("Обработка файла : " + pathlib.Path(args.destfile).__str__())
            createTex(args.destfile,args.tab,args.texfile)
        except OSError as er1:
            logger.error(
                "Ошибка обработки файла" + pathlib.Path(args.destfile).__str__())
            sys.exit(1)




    