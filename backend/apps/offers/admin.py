from django.contrib import admin

# Register your models here.
from backend.apps.offers.models import *

admin.site.register(BoardType)
admin.site.register(RoomType)
admin.site.register(Offer)