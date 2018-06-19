import requests, re

def get_blogs():
	"""
	Get and parse engineering blog URLs into a list
	"""
	blog_source = requests.get('https://raw.githubusercontent.com/kilimchoi/engineering-blogs/master/README.md')
	blogs = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', blog_source.text)

	del blogs[0] # Remove awesome badge URL
	del blogs[len(blogs) - 1] # Remove Creative Commons URL

	return blogs