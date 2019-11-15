from django.contrib import admin
from .models import Type,UserDetails,Orphanage,Orphan,AddOrphan,donatevaluables,donatemoney,Emergency,Transport,Events

admin.site.register(Type)
admin.site.register(UserDetails)

class OrphanageDjangoAdmin(admin.ModelAdmin):
    list_display = ['orphanage_name']
    sortable_by = []
    search_fields = []

admin.site.register(Orphanage, OrphanageDjangoAdmin)
admin.site.register(Orphan)
admin.site.register(AddOrphan)
admin.site.register(donatevaluables)
admin.site.register(donatemoney)
admin.site.register(Emergency)
admin.site.register(Transport)
admin.site.register(Events)

# Register your models here.