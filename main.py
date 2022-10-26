import csv
import os
import re
from os.path import isfile, join

file = open('news/news01.txt',encoding='utf-8-sig')
print(file.read())
with open("data.csv","a", encoding="utf-8-sig") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(
        (
            "Index",
            "Title",
            "Lid",
            "Text",
            "Ner",
            "Language",
            "URL",
            "Date"
        )
    )
directory = r'C:\Users\Илья\PycharmProjects\lab4\news'
index = 0
regexp_url = "https[^ ]+"
regexp_year = r'\d{4}-\d{2}-\d{2}|\d{4}\/\d{2}\/\d{2}|\d{2}\/\d{2}\/\d{4}|d{2}-\d{2}-\d{4}|20[0-2][0-9]'
regexp_lang_en = '[A-Za-z]'
regexp_lang_ru = '[А-Яа-яё]'
regexp_names = '[A-ZА-ЯЁ][a-zа-яё]+'
path = r'C:\Users\Илья\PycharmProjects\lab4\news'
for f in os.listdir(path):
  if isfile(join(path, f)):
    filepath = f"{path}/{f}"
    with open(filepath, encoding='utf-8-sig') as fp:
        file = [string for string in fp.read().split('\n') if string != '']
        index += 1
        title = file[0]
        lid = file[2]
        text = '\\n'.join(file[4:])
        language = []
        ner = 0
        url = ''
        date = ''
        if re.search(regexp_lang_ru, text) or re.search(regexp_lang_ru, lid):
            language.append('ru')
        if re.search(regexp_lang_en, text) or re.search(regexp_lang_en, lid):
            language.append('en')
        if re.search(regexp_names, text):
            ner = 1
        lang = '-'.join(language)
        url = re.search(regexp_url, ' '.join(file)).group(0)
        date = re.findall(regexp_year, url)
        if date == []:
            date = None
        # if year != None:
        #     date = year.group(0)[1:]
        with open("data.csv","a" ,encoding='utf-8-sig') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                (
                    index,
                    title,
                    lid,
                    text,
                    ner,
                    language,
                    url,
                    date
                )
            )
print(index)



