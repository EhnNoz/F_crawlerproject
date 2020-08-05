from rest_framework import serializers
from .models import *


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['id', 'name', 'active']


class ResourceSerializer(serializers.ModelSerializer):
    platform = PlatformSerializer()

    class Meta:
        model = Resource
        fields = ['id', 'name', 'platform', 'active']


class ConfigSerializer(serializers.ModelSerializer):
    reousrces = ResourceSerializer(many=True)
    platforms = PlatformSerializer(many=True)

    class Meta:
        model = Config
        fields = ['plan', 'platforms', 'reousrces']





class ManifestSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True)
    
#    total_crawled_records = serializers.SerializerMethodField()
#    total_delivered_records = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Manifest
        fields = ['id', 'keywords', 'resources', 'active','status']

#    def get_total_crawled_records(self, obj):
#        return obj.total_crawled_records()
#
#    def get_total_delivered_records(self, obj):
#        return obj.total_delivered_records()
        
    def get_status(self, obj):
        return obj.status()


        
class NewsSerializer(serializers.ModelSerializer):
    
#    total_crawled = serializers.SerializerMethodField()
    
    class Meta:
        model = News
        fields = ['id','Platform','Sender_Name','Message','Message_Time','Time','Message_Link']
        
    def get_total_crawled(self, obj):
        return obj.total_crawled()
    
    
    
class ManifestSpSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True)
    
#    status = serializers.SerializerMethodField()

    class Meta:
        model = Manifest
        fields = ['id', 'keywords', 'resources']
        
#    def get_status(self, obj):
#        return obj.status()