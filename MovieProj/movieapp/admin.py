from django.contrib import admin
from movieapp.models import AbtMovie

class AbtMovieAdmin(admin.ModelAdmin):
    list_display=["mname","mrating","mcast","mdate"]

admin.site.register(AbtMovie,AbtMovieAdmin)
