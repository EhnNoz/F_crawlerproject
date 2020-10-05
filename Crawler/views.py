from . import models
from Crawler import serializers
from rest_framework.response import Response
from rest_framework import viewsets, views, mixins, authentication, permissions


class PlatformViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    queryset = models.Platform.objects.all()
    serializer_class = serializers.PlatformSerializer
    authentication_classes = [authentication.TokenAuthentication]
    #    permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]


class DurationViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = models.Duration.objects.all()
    serializer_class = serializers.DurationSerializer


class ResourceViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = models.Resource.objects.filter(active=True)
    serializer_class = serializers.ResourceSerializer


class ConfigViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Config.objects.all()
    serializer_class = serializers.ConfigSerializer


#
#
class ManifestViewSet(viewsets.ModelViewSet):
    queryset = models.Manifest.objects.filter(active=True)
    serializer_class = serializers.ManifestSerializer


class Manifest_SPViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Manifest.objects.filter(active=True)
    serializer_class = serializers.ManifestSpSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer


class AlexaViewSet(views.APIView):
    def get(self, request):
        urls = request.GET['u'] if 'u' in request.GET else ''
        data = []
        for url in urls.split(','):
            data.append({'url': url})

        results = serializers.AlexaSerializer(data=data, many=True)
        results.is_valid(raise_exception=True)
        return Response(results.data)
