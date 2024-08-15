from django.contrib import admin
from .models import Singer, Song

class SingerAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender')

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'singer', 'duration')

# Register the models with their respective admin classes
admin.site.register(Singer, SingerAdmin)
admin.site.register(Song, SongAdmin)
