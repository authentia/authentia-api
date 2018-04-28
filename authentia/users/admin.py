from django.contrib import admin
from django.contrib.auth.models import Group
from users.models import AuthentiaUser, CompanyUser

# Register your models here.
class AuthentiaUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'created')

class CompanyUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'company', 'created')


admin.site.register(AuthentiaUser, AuthentiaUserAdmin)
admin.site.register(CompanyUser, CompanyUserAdmin)
admin.site.unregister(Group)
