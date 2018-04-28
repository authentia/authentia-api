from django.contrib import admin

from companies.models import Company, CompanyDocument

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('bussiness_name', 'tax_id', 'email_contact', 'is_active', 'created')


class CompanyDocumentAdmin(admin.ModelAdmin):
    list_display =  ('company', 'document_type', 'file', 'created')


admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyDocument, CompanyDocumentAdmin)
