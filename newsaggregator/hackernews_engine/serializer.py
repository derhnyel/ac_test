#import your model
from rest_framework import serializers
from .models import Items

class ItemsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Items
        fields = ['type','title','time','id','score']


