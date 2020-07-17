from django.db import models


from . import choice_map


class OaApproverGroup(models.Model):
    must_map = ((1,"是"),(0,"否"))
    # id = models.IntegerField(primary_key=True,)
    groupname = models.CharField("审批组名",db_column='groupName', max_length=100,blank=False,null=False)  # Field name made lowercase.
    leader = models.CharField("直属上级",max_length=100,blank=False,null=False)
    order = models.IntegerField(blank=False,null=False,default=1)
    alias = models.CharField("审批别名",max_length=100,blank=False,null=False)
    must = models.IntegerField("是否必须",choices=must_map,blank=False,null=False,default=0)

    def __str__(self):
        return "审批组管理---->" + str(self.groupname)

    class Meta:
        managed = False
        verbose_name_plural='审批组管理'
        db_table = 'oa_approver_group'


class OaCondition(models.Model):
    # id = models.IntegerField(primary_key=True)
    descripion = models.TextField("申请内容信息",blank=False,null=False)
    afid = models.IntegerField("报销类型",choices=choice_map.afid_to_formName(),blank=False,null=False)
    workfid = models.IntegerField("对应工作流程",choices=choice_map.tid_to_route(),blank=False,null=False)
    priority = models.IntegerField("优先级",blank=False,null=False)

    def __str__(self):
        return "申请报销管理---->" + str(self.id)

    def WorkFid(self):
        return self.workfid

    WorkFid.short_description='工作流程id'

    class Meta:
        managed = False
        verbose_name_plural="申请报销管理"
        db_table = 'oa_condition'


class OaTransferring(models.Model):
    # id = models.IntegerField(primary_key=True)
    route = models.CharField("审批流程",max_length=100,blank=False,null=False)

    def __str__(self):
        return "审批流程管理---->"+str(self.id)

    class Meta:
        managed = False
        verbose_name_plural="审批流程管理"
        db_table = 'oa_transferring'


class OaWorkFlow(models.Model):
    # id = models.IntegerField(primary_key=True)
    flowname = models.CharField('流程名',db_column='flowName', max_length=100,blank=False,null=False)
    flowtype = models.IntegerField("流程类型",blank=False,null=False,default=0)
    tid = models.IntegerField('审批流程',choices=choice_map.tid_to_route(),blank=False,null=False)

    def __str__(self):
        return "工作流程管理---->" + str(self.id)

    def TID(self):
        return self.tid
    TID.short_description="审批流程ID"

    class Meta:
        verbose_name_plural="工作流程管理"
        managed = False
        db_table = 'oa_work_flow'
