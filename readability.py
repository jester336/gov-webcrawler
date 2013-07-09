import urllib
import urllib2
import re
import csv
from bs4 import BeautifulSoup
#juicy_url define at top so it is only created once
juicy_url = 'http://juicysutdio.com/services/readability.php'
#import csv file into list
#define what csv file to open
csvfile = '/users/jonlarsen/Desktop/govsites.csv'
#open csv file with reader
reader = csv.reader(open(csvfile))
#creates a list called '' and imports every line from csvfile
urlList = list(reader) 

#loop throught the list for keywords
for url in urlList:
  #get html for page
  response = urllib2.urlopen(url)
  page_html = response.read()

  #parse HTML with BeautifulSoup
  soup = BeautifulSoup(''.join(page_html))
  soup.find("meta",{"name":"keywords"})['contents']

  #define what is to be entered into the readability site
  url_value = {'url': url}

  #make values in a format that urllib2 can read
  data = urllib.urlencode(url_value)

  #really not full sertain what the next two steps do!!
  request = urllib2.Request(juicy_url, data) #POST to php page
  response = urllib2.urlopen(request)

  #get the HTML from the juicystudion request
  juicy_page = response.read()

  #parse the juicy_page for data
  #may have to make the url list a dictionary to hold all the data
  		# example
  	# tel = {'jack' : 4490, 'sape': 4839}
  	# tel['guido'] = 893
  	# tel[jack].......4490
