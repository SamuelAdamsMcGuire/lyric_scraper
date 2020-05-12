## Lyrics Scrape/Recognition

This program broken down into 5 parts. Finds the link for a band/musician on [www.lyrics.com](https://www.lyrics.com), scrapes the lyrics, compiles all artists of your choosing, trains a machine learning classification model and then implements the model with a bash user interface. The user can enter actual lyrics or any lyrics and the model will 'guess' which artist the lyrics are from or could be from.  

## Installation

clone the repository

## Usage

```bash
python 1_artist_websearch.py
```
the file 2_webscraper.py requires the output of 1_artist_websearch.py as an arguement, see example:

```bash
python 2_webscraper.py https://www.lyrics.com/artist/Paul-Simon/5433
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)






