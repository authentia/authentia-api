from django.contrib import admin

from base.models import DocumentType

# Register your models here.
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')


admin.site.register(DocumentType, DocumentTypeAdmin)
