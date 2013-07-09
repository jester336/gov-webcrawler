import urllib
import urllib2
from bs4 import BeautifulSoup
import re
#list throught every page in my url list


urlDictionary = {}








url = 'http://juicystudio.com/services/readability.php'
values = {'url' : 'http://aoa.gov'}

data = urllib.urlencode(values)#converts 2 values into a readable format for .urlopen()

req = urllib2.Request(url, data)#POST to webpage

response = urllib2.urlopen(req)

the_page = response.read()#contains the resulitng the_page
soup = BeautifulSoup(''.join(the_page))
#print soup.findAll('td')
print values
#get and print all Juicystudio.com values
print 'Total sentences -- ' ,
print soup.find('td', text = re.compile('Total sentences')).next.next.next.next

print 'Total words -- ' ,
print soup.find('td', text = re.compile('Total words')).next.next.next.next

print 'Average words per Sentence -- ' ,
print soup.find('td', text = re.compile('Average words per Sentence')).next.next.next.next

print 'Words with 1 Syllable -- ' ,
print soup.find('td', text = re.compile('Words with 1 Syllable')).next.next.next.next

print 'Words with 2 Syllables -- ' ,
print soup.find('td', text = re.compile('Words with 2 Syllables')).next.next.next.next

print 'Words with 3 Syllables -- ',
print soup.find('td', text = re.compile('Words with 3 Syllables')).next.next.next.next

print 'Words with 4 or more Syllables -- ',
print soup.find('td', text = re.compile('Words with 4 or more Syllables')).next.next.next.next

print 'Percentage of word with three or more syllables -- ',
print soup.find('td', text = re.compile('Percentage')).next.next.next.next

print 'Average Syllables per Word -- ',
print soup.find('td', text = re.compile('Average')).next.next.next.next

print 'Gunning-Fog Index -- ' ,
print soup.find('td', text = re.compile('Gunning Fog Index')).next.next.next.next

print 'Flesch-Kincaid Grade -- ' ,
print soup.find('td', text = re.compile('Flesch-Kincaid Grade')).next.next.next.next

print 'Flesch Reading Ease -- ' ,
print soup.find('td', text = re.compile('Flesch Reading Ease')).next.next.next.next
