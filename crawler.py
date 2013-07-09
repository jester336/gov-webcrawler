#Jon Larsen July 2013
#make a web crawler to iterate through all the .gov links
#on the usa.gov site
#this is a crawler for usa.gov only

import urllib
import urllib2
import string
import re
from bs4 import BeautifulSoup

allTheLetters = string.uppercase #A-Z capital letters
allTheLetters = allTheLetters.replace("A", "")#A is index.shtml
allTheLetters = allTheLetters.replace("K", "")
allTheLetters = allTheLetters.replace("Q", "")
allTheLetters = allTheLetters.replace("X", "")
allTheLetters = allTheLetters.replace("Y", "")
allTheLetters = allTheLetters.replace("Z", "")
seed_url = urllib2.urlopen('http://www.usa.gov/directory/federal/index.shtml')
urlList = []

soup = BeautifulSoup(''.join(seed_url))

for link in soup.findAll('a', {'class':'url'}):
    href = link.get('href')
    templink = 'http://usa.gov' + href
    if link not in urlList:
      urlList.append(templink)

for letter in allTheLetters:#iterate through the alphabet
  #letter A starts with index.shtml
  temp = 'http://usa.gov/directory/federal/' + letter + '.shtml'
  to_be_named_later = urllib2.urlopen(temp)
  #open usa.gov url
  soup = BeautifulSoup(''.join(to_be_named_later))
  for link in soup.findAll('a', {'class':'url'}):
    href = link.get('href')
    templink = 'http://usa.gov' + href
    if link not in urlList:
      urlList.append(templink)
#AT THIS POINT I GET ALL THE DEPARTMENTS IN THE GOVERNMENT 509 OF THEM

#next page
for url in urlList:

link = urllib2.urlopen('http://www.usa.gov/directory/federal/abilityone-commission.shtml')

soup = BeautifulSoup(''.join(link))
link_foo = soup.find('a',{'class':'url'})['href']
print link_foo









print urlList
print len(urlList)