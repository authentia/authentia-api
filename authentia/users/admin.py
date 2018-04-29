from django.contrib import admin
from django.contrib.auth.models import Group
from users.models import AuthentiaUser, CompanyUser, UserDocument, Lead, TokenUserModel, PhotoEnroll

# Register your models here.
class AuthentiaUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'token', 'created')


class CompanyUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'company', 'token', 'created')


class UserDocumentAdmin(admin.ModelAdmin):
    list_display = ('user', 'document_type', 'file', 'created')


class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created')


class TokenUserModelAdmin(admin.ModelAdmin):
    list_display = ('key',)


class PhotoEnrollAdmin(admin.ModelAdmin):
    list_display = ('user', 'file', 'created',)


admin.site.register(AuthentiaUser, AuthentiaUserAdmin)
admin.site.register(CompanyUser, CompanyUserAdmin)
admin.site.register(UserDocument, UserDocumentAdmin)
admin.site.register(Lead, LeadAdmin)
admin.site.register(PhotoEnroll, PhotoEnrollAdmin)
admin.site.unregister(Group)
