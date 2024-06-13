# logos.py

This script generates the logos for the Hugo WebStack theme.It's not perfect, it just helped me go faster, so maybe I'll rework it.

Images go directly into the `themes/hugo-webstack/static/assets/images/logos`.

## Installation


```bash
pip install -r requirements.txt
```

## Usage

In `themes/hugo-webstack/bin`.

```bash
python logos.py -u https://github.com/tsnaketech
```

And select your icon.

```bash
Choose an icon:

1. https://github.githubassets.com/favicons/favicon.png
2. https://avatars.githubusercontent.com/u/34743212?v=4?s=400
3. https://github.githubassets.com/favicons/favicon.svg
4. https://github.com/favicon.ico

0. Exit
```

### Output

If you specify the `--output` to be able to change the name.

```bash
python logos.py -u https://github.com/tsnaketech -o github.ico
```

### Direct download

If you want to download the icon directly.

```bash
python logos.py -d https://github.githubassets.com/favicons/favicon.svg -o github.svg
```

### Help

```plaintext
usage: logos.py [-h] [-d DOWNLOAD] [-u URL] [-o OUTPUT]

Download favicon from a website

options:
  -h, --help            show this help message and exit
  -d DOWNLOAD, --download DOWNLOAD
                        URL for direct download
  -u URL, --url URL     URL of the website
  -o OUTPUT, --output OUTPUT
                        Output file
```