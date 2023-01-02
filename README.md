**checkout ssl connections of different websites**

## Installation

Install python 3.9.2. Checkout pyenv [installation](https://github.com/pyenv/pyenv-installer)

If you use pyenv:

```bash
pyenv install 3.9.2
#pyenv local 3.9.2
# ->should be set automatically by .python-version
```

Check on python version.

```bash
python --version
```

This should print out 3.9.2

Once you installed python 3.9.2

```bash

pip install poetry

poetry install

```

You can download the ssl certificate of swisscom.ch by running:

```bash
./sslCheck.sh
```

The script can show additional information about the ssl connection by running:

```bash
./sslCheck.sh -i
```

Note: sslCheck.sh works without testssl.sh. The compare functionality can't be used (-c flag) if testssl.sh is not installed.

Install testssl for the "compare" functionality of the script by running:

```bash
sudo apt install testssl.sh
```

You can now compare the security of the ciphers used on the server against the database on [ciphersuite](https://ciphersuite.info/) by running:

```bash
./sslCheck.sh -c
```

To get information as well as a comparison of a custom hostname in verbose mode and save files in custom path run:

```bash
./sslCheck.sh -icvn migros.ch -p ./myCustomPath
```

Make sure the folder myCustomPath exists.

To get more information about the script run:

```bash
./sslCheck.sh -h
```

Or by running the python script directly:

```bash
poetry shell
python main.py --help
```

sslCheck.sh saves the following into the data folder:

- the ssl certificate as a .cert file
- if the flag -i is enabled:
  - a .txt file with the information data
- if the flag -c is enabled:
  - the csv file with the cipher information of the server
  - a .txt file with the comparison data
