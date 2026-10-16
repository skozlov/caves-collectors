from pathlib import Path

import pandas
from bs4 import BeautifulSoup, Tag
from pandas import DataFrame

from src.common import HtmlPageLoader

html_loader = HtmlPageLoader(url='https://asak.org.rs/caves/srbdeeplong_e.php')

html: BeautifulSoup = html_loader.load()

tables = html.select(
    'table[summary="Spisak najduzih"], '
    'table[summary="Spisak najdubljih"]'
)


def parse_table(table: Tag) -> DataFrame:
    headers = [
        th.get_text(" ", strip=True)
        for th in table.select("thead th")
    ]

    rows = [
        [
            cell.get_text(" ", strip=True)
            for cell in row.find_all(["th", "td"], recursive=False)
        ]
        for row in table.select("tbody > tr")
    ]

    return DataFrame(rows, columns=headers)


raw_data = pandas.concat(
    [
        parse_table(table)
        for table in tables
    ],
    ignore_index=True,
)[["Name", "Length", "Depth", "Notes"]].fillna('')

out_dir = Path('../../build/asak_historical')
out_dir.mkdir(parents=True, exist_ok=True)
raw_data.to_csv(out_dir / 'raw.csv', header=True, index=False)
