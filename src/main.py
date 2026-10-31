from pathlib import Path
from shutil import rmtree

from src.sources.asak_historical import AsakHistoricalSource

out_parent_dir = Path('../build')

sources = [
    AsakHistoricalSource(out_parent_dir, internal_id='asak_historical_longest', table_summary='Spisak najduzih'),
    AsakHistoricalSource(out_parent_dir, internal_id='asak_historical_deepest', table_summary='Spisak najdubljih')
]

if out_parent_dir.exists():
    rmtree(out_parent_dir)

for source in sources:
    source.load()
