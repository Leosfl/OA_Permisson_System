from django.template import Library

from app_02.choice_map import creat_of_mysql




register = Library()

@register.filter
def cut_route(val):
    # return type(val)
    print(type(val))
    if val is None:
        return []
    result = val.split("-")
    return result

@register.filter
def get_dict(val):
    cursur = creat_of_mysql()
    sql_from_oaapprovergroup = "select id,groupName from oa_approver_group"
    cursur.execute(sql_from_oaapprovergroup)
    oaapprovergroup = dict(cursur.fetchall())
    oaapprovergroup[0] = '结束'
    return oaapprovergroup.items()