from pathlib import Path

from pandas import DataFrame

from src.common import HtmlPageLoader
from src.sources.source import DataSource


class AsakHistoricalSource(DataSource):
    def __init__(self, out_parent_dir: Path, internal_id: str, table_summary: str):
        super().__init__(out_parent_dir, internal_id)
        self.table_summary = table_summary
        self.html_loader = HtmlPageLoader('https://asak.org.rs/caves/srbdeeplong_e.php')

    def load_raw_df(self) -> DataFrame:
        table = self.html_loader.load().select_one(f'table[summary="{self.table_summary}"]')
        if table is None:
            raise ValueError('Could not find table element')
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
        return DataFrame(rows, columns=headers)[["Name", "Length", "Depth", "Notes"]].fillna('')

