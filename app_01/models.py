from django.db import models

is_leave = (("0", "否"), ("1", "是"))


class Oaapprover(models.Model):
    ldap = models.CharField('ldap', primary_key=True, max_length=255)
    name = models.CharField('姓名', max_length=255, blank=False, null=True)
    leave = models.CharField('能否审批请假', choices=is_leave, max_length=255, blank=False, null=True,default='0')
    dimission = models.CharField('能否审批离职权限', choices=is_leave, max_length=255, blank=False, null=True,default='0')

    def __str__(self):
        return "审批权限表---->" + str(self.name)

    class Meta:
        managed = False
        db_table = 'oaapprover'
        verbose_name_plural = '审批权限管理'


class Oaexecutives(models.Model):
    ldap = models.CharField(primary_key=True, max_length=255)
    name = models.CharField('姓名', max_length=255, blank=False, null=True)

    def __str__(self):
        return "执行权限表---->" + str(self.name)

    class Meta:
        managed = False
        db_table = 'oaexecutives'
        verbose_name_plural = '执行权限管理'


class Oafinance(models.Model):
    ldap = models.CharField(primary_key=True, max_length=255)
    name = models.CharField('姓名', max_length=255, blank=False, null=True)

    def __str__(self):
        return "财政权限表---->" + str(self.name)

    class Meta:
        managed = False
        db_table = 'oafinance'
        verbose_name_plural = '财政权限管理'


class Oahr(models.Model):
    ldap = models.CharField(primary_key=True, max_length=255)
    name = models.CharField('姓名', max_length=255, blank=False, null=True)
    company = models.CharField('可导出员工信息的公司名称', max_length=255, blank=False, null=True)
    exportstaff = models.CharField('能否导出员工', choices=is_leave, db_column='exportStaff', max_length=255, blank=False,
                                   null=True,default='0')  # Field name made lowercase.
    confirmentry = models.CharField('能否确定入职', choices=is_leave, db_column='confirmEntry', max_length=255, blank=False,
                                    null=True,default='0')  # Field name made lowercase.
    cancel_ack_leave_auth = models.CharField('能否销假', choices=is_leave, max_length=255, blank=False, null=True,default='0')

    def __str__(self):
        return "人事权限表---->" + str(self.name)

    class Meta:
        managed = False
        db_table = 'oahr'
        verbose_name_plural = '人事权限管理'


class Oaother(models.Model):
    ldap = models.CharField(primary_key=True, max_length=255)
    name = models.CharField('姓名', max_length=255, blank=True, null=True)
    qr_code_auth = models.CharField('能否重置二维码', choices=is_leave, max_length=255, blank=False, null=True,default='0')
    password_auth = models.CharField('能否重置密码', choices=is_leave, max_length=255, blank=False, null=True,default='0')
    add_ldap_auth = models.CharField('能否添加ldap', choices=is_leave, max_length=255, blank=False, null=True,default='0')

    # cancel_ack_leave_auth = models.CharField('能否销假',max_length=255, blank=True, null=True)

    def __str__(self):
        return "IT权限表---->" + str(self.name)

    class Meta:
        managed = False
        db_table = 'oaother'
        verbose_name_plural = 'IT权限管理'


class Oaadmin(models.Model):
    ldap = models.CharField('ldap', primary_key=True, max_length=255)
    name = models.CharField('姓名', max_length=255, blank=False, null=True)

    def __str__(self):
        return "管理员权限表---->" + str(self.name)

    class Meta:
        managed = False
        db_table = 'oaadmin'
        verbose_name_plural = '管理员权限管理'
