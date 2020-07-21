from django.db import models


class Permission(models.Model):
    auth_map = (
        (0,"否"),
        (1,"是")
    )
    ldap = models.CharField("Ldap",primary_key=True, max_length=50, null=False, blank=False, unique=True)
    noter = models.CharField("Noter", choices=auth_map, default=0,max_length=20)
    admin = models.CharField("Admin", choices=auth_map,default=0,max_length=20)

    def __str__(self):
        return "TB权限管理---->" + str(self.ldap)

    class Meta:
        managed = False
        verbose_name_plural = 'TB权限管理'
        db_table = 'permission'

class TBS(models.Model):
    ldap = models.CharField("Ldap",max_length=255,unique=True,null=False,blank=False)
    name = models.CharField("姓名",max_length=255,null=False,blank=False)
    money = models.IntegerField("金额",null=False,blank=False)
    created_at = models.DateTimeField("创建时间",auto_now_add=True)
    updated_at = models.DateTimeField("修改时间",auto_now=True)
    company = models.CharField("公司",max_length=20,default=None)

    def __str__(self):
        return "TB内容管理---->" + str(self.ldap)

    class Meta:
        managed = False
        verbose_name_plural = 'TB内容管理'
        db_table = 'tbs'