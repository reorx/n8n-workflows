import os
import sys
import json
from pathlib import Path


def main():
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    for i in os.scandir(source_dir):
        if not i.is_file():
            continue
        path = Path(i.path)
        if path.suffix != '.json':
            continue
        d = get_workflow(path)
        save_workflow(d, dest_dir)


data_key = 'staticData'


def get_workflow(path):
    with open(path, 'r') as f:
        d = json.loads(f.read())
    # remove data from workflow
    if d.get(data_key):
        for key in d[data_key]:
            d[data_key][key] = {}
    return d


def save_workflow(d, dest_dir):
    filename = f'{d["name"]}.json'
    filepath = Path(dest_dir).joinpath(filename)
    print(f'write {filepath}')
    with open(filepath, 'w') as f:
        f.write(json.dumps(d))


if __name__ == '__main__':
    main()
