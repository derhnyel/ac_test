from .models import Items
from .serializer import ItemsSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from .utils import utils
import datetime
from django.db.models import F

class WordCountApi(APIView):
    """
    Get Occurences
    """
    def get(self,request):
        #unpack word,story,day,score queries from url request
        word,story,day,score = request.query_params.get('word'),request.query_params.get('story'),request.query_params.get('day'),request.query_params.get('score')
        #check query validity
        word_check,story_check,day_check ,score_check= utils.check_query(word),utils.check_query(story),utils.check_query(day),utils.check_query(score)
        word,story,day,score = int(word) if word_check else 0,int(story) if story_check else 0,int(day) if day_check else 0,int(score) if score_check else 0
        #define queryset based on values
        days_ago = datetime.date.today() - datetime.timedelta(days=day)
        less_days_ago = datetime.date.today() - datetime.timedelta(days=day-1)
        #datetime.date.today()
        #.filter(time__lte = F('time') - datetime.timedelta(days=day),time__gte = F('time') - datetime.timedelta(days=day-1))
        queryset = Items.objects.filter(type='story',score__gte=score).order_by('-time')[:story] if score != 0 else Items.objects.filter(type='story').all().order_by('-time')[:story] if day is 0 else Items.objects.exclude(time__gte=less_days_ago).filter(time__gte=days_ago)
        #extract titles from queryset
        titles = [element.title for element in queryset]
        #get word_count in tiltes
        word_count = utils.word_frequency(titles)[:word]
        key = 'top {occurence} most occured word in {stories} stories in the last {days} day(s) with {score} karma'.format(occurence=word if word != 0 else '(Null)',stories=story if story != 0 else '(Null)',days=day if day != 0 else '(Null)',score=score if score != 0 else '(Null)')
        return Response({key:word_count})
        #raise Http404 
        #items_serializer = ItemsSerializer(items,many=True)
        
        



