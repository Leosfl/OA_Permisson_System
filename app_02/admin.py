from django.contrib import admin
# Register your models here.
from .models import OaWorkFlow, OaCondition, OaTransferring, OaApproverGroup,OaBank,OaFeeType,OaAccountCoding


class OaWorkFlowAdmin(admin.ModelAdmin):
    search_fields = ("id","flowname",)
    list_display = ("id", "flowname", "TID", "tid", "flowtype")
    list_per_page = 15


class OaConditionAdmin(admin.ModelAdmin):
    search_fields = ('id',"descripion", "afid")
    list_display = ('id', 'descripion', 'afid', 'WorkFid', 'workfid', 'priority')
    list_per_page = 15


class OaTransferringAdmin(admin.ModelAdmin):
    search_fields = ("id","route")
    list_display = ('id', 'route','route_map',)
    list_per_page = 15


class OaApproverGroupAdmin(admin.ModelAdmin):
    search_fields = ('groupname','alias','leader')
    list_display = ('id', 'groupname', 'leader', 'order', 'alias', 'must')
    list_per_page = 15


class OaBankAdmin(admin.ModelAdmin):
    search_fields = ('bank',)
    list_display = ('id','bank','bankaccount','useCompany','subject')
    list_per_page = 15


class OaFeeTypeAdmin(admin.ModelAdmin):
    search_fields = ('feeName','subject','third')
    list_display = ('id','feeName','subject','third','seeCompany','seeDept','noDept','specialPerson','formids','crashFlow')
    list_per_page = 15


class OaAccountCodingAdmin(admin.ModelAdmin):
    search_fields = ('name','coding')
    list_display = ('id','name','coding','remark')
    list_per_page = 15

admin.site.register(OaWorkFlow, OaWorkFlowAdmin)
admin.site.register(OaCondition, OaConditionAdmin)
admin.site.register(OaTransferring, OaTransferringAdmin)
admin.site.register(OaApproverGroup, OaApproverGroupAdmin)
admin.site.register(OaBank,OaBankAdmin)
admin.site.register(OaAccountCoding,OaAccountCodingAdmin)
admin.site.register(OaFeeType,OaFeeTypeAdmin)

