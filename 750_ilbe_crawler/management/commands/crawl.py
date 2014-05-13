'''
Created on May 13, 2014

@author: a141890
'''
from crawler.crawler import begin_crawling
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        self.stdout.write("Begin Crawling", ending="\n")
        begin_crawling(args[0])
        