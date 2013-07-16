#Jon larsen July 2013
#.gov webcrawler
#goal is to find every .gov webpage
#get readability for each site from juicystudio.com

import urllib
import urllib2
from bs4 import BeautifulSoup
import re
import csv
import time

siteList = []
readabilityList = []
#import any .csv file containing only URL's
#REQUIRED:  delimter=',' && quotechar='|'

with open('url.csv', 'rb') as csvfile:
  reader = csv.reader(csvfile, delimiter=' ' , quotechar='|')
  for row in reader:
    siteList.append(''.join(row)) # adds all url's from csv to siteList
   # site list is now full of url's 

#get readability for all url's in siteList

juicy_url = 'http://juicystudio.com/services/readability.php'
for url in siteList:
  time.sleep(1)#sleep for 2 seconds as a curtacy to juicystudio.com
  urlReadabiltiy = [url]
  values = {'url' : url}

  data = urllib.urlencode(values)#converts 2 values into a readable format for .urlopen()

  req = urllib2.Request(juicy_url, data)#POST to webpage

  response = urllib2.urlopen(req)

  the_page = response.read()#contains the resulitng the_page
  soup = BeautifulSoup(''.join(the_page))
  #print soup.findAll('td')
  print '----------------------------------------'
  print url
  print '----------------------------------------'
  #get and print all Juicystudio.com values
  
  print 'Total sentences -- ' ,
  try:
    total_sent = soup.find('td', text = re.compile('Total sentences')).next.next.next.next
    urlReadabiltiy.append(total_sent)
    print total_sent
  except AttributeError:
  	urlReadabiltiy.append('None')
  	continue

  print 'Total words -- ' ,
  try:
    total_words = soup.find('td', text = re.compile('Total words')).next.next.next.next
    urlReadabiltiy.append(total_words)
    print total_words
  except AttributeError:
  	urlReadabiltiy.append('None')
  	continue

  print 'Average words per Sentence -- ' ,
  try:
    average_words = soup.find('td', text = re.compile('Average words per Sentence')).next.next.next.next
    urlReadabiltiy.append(average_words)
    print average_words
  except AttributeError:
  	urlReadabiltiy.append('None')
  	continue

  print 'Words with 1 Syllable -- ' ,
  try:
    one_sylable = soup.find('td', text = re.compile('Words with 1 Syllable')).next.next.next.next
    urlReadabiltiy.append(one_sylable)
    print one_sylable
  except AttributeError:
  	urlReadabiltiy.append('None')
  	continue

  print 'Words with 2 Syllables -- ' ,
  try:
    two_sylables = soup.find('td', text = re.compile('Words with 2 Syllables')).next.next.next.next
    urlReadabiltiy.append(two_sylables)
    print two_sylables
  except AttributeError:
  	urlReadabiltiy.append('None')
  	continue

  print 'Words with 3 Syllables -- ',
  try:
    three_sylables = soup.find('td', text = re.compile('Words with 3 Syllables')).next.next.next.next
    urlReadabiltiy.append(three_sylables)
    print three_sylables
  except AttributeError:
  	urlReadabiltiy.append('None')
  	continue

  print 'Words with 4 or more Syllables -- ',
  try:
    four_more = soup.find('td', text = re.compile('Words with 4 or more Syllables')).next.next.next.next
    urlReadabiltiy.append(four_more)
    print four_more
  except AttributeError:
  	urlReadabiltiy.append('None')
  	continue

  print 'Percentage of word with three or more syllables -- ',
  try:
    percent_three = soup.find('td', text = re.compile('Percentage')).next.next.next.next
    urlReadabiltiy.append(percent_three)
    print percent_three
  except AttributeError:
  	urlReadabiltiy.append('None')
  	continue

  print 'Average Syllables per Word -- ',
  try:
    average_sylables = soup.find('td', text = re.compile('Average')).next.next.next.next
    urlReadabiltiy.append(average_sylables)
    print average_sylables
  except AttributeError:
  	urlReadabiltiy.append('None')
  	continue

  print 'Gunning-Fog Index -- ' ,
  try:
    gunning_fog = soup.find('td', text = re.compile('Gunning Fog Index')).next.next.next.next
    urlReadabiltiy.append(gunning_fog)
    print gunning_fog
  except AttributeError:
    urlReadabiltiy.append('None')
    continue

  print 'Flesch-Kincaid Grade -- ' ,
  try:
    flesch_kincaid = soup.find('td', text = re.compile('Flesch-Kincaid Grade')).next.next.next.next
    urlReadabiltiy.append(flesch_kincaid)
    print flesch_kincaid
  except AttributeError:
  	urlReadabiltiy.append('None')
    #continue

  print 'Flesch Reading Ease -- ' ,
  try:
    flesch_reading = soup.find('td', text = re.compile('Flesch Reading Ease')).next.next.next.next
    urlReadabiltiy.append(flesch_reading)
    print flesch_reading
  except AttributeError:
  	urlReadabiltiy.append('None')
  	continue
  readabilityList.append(urlReadabiltiy)


#export readabilityList as a CSV file
with open('readabiltiy.csv', 'wb') as csvfile:
  writer = csv.writer(csvfile, delimiter=',', quotechar='|')
  writer.writerows(readabilityList)

for tupple in readabilityList:
  print tupple
