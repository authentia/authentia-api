from django.contrib import admin

from companies.models import Company, CompanyDocument, Transaction

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('bussiness_name', 'tax_id', 'email_contact', 'is_active', 'created')


class CompanyDocumentAdmin(admin.ModelAdmin):
    list_display =  ('company', 'document_type', 'file', 'created')


class TransactionAdmin(admin.ModelAdmin):
    list_display =  ('company', 'user', 'status', 'photo', 'created')


admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyDocument, CompanyDocumentAdmin)
admin.site.register(Transaction, TransactionAdmin)
