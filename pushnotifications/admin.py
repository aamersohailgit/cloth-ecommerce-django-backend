from django.contrib import admin
from .models import ExpoPushToken


class ExpoPushTokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'token')
    # list_filter = ('created_at',)
    search_fields = ('user__username', 'token')



# Register your models here.
admin.site.register(ExpoPushToken, ExpoPushTokenAdmin)
