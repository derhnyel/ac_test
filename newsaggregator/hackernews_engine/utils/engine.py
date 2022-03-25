#fetch news articles from hackernew api
from datetime import datetime
import time
from fake_useragent import UserAgent
import random
import asyncio
import aiohttp
import requests

USER_AGENTS = [
    "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Firefox/59",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
]

def gen_user_agent() -> str:
    user_agent = random.choice(USER_AGENTS)
    try:
        user_agent = UserAgent().random
    except Exception:
       pass
    return user_agent

class HackerNewsEngine():
    def __init__(self):
        self.url = 'https://hacker-news.firebaseio.com/v0/{path}'

    def get_tasks(self,session,endpoint,ids):
        endpoints = {'user':'user/{id}.json','item':'item/{id}.json'}
        if endpoint in endpoints:
            tasks =[]
            for id in ids:
                print('event_on_loop')
                tasks.append(asyncio.create_task(session.get(url=self.url.format(path=endpoint.format(user_id=id),headers=self.get_header()))))
                time.sleep(0.1)
            print('\n\n\n\n\n\nall on event loop')    
            return tasks
        raise Exception("Endpoint not valid")    

    def get_header(self):
        headers = {
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "User-Agent": gen_user_agent(),
        }
        return headers
    async def get_useritem(self,endpoint,ids):

        results = []
        async with aiohttp.ClientSession() as session:
            tasks = self.get_tasks(session,endpoint,ids)
            responses = await asyncio.gather(*tasks)
            for response in responses:
                try:
                    api_response = await response.json()
                    print(api_response)
                except:
                    continue    
                if 'time' in api_response:
                    api_response['time'] = datetime.fromtimestamp(api_response['time']) #format items timestamp with datetime
                    results.append(api_response)

        return results        
    async def request(self,path):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url.format(path=path),headers = self.get_header()) as response:
                return await response.json()  
                        
    def get_story(self,endpoint=None,id=None,request_= False): 
        """Function to get stories"""
        print('Event Started')
        time.sleep(0.02)
        endpoints = {'max':'maxitem.json','top':'topstories.json','update':'updates.json', 'job':'jobstories.json','new':'newstories.json','user':'user/{id}.json','item':'item/{id}.json'}
        try:
            if endpoint in endpoints:
                path = endpoints[endpoint]
                if endpoint in ['user', 'item']:
                    path = path.format(id=id)
                if not request_:    
                    #loop = asyncio.get_event_loop()   
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop) 
                    api_response = loop.run_until_complete(self.request(path))
                    if endpoint in ['user', 'item']:
                        if 'time' in api_response:
                            api_response['time'] = datetime.fromtimestamp(api_response['time']) 
                            print(api_response)
                    return api_response
                api_response = requests.get(self.url.format(path=path),headers=self.get_header()).json()
                if 'time' in api_response:
                    api_response['time'] = datetime.fromtimestamp(api_response['time']) #format items timestamp with datetime
                    return api_response
        except:        
            return None
            



 








