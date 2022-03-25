from .utils import engine
from django.core.cache import cache
from .models import Items
import asyncio


#create an instance of hacker_news_api_calls 
hackernews = engine.HackerNewsEngine()

#fetch ids
#check for cache/ db availablility
#find items in new_items not in cache or db

def crud_cachedb(key):
    fetched_ids = hackernews.get_story(key)
    cached_ids = cache.get(key)
    recent_ids = fetched_ids
    if cached_ids is not None:# set higher priority on cache
        recent_ids = recentids(cached_ids,fetched_ids)
        cache.set(key,fetched_ids)
        #write to cache with fetched_ids   
    else:
        db_ids = Items.objects.values_list('id',flat=True)
        if db_ids.exists():
            recent_ids = recentids(db_ids,fetched_ids)

#event loop
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop) 
    # return loop.run_until_complete(hackernews.get_useritem('item',recent_ids))

    # loop = asyncio.get_event_loop()    
    # return  loop.run_until_complete(hackernews.get_useritem('item',recent_ids))

    return list(hackernews.get_story('item',id) for id in recent_ids) 

def get_dbtasks(items):
    tasks = []
    for item in items:
        kwargs = dict(id=item['id'],type=item['type'],score= item['score'],title =item['title'],time =item['time'])
        tasks.append(asyncio.create_task(Items.objects.create(**kwargs)))
    return tasks
       
async def async_dbwrite(items):
    tasks = get_dbtasks(items)
    coroutines = await asyncio.gather(*tasks)
    for coroutine in coroutines:
        await coroutine

#write recent_items  to db  
def write_db(recent_items):
    for item in recent_items:
        kwargs = dict(type=item['type'],score=item['score'],title =item['title'],time =item['time'])
        Items.objects.create(id=item['id'],**kwargs)
        
def recentids(storedids,fetchedids):
    """Find uncommon elements in the lists"""  
    set_storedids,set_fetchedids = set(storedids),set(fetchedids) # this reduces the lookup time from O(n) to O(1)
    
    #recent_ids = [id for id in fetchedids if id not in set_storedids] #list comprehension to find elements in list_2 not in list_1
    
    recent_ids = list(set_fetchedids.difference(set_storedids))
    return recent_ids 

def main(key):
    items = crud_cachedb(key)

    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop) 
    # loop.run_until_complete(async_dbwrite(items))
    
    #loop = asyncio.get_event_loop()    
    #loop.run_until_complete(async_dbwrite(items))

    write_db(items)
                  
