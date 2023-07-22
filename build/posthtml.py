from os import walk
import subprocess as sp
import pathlib
from pathlib import Path

output_dir = Path('./public/')
output_dir.mkdir(exist_ok=True)
input_dir = 'html/pages/'
for dirpath, _, filenames in walk(input_dir):
    rel_path = Path('./public/' + dirpath.replace(input_dir, ''))
    rel_path.mkdir(exist_ok=True)
    for filename in filenames:
        input_file = str(Path(dirpath) / filename)
        print(input_file)
        print(rel_path)
        try:
            sp.run(["posthtml", input_file, "-o", rel_path, "-c", "posthtml.json"], shell=True)
        except sp.CalledProcessError as e:
            print(e.output)
