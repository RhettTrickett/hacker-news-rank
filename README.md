# Hacker News Rank

A simple Python 3 script that takes a list of URLs (i.e. website domains) and ranks them by total Hacker News points using the Hacker News Search API. You can pass a list of URLs to the `rank_urls()` function and it will output the urls ranked in order of Hacker News points or pass a list of URLs to the `rank_articles()` function and it will output a rank of all articles and their points for the list of URLs.

## Installation
Ensure you have a Python 3 virtual environment set up. If you have [Virtualenv](https://virtualenv.pypa.io/en/stable/) installed then you can set up a Python 3 virtual environment on your machine by typing the following into the command line:
```
$ virtualenv -p python3 envname
```

This will create a Python 3 virtual environment called **envname** in your command line's current working directory. Next, navigate to `envname/bin` and activate the virtual environment as follows:
```
$ cd envname/bin 
$ source activate
```

Clone or download this repo to `envname/bin`:
```
$ git clone https://github.com/RhettTrickett/hacker-news-rank.git
```

Install the dependencies:
```
$ pip install requirements.txt
```

## How to use
While your virtual environment is active, navigate to `/hacker-news-rank` in your command line and start the Python shell:
```
$ cd hacker-news-rank
$ python
>>>
```

Import `hn_rank`:
```python
>>> import hn_rank
```

Create a list of URLs to search for:
```python
>>> urls = ['https://instagram-engineering.com', 'https://medium.com/netflix-techblog']
```

and then pass that list into the `rank_urls()` or `rank_articles()` functions below.

### rank_urls()
Takes a list of URLs and optionally, a `year` paramater (default is all time) and/or a `filename` parameter to save to (if not provided results will be printed to terminal). The function then returns each of the domains and the total points they've accumulated from submissions on Hacker News in descending order of total points.

**Example:**
```python
>>> hn_rank.rank_urls(urls, year=2017, filename='results.csv')
```

Creates a file called **results.csv**, formatted like this:
```
1256,https://instagram-engineering.com
520,https://medium.com/netflix-techblog
```

### rank_articles()
Takes a list of URLs and optionally, a `year` paramater (default is all time) and/or a `filename` parameter to save to (if not provided results will be printed to terminal). The function will return the article URL and and total points for each Hackers News submission in descending order of total points.

**Example:**
```python
>>> hn_rank.rank_articles(urls, year=2017, filename='results.csv')
```

Outputs a file called **results.csv**, formatted like this:
```
589,https://engineering.instagram.com/react-native-at-instagram-dd828a9a90c7#.88g2rf8hr
375,https://engineering.instagram.com/bringing-wide-color-to-instagram-5a5481802d7d#.44soiw7he
258,https://engineering.instagram.com/dismissing-python-garbage-collection-at-instagram-4dca40b29172
178,https://medium.com/@NetflixTechBlog/developer-experience-lessons-operating-a-serverless-like-platform-at-netflix-part-ii-63a376c28228
146,https://medium.com/netflix-techblog/serving-100-gbps-from-an-open-connect-appliance-cdb51dda3b99
127,https://medium.com/netflix-techblog/artwork-personalization-c589f074ad76
20,https://medium.com/@NetflixTechBlog/introducing-vectorflow-fe10d7f126b8#1
12,https://engineering.instagram.com/bringing-wide-color-to-instagram-5a5481802d7d
...
```


## Extras

I originally wrote this script to rank the urls from the [engineering blogs](https://github.com/kilimchoi/engineering-blogs) repo. If you want to parse these URLs into a list you can use `get_blogs()` in `extra.py`.
```python
>>> from hn_rank.extra import get_blogs
>>> blogs = get_blogs()
```

You can then pass this into `rank_urls()` or `rank_articles()`, like this:
```python
>>> hn_rank.rank_urls(blogs)
```

NOTE: When using the `rank_urls()` and `rank_articles()` functions, a request will be made to the Hacker News Search API for each URL provided. There are approximately 628 URLs in the awesome engineering blogs list and the HN API limit is 10,000 requests per hour.

## TODO
Find a more efficient way of querying the HN Search API.

## Disclaimer
I'm relatively new to Python and wrote this in a few hours. Constructive feedback and contributions are welcome.