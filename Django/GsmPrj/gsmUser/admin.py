from django.contrib import admin
from gsmUser.models import Guser
# Register your models here.

class GuserAdmin(admin.ModelAdmin):
    list_display=('username','password')

admin.site.register(Guser,GuserAdmin)