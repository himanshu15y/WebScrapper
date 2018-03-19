import requests
import urllib
import os
from bs4 import BeautifulSoup as bs
from collections import deque
import re
def parseDirectories(deq,song):
	url=deq.pop()
	print "parsing directory",url
        baseurl=url
        page=requests.get(url)
        print "status is ",page.status_code
        soup=bs(page.content,'html.parser')
        html=list(soup.children)
        typeofchilds=[type(item) for item in html]
        #print typeofchilds
        #print list(list(html[2].children)[1])
        z=0
	for a in soup.find_all('a', href=True):
		newurl=baseurl+"/"+a['href']
		print "this is url",newurl
		#u = urllib.urlopen(newurl)
        	#link_type = u.headers.gettype()
		if ".." in newurl:
			print "not adding",newurl
			continue
		if newurl[-1]=="/":
			print "adding",newurl
#			if z>2:
#				break
			z+=1
			deq.append(newurl)
		elif song in newurl:
			print song,"found in",url
                	return
		#print "type of link",link_type
    		#print "Found the URL:", a['href']
	for readText in page.content.split("\n"):
	#	print readText
                if re.match("^_d",str(readText)):
        #                print readText
                        s=readText.split(",")[0][3:].strip("'")
                        deq.append(base_url+""+str(s)+"/")
         #               print deq
			if len(deq) > 2:
				break;
                        print "length of deque",len(deq)
                if re.match("^_f",str(readText)):
                        if song in readText:
                                print song,"found in",url
                                return
	print "here",len(deq)
        parseDirectories(deq,song)
base_url="http://dl.myirmusic.com/Artist/"
'''page = requests.get("http://dl.myirmusic.com/Artist/")
print page.status_code
#print page.content
soup = bs(page.content, 'html.parser')
#print(soup.prettify())
html=list(soup.children)
typeofchilds=[type(item) for item in html] 
print typeofchilds
'''
#print list(list(html[2].children)[1])
deq=deque([base_url]);
'''
for readText in page.content.split("\n"):
	if re.match("^_d",str(readText)):
		print readText
		s=readText.split(",")[0][3:].strip("'")
		deq.append(base_url+""+str(s)+"\\")
		print deq
		print len(deq)
	else:
		print "nope"
'''
parseDirectories(deq,"Donyami")
'''
#print list(body.children)
page1=requests.get("http://thesoundeffect.com/music/mp3/")
host="http://thesoundeffect.com/music/mp3/"
#print page1.status_code
soup1=bs(page1.content,'html.parser')
#print soup1.find_all('a')[0:2]
for song in soup1.find_all('a',href=True):
#	print "here",song.get_text()
	if("mp3" in str(song.get_text())):
#		print song['href']
		url=host+"/"+song['href']
#		file=requests.get(url,stream=True)
		dump=file.raw
#		print dump
		location="/home/himanshu/Programming"
		break;
	#else:
#		print song['href']
'''
