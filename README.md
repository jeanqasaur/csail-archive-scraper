csail-archive-scraper
=====================

Scraping csail-related archives.

Usage:

```
python scrape.py -e <email> -o <output file> -m <number of months>
```

For example, this gets all the emails from `alice@mail.org` and writes to `alice.txt` the bodies of all the emails for the last three months:

```
python scrape.py -e alice@mail.org -o alice.txt -m 3
```

The default output file is `out.txt` and the default number of months is one.
