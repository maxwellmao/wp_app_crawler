import random
import json
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

'''
    code is from http://tangww.com/2013/06/UsingRandomAgent/
'''

class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent
        with open('user_agent_list.json') as fp:
            self.user_agent_list=json.load(fp)

#for more user agent strings,you can find it in http://www.useragentstring.com/pages/useragentstring.php
    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            request.headers.setdefault('User-Agent', ua)
#            print '[User agent]', ua
