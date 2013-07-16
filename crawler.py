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
urlList2 = []

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
      print link #used to show the program is running
      print len(urlList)
#AT THIS POINT I GET ALL THE DEPARTMENTS IN THE GOVERNMENT 509 OF THEM

#next page
for url in urlList:
  #find div class="right" <a>
  nextlink = urllib2.urlopen(url)
  soup = BeautifulSoup(''.join(nextlink))
  url2 = soup.find('a',{'class':'url'})['href']
  if url2 not in urlList2:
    urlList2.append(url2)
    print url2 #used to show the program is running
    print len(urlList2)

#find all .gov link is each page
siteList = []

#for url3 in urlList2:
#  link = urllib2.urlopen(url3)
 # soup = BeautifulSoup(''.join(link))
  #for a in soup.findAll('a'):
   # extention = a.get('href')
    #if extention not in siteList:
     # if extention != None:
      #  if re.match('^/', extention):
       #   siteList.append(url + extention)

for item in siteList:
  print item

# write urlList2 to csv.file
import csv
with open('url.csv','wb') as f:
  writer = csv.writer(f, delimiter = ' ', quotechar = '|')
  writer.writerows(urlList2)
#read written .csv file
with open('url.csv', 'rb') as r:
  reader = csv.reader(r, delimiter=',',quotechar='|')
  for row in reader:
    print ''.join(row)






print 'siteList...' ,
print len(siteList)
print 'urlList2 length...' ,
print len(urlList2)
print 'urlList length...' ,
print len(urlList)
