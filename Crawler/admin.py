from .models import *
from django.contrib import admin
from django.contrib import messages


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    class Meta:
        model = Platform


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    class Meta:
        model = Resource


@admin.register(Manifest)
class ManifestAdmin(admin.ModelAdmin):
    class Meta:
        model = Manifest


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    class Meta:
        model = Config

    def save_model(self, request, obj, form, change):
        try:
            return super(ConfigAdmin, self).save_model(request, obj, form, change)
        except Exception as e:
            self.message_user(request, e, messages.ERROR)

    def save_form(self, request, form, change):
        try:
            return super(ConfigAdmin, self).save_form(request, form, change)
        except Exception as e:
            self.message_user(request, e, messages.ERROR)

    def save_related(self, request, form, formsets, change):
        try:
            return super(ConfigAdmin, self).save_related(request, form, formsets, change)
        except Exception as e:
            self.message_user(request, e, messages.ERROR)
            
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    class Meta:
        model = News