from django.contrib import admin

from .models import Oafinance, Oaother, Oahr, Oaapprover, Oaexecutives, Oaadmin,OaPosition

class ReadonlyFieldsMixin(object):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return super(ReadonlyFieldsMixin, self).get_readonly_fields(request, obj)
        else:
            return tuple()

class OafinanceAdmin(ReadonlyFieldsMixin,admin.ModelAdmin):
    search_fields = ("ldap", 'name')
    list_display = ("ldap", 'name')
    readonly_fields = ('ldap',)
    list_per_page = 15


class OaapproverAdmin(ReadonlyFieldsMixin,admin.ModelAdmin):
    search_fields = ("ldap", 'name')
    list_display = ('ldap', 'name', "leave", "dimission")
    readonly_fields = ('ldap',)
    list_per_page = 15


class OaotherAdmin(ReadonlyFieldsMixin,admin.ModelAdmin):
    search_fields = ("ldap", 'name')
    readonly_fields = ('ldap',)
    list_display = ("ldap", "name", "qr_code_auth", "password_auth", "add_ldap_auth")
    list_per_page = 15


class OahrAdmin(ReadonlyFieldsMixin,admin.ModelAdmin):
    search_fields = ("ldap", 'name')
    readonly_fields = ('ldap',)
    list_display = ("ldap", "name", "company", "exportstaff", "confirmentry", "cancel_ack_leave_auth")
    list_per_page = 15


class OaexecutivesAdmin(ReadonlyFieldsMixin,admin.ModelAdmin):
    search_fields = ("ldap", 'name')
    list_display = ("ldap", "name")
    readonly_fields = ('ldap',)
    list_per_page = 15


class OaadminAdmin(ReadonlyFieldsMixin,admin.ModelAdmin):
    search_fields = ("ldap", 'name')
    list_display = ("ldap", 'name')
    readonly_fields = ('ldap',)
    list_per_page = 15

class OaPositionAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_per_page = 15
    search_fields = ('name',)

admin.site.register(Oahr, OahrAdmin)
admin.site.register(Oaother, OaotherAdmin)
admin.site.register(Oafinance, OafinanceAdmin)
admin.site.register(Oaapprover, OaapproverAdmin)
admin.site.register(Oaexecutives, OaexecutivesAdmin)
admin.site.register(Oaadmin, OaadminAdmin)
admin.site.register(OaPosition,OaPositionAdmin)
# from django.contrib import admin

# Register your models here.
