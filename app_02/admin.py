from django.contrib import admin
# Register your models here.
from .models import OaWorkFlow, OaCondition, OaTransferring, OaApproverGroup


class OaWorkFlowAdmin(admin.ModelAdmin):
    search_fields = ("flowname",)
    list_display = ("id", "flowname", "TID", "tid", "flowtype")
    list_per_page = 15


class OaConditionAdmin(admin.ModelAdmin):
    search_fields = ("descripion", "afid")
    list_display = ('id', 'descripion', 'afid', 'WorkFid', 'workfid', 'priority')
    list_per_page = 15


class OaTransferringAdmin(admin.ModelAdmin):
    list_display = ('id', 'route')
    list_per_page = 15


class OaApproverGroupAdmin(admin.ModelAdmin):
    search_fields = ('groupname','alias','leader')
    list_display = ('id', 'groupname', 'leader', 'order', 'alias', 'must')
    list_per_page = 15


admin.site.register(OaWorkFlow, OaWorkFlowAdmin)
admin.site.register(OaCondition, OaConditionAdmin)
admin.site.register(OaTransferring, OaTransferringAdmin)
admin.site.register(OaApproverGroup, OaApproverGroupAdmin)
