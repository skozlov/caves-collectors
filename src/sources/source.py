from abc import ABC, abstractmethod
from pathlib import Path

from pandas import DataFrame


class DataSource(ABC):
    def __init__(self, out_parent_dir: Path, internal_id: str):
        self.internal_id = internal_id
        self.out_dir = out_parent_dir / internal_id
        self.raw_file = self.out_dir / 'raw.csv'

    def load(self):
        self.out_dir.mkdir(parents=True, exist_ok=True)
        df = self.load_raw_df()
        df.to_csv(self.raw_file, header=True, index=False)

    @abstractmethod
    def load_raw_df(self) -> DataFrame:
        ...
