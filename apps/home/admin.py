from django.contrib import admin

# Register your models here.
from apps.home.models import Users
# Register your models here.


class AdminUsers(admin.ModelAdmin):
    list_display=('id','username','phone', 'email')

admin.site.register(Users,AdminUsers)