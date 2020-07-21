import pymysql



def creat_of_mysql():
    db = pymysql.connect(host='op-servicedb-online', port=3306, user='reimb', password='reimb', database='bx_reimb')
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

def trans_route(route):
    cursur = creat_of_mysql()
    sql_from_oaapprovergroup = "select id,groupName from oa_approver_group"
    cursur.execute(sql_from_oaapprovergroup)
    oaapprovergroup = dict(cursur.fetchall())
    oaapprovergroup[0] = '结束'
    route_list = route.split("-")
    return '-'.join([oaapprovergroup[int(r)] for r in route_list])

def get_second_type():
    cursur = creat_of_mysql()
    sql_from_oafeetype = "SELECT DISTINCT(`subject`)from oa_fee_type"
    cursur.execute(sql_from_oafeetype)
    second_type_map = list(cursur.fetchall())
    result = []
    for second in second_type_map:
        result.append((second[0],second[0]))
    return tuple(result)
    # print(tuple(result))

def get_third_type():
    cursur = creat_of_mysql()
    sql_from_oafeetype = "SELECT DISTINCT(`third`)from oa_fee_type"
    cursur.execute(sql_from_oafeetype)
    second_type_map = list(cursur.fetchall())
    result = []
    for second in second_type_map:
        result.append((second[0],second[0]))
    return tuple(result)
    # print(tuple(result))