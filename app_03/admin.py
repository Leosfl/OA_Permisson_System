from django.contrib import admin

from .models import Permission,TBS

class ReadonlyFieldsMixin(object):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return super(ReadonlyFieldsMixin, self).get_readonly_fields(request, obj)
        else:
            return tuple()

# Register your models here.

class PermissionAdmin(ReadonlyFieldsMixin,admin.ModelAdmin):
    list_display = ("ldap","noter","admin")
    readonly_fields = ("ldap",)
    list_per_page = 15


class TBSModelAdmin(ReadonlyFieldsMixin,admin.ModelAdmin):
    list_per_page = 15
    list_display = ("id","ldap","name","money","created_at","updated_at","company")
    readonly_fields = ("ldap",)

admin.site.register(Permission,PermissionAdmin)
admin.site.register(TBS,TBSModelAdmin)