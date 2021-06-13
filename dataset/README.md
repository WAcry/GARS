`anime.csv` `rating.csv` are original dataset

`merged.csv` are left join of original dataset and crawler data for more info about each anime

`parsed_anime.csv` reformat dates in merged.csv



`animelist` directory contains a scrapy spider that scrapes anime data from animelist.net

`scrapy crawl anime -o output.csv -t csv`

