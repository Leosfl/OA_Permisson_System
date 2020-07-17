import pymysql



def creat_of_mysql():
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='sfl123456', database='for_app02')
    cursur = db.cursor()
    return cursur

def tid_to_route():
    cursur = creat_of_mysql()
    sql_from_oatransferring = "select id,route from oa_transferring"
    cursur.execute(sql_from_oatransferring)
    oa_transferring = dict(cursur.fetchall())
    # print(oa_transferring)
    sql_from_oaapprovergroup = "select id,groupName from oa_approver_group"
    cursur.execute(sql_from_oaapprovergroup)
    oaapprovergroup = dict(cursur.fetchall())
    oaapprovergroup[0] = '结束'
    result = []
    for key, route in oa_transferring.items():
        result.append((int(key), '-'.join([oaapprovergroup[int(value)] for value in route.split("-")])))
    return tuple(result)

def afid_to_formName():
    cursur = creat_of_mysql()
    sql_oa_apply_form = "select id,formName from oa_apply_form"
    cursur.execute(sql_oa_apply_form)
    oa_apply_form = dict(cursur.fetchall())
    # oa_apply_form
    return tuple(oa_apply_form.items())

def workfid_to_route():
    cursur = creat_of_mysql()
    route = dict(tid_to_route())
    sql_work_flow = "select id,tid from oa_work_flow"
    cursur.execute(sql_work_flow)
    id_wid = dict(cursur.fetchall())
    result = {}
    for key, value in id_wid.items():
        result[key] = route[value]
    return tuple(result)

# def get_id_group():
#     sql_from_oaapprovergroup = "select id,groupName from oa_approver_group"
#     cursur.execute(sql_from_oaapprovergroup)
#     oaapprovergroup = dict(cursur.fetchall())
#     oaapprovergroup[0] = '结束'
#     return oaapprovergroup.items()

