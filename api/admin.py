from django.contrib import admin
from api.models import PhoneToken, CustomUser

class PhoneTokenAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'otp']

admin.site.register(PhoneToken)
admin.site.register(CustomUser)

# Register your models here.
