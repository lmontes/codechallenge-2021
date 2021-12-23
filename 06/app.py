# pip install babel pandas

import sys
import pandas as pd
from datetime import date
from babel.dates import format_date

dates = [
    date(2021, 12,  6),
    date(2021, 12,  7),
    date(2021, 12,  8),
    date(2021, 12,  9),
    date(2021, 12, 10),
    date(2021, 12, 11),
    date(2021, 12, 12),
]

# http://babel.pocoo.org/en/latest/index.html

WEEKDAYS = {}

for lang in ["cs_CZ", "da_DK", "el_GR","CA","DE","EN","ES","FI","FR","IS","HU","IT","NL","VI","PL","RO","RU","SE","SI","SK"]:
    days = []
    for d in dates:
        wday = format_date(d, "EEEE", locale=lang).lower()
        days.append(wday)
    WEEKDAYS[lang.split("_")[-1]] = days

# print(WEEKDAYS)

# https://en.wiktionary.org/wiki/Appendix:Days_of_the_week
WEEKDAYS["FI"] = ["maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai"]
WEEKDAYS["SE"] = ["måndag", "tisdag", "onsdag", "torsdag", "fredag", "lördag", "söndag"]
WEEKDAYS["RO"] = ["luni", "marţi", "miercuri", "joi", "vineri", "sâmbătă", "duminică"]
WEEKDAYS["DK"] = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"]
WEEKDAYS["SI"] = ["ponedeljek", "torek", "sreda", "četrtek", "petek", "sobota", "nedelja"]


def translate_day(lang, n):
    if lang not in WEEKDAYS:
        return "INVALID_LANGUAGE"
    if n < 0 or n >= len(WEEKDAYS[lang]):
        return "INVALID_DATE"
    return WEEKDAYS[lang][n].lower()


N = int(sys.stdin.readline())

for i in range(0, N):
    line = sys.stdin.readline().replace("\n", "")

    date_str, lang = line.split(":")

    try:
        dt = pd.to_datetime(date_str, dayfirst=True)
        result = translate_day(lang, dt.weekday())
        wday = dt.weekday()
    except:
        result = "INVALID_DATE"
        wday = None
    
    print(f"Case #{i+1}: {result}")
