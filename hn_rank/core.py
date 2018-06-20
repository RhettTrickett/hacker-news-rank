import requests, json, operator, sys
from datetime import datetime


def rank_urls(urls, year=None, filename=None):
	"""
	Takes a list of URLs and searches for them in 
	Hacker News submissions. Prints or saves each
	URL and its total points to a given filename 
	in descending order of points. Searches for 
	submissions from all years, unless year is given.
	"""
	now = datetime.now()
	if year:
		if year > now.year: 
			print("Please enter a valid year parameter (example: " + str(now.year) + ") or leave out for all time.")
			return None
		else:
			pass

	leaderboard = {}
	count = 0

	for url in urls:
		query = 'http://hn.algolia.com/api/v1/search?query=' + url + '&restrictSearchableAttributes=url'
		r = requests.get(query)
		data = json.loads(r.text)
		total_score = 0

		for item in data['hits']:
			date = item['created_at'][:-5]
			date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
			now = datetime.now()

			if not year:
				total_score += item['points']
			elif date.year != year:
				pass
			else:
				total_score += item['points']

		count += 1
		progress = (count / len(urls) ) * 100.00
		sys.stdout.write(" Progress: %d%%   \r" % (progress) )
		sys.stdout.flush()

		leaderboard[url] = total_score
	sorted_leaderboard = reversed(sorted(leaderboard.items(), key=operator.itemgetter(1)))

	if filename:
		f = open(filename, 'w')
		for key, value in sorted_leaderboard:
			f.write(str(value) + "," + key + '\n')
		f.close()
		print('Results saved to ' + filename)	
	else:
		for key, value in sorted_leaderboard:
			print(str(value) + "," + key)


def rank_articles(urls, year=None, filename=None):
	"""
	Takes a list of URLs and searches for them in 
	Hacker News submissions. Prints or saves each article 
	URL and its points to a given filename in descending 
	order of points. Searches for submissions from all years, 
	unless specific year is given.
	"""
	now = datetime.now()
	if year:
		if year > now.year: 
			print("Please enter a valid year parameter (example: " + str(now.year) + ") or leave out for all time.")
			return None
		else:
			pass
		
	articles = {}
	count = 0

	for url in urls:
		query = 'http://hn.algolia.com/api/v1/search?query=' + url + '&restrictSearchableAttributes=url'
		r = requests.get(query)
		data = json.loads(r.text)
		for item in data['hits']:
			link = item['url']
			points = item['points']
			date = item['created_at'][:-5]
			date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
			if not year:
				articles[link] = points
			elif date.year != year:
				pass
			else:
				articles[link] = points
		count += 1
		progress = (count / len(urls) ) * 100.00
		sys.stdout.write(" Progress: %d%%   \r" % (progress) )
		sys.stdout.flush()

	sorted_articles = reversed(sorted(articles.items(), key=operator.itemgetter(1)))

	if filename:
		f = open(filename, 'w')
		for key, value in sorted_articles:
			f.write(str(value) + "," + key + '\n')
		f.close()
		print('Results saved to ' + filename)
	else:
		for key, value in sorted_articles:
			print(str(value) + "," + key)

