from django.contrib import admin

from .models import Oafinance, Oaother, Oahr, Oaapprover, Oaexecutives, Oaadmin


class OafinanceAdmin(admin.ModelAdmin):
    search_fields = ("ldap", 'name')
    list_display = ("ldap", 'name')
    list_per_page = 15


class OaapproverAdmin(admin.ModelAdmin):
    search_fields = ("ldap", 'name')
    list_display = ('ldap', 'name', "leave", "dimission")
    list_per_page = 15


class OaotherAdmin(admin.ModelAdmin):
    search_fields = ("ldap", 'name')
    list_display = ("ldap", "name", "qr_code_auth", "password_auth", "add_ldap_auth")
    list_per_page = 15


class OahrAdmin(admin.ModelAdmin):
    search_fields = ("ldap", 'name')
    list_display = ("ldap", "name", "company", "exportstaff", "confirmentry", "cancel_ack_leave_auth")
    list_per_page = 15


class OaexecutivesAdmin(admin.ModelAdmin):
    search_fields = ("ldap", 'name')
    list_display = ("ldap", "name")
    list_per_page = 15


class OaadminAdmin(admin.ModelAdmin):
    search_fields = ("ldap", 'name')
    list_display = ("ldap", 'name')
    list_per_page = 15


admin.site.register(Oahr, OahrAdmin)
admin.site.register(Oaother, OaotherAdmin)
admin.site.register(Oafinance, OafinanceAdmin)
admin.site.register(Oaapprover, OaapproverAdmin)
admin.site.register(Oaexecutives, OaexecutivesAdmin)
admin.site.register(Oaadmin, OaadminAdmin)
# from django.contrib import admin

# Register your models here.
