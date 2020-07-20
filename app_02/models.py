from django.db import models

from . import choice_map


class OaApproverGroup(models.Model):
    must_map = ((1, "是"), (0, "否"))
    # id = models.IntegerField(primary_key=True,)
    groupname = models.CharField("审批组名", db_column='groupName', max_length=100, blank=False,
                                 null=False)  # Field name made lowercase.
    leader = models.CharField("直属上级", max_length=100, blank=False, null=False)
    order = models.IntegerField(blank=False, null=False, default=1)
    alias = models.CharField("审批别名", max_length=100, blank=False, null=False)
    must = models.IntegerField("是否必须", choices=must_map, blank=False, null=False, default=0)

    def __str__(self):
        return "审批组管理---->" + str(self.groupname)

    class Meta:
        managed = False
        verbose_name_plural = '审批组管理'
        db_table = 'oa_approver_group'


class OaCondition(models.Model):
    # id = models.IntegerField(primary_key=True)
    descripion = models.TextField("申请内容信息", blank=False, null=False)
    afid = models.IntegerField("报销类型", choices=choice_map.afid_to_formName(), blank=False, null=False)
    workfid = models.IntegerField("对应工作流程", choices=choice_map.tid_to_route(), blank=False, null=False)
    priority = models.IntegerField("优先级", blank=False, null=False)

    def __str__(self):
        return "申请报销管理---->" + str(self.id)

    def WorkFid(self):
        return self.workfid

    WorkFid.short_description = '工作流程id'

    class Meta:
        managed = False
        verbose_name_plural = "申请报销管理"
        db_table = 'oa_condition'


class OaTransferring(models.Model):
    # id = models.IntegerField(primary_key=True)
    route = models.CharField("审批流程", max_length=100, blank=False, null=False)

    def __str__(self):
        return "审批流程管理---->" + str(self.id)

    def route_map(self):
        for r in str(self.route).split():
            return choice_map.trans_route(str(r))

    route_map.short_description = '对应审批流程'

    class Meta:
        managed = False
        verbose_name_plural = "审批流程管理"
        db_table = 'oa_transferring'


class OaWorkFlow(models.Model):
    # id = models.IntegerField(primary_key=True)
    flowname = models.CharField('流程名', db_column='flowName', max_length=100, blank=False, null=False)
    flowtype = models.IntegerField("流程类型", blank=False, null=False, default=0)
    tid = models.IntegerField('审批流程', choices=choice_map.tid_to_route(), blank=False, null=False)

    def __str__(self):
        return "工作流程管理---->" + str(self.id)

    def TID(self):
        return self.tid

    TID.short_description = "审批流程ID"

    class Meta:
        verbose_name_plural = "工作流程管理"
        managed = False
        db_table = 'oa_work_flow'


class OaBank(models.Model):
    bank = models.CharField("银行名称", null=False, blank=False, max_length=30, default="招商银行")
    bankaccount = models.CharField("银行账户", null=False, blank=False, max_length=100)
    useCompany = models.TextField("所属公司", null=False, blank=False)
    subject = models.CharField("备注", null=False, blank=True, max_length=50)

    def __str__(self):
        return "银行管理表---->" + str(self.id)

    class Meta:
        verbose_name_plural = "银行管理"
        managed = False
        db_table = 'oa_bank'


class OaFeeType(models.Model):

    second_type_map = choice_map.get_second_type()
    # print(second_type_map)
    third_type_map = choice_map.get_third_type()
    feeName = models.CharField("费用名称", null=False, blank=False, max_length=100)
    subject = models.CharField("费用第一类型",choices=second_type_map, null=False, blank=False, max_length=100)
    third = models.CharField("费用第二类型", null=False,choices=third_type_map, blank=False, max_length=100)
    seeCompany = models.CharField("可查看的公司", null=False, max_length=255)
    seeDept = models.TextField("可查看的部门", null=False)
    noDept = models.TextField("可查看的组", null=False)
    specialPerson = models.CharField("特殊用户", null=False, max_length=100)
    noPerson = models.CharField('Noperson', null=False, max_length=100, default='')
    formids = models.CharField("表单类型", null=False, blank=False, max_length=100)
    crashFlow = models.CharField("现金流", null=False, max_length=100)

    def __str__(self):
        return "费用类型管理表---->" + str(self.feeName)

    class Meta:
        verbose_name_plural = "费用类型管理"
        managed = False
        db_table = 'oa_fee_type'


class OaAccountCoding(models.Model):
    name = models.CharField("名称", max_length=200, null=False, blank=False)
    coding = models.CharField("对应代码", max_length=200, null=False, blank=False)
    remark = models.CharField("备注", max_length=200, null=False, blank=False)

    def __str__(self):
        return "费用代码管理---->" + str(self.name)

    class Meta:
        verbose_name_plural = "费用代码管理"
        managed = False
        db_table = 'oa_account_coding'
