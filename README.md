# csv-translate

### This project allows you to create a CSV file with any supported languages in the header and convert english text to each language with google translate automatically

---

## Setup

You'll need to have python 3 installed, as well as pip.

Install all requirements

```
pip install -r requirements.txt
```

## CSV File Input

Create a new csv file in google sheets -> file -> download -> 'Comma-separated values'

The top row should be header values for what languages to translate, e.g.

```input.csv```
```
en,fr,ja,ko
I new recipe has been included on your menu!,,,
A mashmallow twist!,,,
A pastry is burning!,,,
```

Valid language codes are listed here:

https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages



## Usage
```python translate.py input_file.csv output_file.csv```