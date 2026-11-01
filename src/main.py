from pathlib import Path
from shutil import rmtree

from src.sources.asak_historical import AsakHistoricalSource

out_parent_dir = Path(__file__).parent.parent.resolve() / 'build'

sources = [
    AsakHistoricalSource(out_parent_dir, internal_id='asak_historical_longest', table_summary='Spisak najduzih'),
    AsakHistoricalSource(out_parent_dir, internal_id='asak_historical_deepest', table_summary='Spisak najdubljih')
]

if out_parent_dir.exists():
    print(f'Removing output directory: {out_parent_dir}')
    rmtree(out_parent_dir)
    print('Output directory is removed')

for source in sources:
    print(f'Source: {source.internal_id}')
    source.load()
