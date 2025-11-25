
# PyRedact

A tool to redact personal info from text files.

## Instalation

This project uses the python utility `uv` to install two scripts to the user's `$PATH`, the main script `pyredact` and a bash wrapper, `redact`, that simply pipes the output of `pyredact`'s `diff` into `less` for convenience.

Clone the repository with

```
git clone https://github.com/luiztosk/pyredact
```

and install it using

```
uv tool install ./pyredact
```


## Usage

```
usage: pyredact [-h] [-pi PERSONAL_INFO_FILE] filename

positional arguments:
  filename

options:
  -h, --help            show this help message and exit
  -pi, --personal_info_file PERSONAL_INFO_FILE
```


It reads a list of pairs of strings to be replaced, and tags to replace them with, from a file in the user's home directory. The default location is at `~/.config/pyredact/personal_info.yml`.  This can be changed in `config.py`, or by using the command line argument, `-pi [PERSONAL INFO FILE]`.

Typically you would create the dir, then copy the file `sample_files/personal_info.yml` there, and add the info you want redacted. Pay attention to the order, **larger strings** should **come first**, since if you put at the top shorter strings, containing for example only your first name, it would be impossible to replace your full name later.


A required argument is the `filename` for the file being redacted, which can be in relative or absolute paths, or in the current directory.


## Example

When using the sample files provided in the `sample_files` directory, the `personal_info.yml` looks like so:
```
- ["gonzaga_jr_dev", "github username"]
- ["Luiz Gonzaga do Nascimento Júnior", "full name"]
- ["Luiz Gonzaga Jr", "first and last name"]
- ["gonzaguinha@exemplo.com", "email address"]
- ["Luiz", "first name"]
- ["Odaléia Guedes dos Santos", "full mother's name"]
- ["Luiz Gonzaga do Nascimento", "full father's name"]
- ["simples_desejo.dev", "domain name"]
- ["Moleque Doido Inc", "business name"]
- ["Asa Branca Systems", "company name"]
- ["Rio de Janeiro", "city"]
- ["UniPirapora", "university"]
- ["September 22, 1945", "birth date"]
- ["22/09/1945", "birth date"]
```
and we can run `pyredact` by invoking:

```
redact -pi ./sample_files/personal_info.yml ./sample_files/original_text.txt
```

It will write the redacted file, containing the text in `original_text.txt` minus the replacements, into `./sample_files/REDACTED_original_text.txt`. In our terminal, `less` will show a diff with the changes:

![image](sample_files/diff_result.png)