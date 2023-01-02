**checkout ssl connections of different websites**

this script ....

## Installation

Install python 3.9.2. Checkout pyenv [installation](https://github.com/pyenv/pyenv-installer)

if you use pyenv:

```bash
pyenv install 3.9.2

#pyenv local 3.9.2
# ->should be set automatically by .python-version

pip install poetry

poetry install

poetry shell
```

once you installed python 3.9.2

```bash

pip install poetry

poetry install

poetry shell
```

You can download the ssl certificate of swisscom.ch by running:

```bash
./sslCheck.sh
```

The script can show additional information about the ssl connection by running:

```bash
./sslCheck.sh -i
```

Install testssl for the "compare" functionality of the script by running:

```bash
sudo apt install testssl.sh
```

you can now compare the security of the ciphers used on the server against the database on [ciphersuite](https://ciphersuite.info/) by running:

```bash
./sslCheck.sh -c
```

to get information as well as a comparison of a custom hostname in verbose mode run:

```bash
./sslCheck.sh -icvn migros.ch
```

to get more information about the script run:

```bash
./sslCheck.sh -h
```

or by running the python script directly:

```bash
python main.py --help
```

this script saves the following into the data folder:

- the ssl certificate as a .cert file
- if the flag -i is enabled:
  - a .txt file with the information data
- if the flag -c is enabled:
  - the csv file with the cipher information of th server
  - a .txt file with the comparison data
