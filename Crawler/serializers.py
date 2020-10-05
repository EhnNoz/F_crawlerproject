import locale
import requests
from .models import *
from bs4 import BeautifulSoup
from rest_framework import serializers

locale.setlocale(locale.LC_ALL, '')


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['id', 'name', 'active']


class DurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duration
        fields = ['id', 'duration', 'active']


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
        fields = ['plan', 'duration', 'platforms', 'reousrces']


class ManifestSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True)

    #    total_crawled_records = serializers.SerializerMethodField()
    #    total_delivered_records = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Manifest
        fields = ['id', 'keywords', 'resources', 'active', 'status']

    # def get_total_crawled_records(self, obj):
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
        fields = ['id', 'Platform', 'Sender_Name', 'Message', 'Message_Time', 'Time', 'Message_Link']

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


class AlexaSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=1024)
    rank = serializers.SerializerMethodField()
    rank_formatted = serializers.SerializerMethodField()
    content = None

    class Meta:
        fields = ['url', 'rank', 'rank_formatted']

    def get_content(self, obj):
        if not 'content' in obj:
            r = requests.get('https://www.alexa.com/siteinfo/%s' % obj['url'])
            obj['content'] = r.content
        return obj['content']

    def get_rank(self, obj):
        if not 'rank' in obj:
            content = self.get_content(obj)
            soup = BeautifulSoup(content)
            try:
                main_content = soup.find('p', attrs={'class': 'big data'}).text
                b = main_content.strip()
                a = str(b)
                a = a.replace("#", "").replace(",", "").strip()
                obj['rank'] = int(a)
            except:
                obj['rank'] = "N/A"

        return obj['rank']

    def get_rank_formatted(self, obj):
        try:
            return locale.format("%d", obj['rank'], grouping=True)
        except:
            return "N/A"
