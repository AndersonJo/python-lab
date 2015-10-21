'''
Created on May 13, 2014

@author: a141890
'''
from Queue import Queue
from bs4 import BeautifulSoup
from bson import ObjectId
from cookielib import CookieJar
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from forms import IlbeArticleForm
from models import IlbeArticleModel
from mongoengine.errors import DoesNotExist
from pprint import pprint
from urllib2 import HTTPError, URLError
from urlparse import urlparse, urljoin
import json
import os
import random
import re
import string
import threading
import urllib2


NUMBER_OF_CRAWLERS = 20
NUMBER_OF_PARSERS = 5


# Make Temporary Directory
BASE_DIR = os.path.dirname(__file__)
TEMP_DIR = os.path.join(BASE_DIR, 'temp')
if not os.path.exists(TEMP_DIR):
    os.mkdir(TEMP_DIR)


_stdout_lock = threading.Lock()
_url_queue = Queue()
_content_queue = Queue()

_url_history = {}


class Crawler(threading.Thread):
    
    def  __init__(self, baseUrl, lock, urlQueue, contentQueue):
        super(Crawler, self).__init__()
        self.baseUrl = baseUrl
        self.baseHostname = urlparse(self.baseUrl).hostname
        
        self.lock = lock
        self.urlQueue = urlQueue
        self.contentQueue = contentQueue
        
    def run(self):
        
        while True:
            url = self.urlQueue.get()
            
            cj = CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            opener.addheaders = [
                ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22'),
            ]
            try:
                response  = urllib2.urlopen(url)
                if response.getcode() == 200:
                    self.contentQueue.put((url, response.read()))
            except HTTPError as e:
                pass
            except URLError as e:
                pass
                
            self.urlQueue.task_done()
            
            
class ContentParser(threading.Thread):
    
    def  __init__(self, baseUrl, lock, urlQueue, contentQueue):
        super(ContentParser, self).__init__()
        self.baseUrl = baseUrl
        self.baseHostname = urlparse(self.baseUrl).hostname
        
        self.lock = lock
        self.urlQueue = urlQueue
        self.contentQueue = contentQueue
        
    def run(self):
        while True:
            parsedUrl, content = self.contentQueue.get()
            parsedUrl = urlparse(parsedUrl)
            currentUrl = parsedUrl.geturl()
            if self.baseHostname != parsedUrl.hostname:
                continue 
            
            #print currentUrl
            parsedData = self.parse_ilbe(currentUrl, content)
            if parsedData:
                self.save_to_model(parsedData)
            
            bs = BeautifulSoup(content)
            for link in bs.find_all('a', href=True):
                href = link['href']
                
                nextUrl = urljoin(self.baseUrl, href)
                if not _url_history.has_key(nextUrl):
                    _url_history[nextUrl] = True
                    self.urlQueue.put(nextUrl)
                
            self.contentQueue.task_done()
            
    def parse_ilbe(self, url, content):
        response = {}
        try:
            print 'parse_ilbe: '+ url
            #self.save_to_file(content)
            
            bs = BeautifulSoup(content)
            titleEl = bs.find('div', {'class':'title'})
            contentEl =  bs.find('div', {'class': 'xe_content'})
            authorEl = bs.find('div', {'class': 'author'})
            
            title = titleEl.text
            content = str(contentEl)
            author = authorEl.text
            
            response['title'] = title
            response['content'] = content
            response['author'] = author
            return response
        except:
            pass
        return None
        
    def save_to_model(self, data):
        print 'save_to_model'
        
        # Get or Create a user
        username = re.sub('\s+', '', data['author']).strip()
        email = username +"@test.com"
        user, created = get_user_model().objects.get_or_create(username=username, email=email)
        if created:
            user.set_password('1234')
        
        data['registed'] = datetime.utcnow().replace(tzinfo=timezone.utc)
        data['author'] = user
        pprint(data)
        
        articleRow = IlbeArticleModel()
        articleRow.title = data['title']
        articleRow.content = data['content']
        articleRow.author = data['author']
        articleRow.registed = data['registed']
        articleRow.save()
    
    def save_to_file(self, content):
        location = os.path.join(TEMP_DIR, self.random_string() +".html")
        with self.lock:
            with open(location, 'w') as f:
                f.write(content)
        
    def random_string(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))





def begin_crawling(base_url):
    _url_queue.put(base_url)
    
    
    crawlers = []
    for i in xrange(NUMBER_OF_CRAWLERS):
        crawler = Crawler(base_url, _stdout_lock, _url_queue, _content_queue)
        crawler.setDaemon(True)
        crawler.start()
        crawlers.append(crawler)
        
    parsers = []
    for i in xrange(NUMBER_OF_PARSERS):
        parser = ContentParser(base_url, _stdout_lock, _url_queue, _content_queue)
        parser.setDaemon(True)
        parser.start()
        parsers.append(parser)
    
    for t in crawlers:
        t.join()
    
    for t in parsers:
        t.join()
    

if __name__ == "__main__":
    begin_crawling('http://www.ilbe.com/3520231346')








