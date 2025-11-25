from pathlib import Path, PosixPath
import argparse
import subprocess
import re
import yaml

import config


class PyRedact():

    def __init__(self):
        args = self.parse_args()
        self.old_file: PosixPath = Path(args.filename)
        self.new_file: PosixPath = self.old_file.parent / f'REDACTED_{self.old_file.name}'
        self.replacements = []

        if args.personal_info_file is not None:
            personal_info_file: PosixPath = Path('.') / args.personal_info_file
        else:
            personal_info_file: PosixPath = Path.home() / config.personal_info_file

        if not personal_info_file.exists():
            raise FileNotFoundError(
                f'Error: Personal Info file not found at: {personal_info_file.absolute()}'
                )

        with personal_info_file.open() as f:
            data = yaml.safe_load(f)
            self.replacements = [tuple(pair) for pair in data]
        
    def redact(self):
        text = self.old_file.read_text()
        for pair in self.replacements:
            text = re.sub(pair[0], f'[{pair[1]}]', text, flags=re.IGNORECASE)
        self.new_file.write_text(text)

    def diff(self):
        dwdiff = subprocess.Popen(
            ['dwdiff', f'{self.old_file}', f'{self.new_file}'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            )
        colordiff = subprocess.Popen(
            ['colordiff'],
            stdin=dwdiff.stdout,
        )

    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('filename')
        parser.add_argument('-pi', '--personal_info_file')

        return parser.parse_args()