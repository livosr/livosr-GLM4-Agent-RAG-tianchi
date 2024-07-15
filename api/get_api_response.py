import requests
import json
from cachetools import keys
# 本文件包含24个接口，一个筛选接口和一个提取属性的工具函数
# main中包含了很多很多运行样例，应该是每道题都有
domain = "comm.chatglm.cn"


def get_company_info(query_conds: dict[str, str], need_fields: list[str]) -> dict[str, str]:
    '''
    0
    描述:
        根据上市公司名称、简称或代码查找上市公司信息
    参数:
        query_conds (dict[str, str]): 查询条件的字典,键为'公司名称'或'公司简称'或'公司代码'
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
    返回:
        dict[str, str]: 包含公司信息的字典。
    示例输入:
        get_company_info("query_conds": {"公司名称": "上海妙可蓝多食品科技股份有限公司"}, "need_fields": []})
        get_company_info({"公司名称": "上海妙可蓝多食品科技股份有限公司"},['公司名称','公司简称'])
    示例输出:
        {'公司名称': '上海妙可蓝多食品科技股份有限公司', '公司简称': '妙可蓝多', '英文名称': 'Shanghai Milkground Food Tech Co., Ltd.', '关联证券': '', '公司代码': '600882', '曾用简称': '大成股份>> *ST大成>> 华联矿业>> 广泽股份', '所属市场': '上交所', '所属行业': '食品制造业', '成立日期': '1988-11-29', '上市日期': '1995-12-06', '法人代表': '柴琇', '总经理': '柴琇', '董秘': '谢毅', '邮政编码': '200136', '注册地址': '上海市奉贤区工业路899号8幢', '办公地址': '上海市浦东新区金桥路1398号金台大厦10楼', '联系电话': '021-50188700', '传真': '021-50188918', '官方网址': 'www.milkground.cn', '电子邮箱': 'ir@milkland.com.cn', '入选指数': '国证Ａ指,巨潮小盘', '主营业务': '以奶酪、液态奶为核心的特色乳制品的研发、生产和销售，同时公司也从事以奶粉、黄油为主的乳制品贸易业务。', '经营范围': '许可项目：食品经营；食品互联网销售；互联网直播服务（不含新闻信息服务、网络表演、网络视听节目）；互联网信息服务；进出口代理。（依法须经批准的项目，经相关部门批准后方可开展经营活动，具体经营项目以相关部门批准文件或许可证件为准）。一般项目：乳制品生产技术领域内的技术开发、技术咨询、技术服务、技术转让；互联网销售（除销售需要许可的商品）；互联网数据服务；信息系统集成服务；软件开发；玩具销售。（除依法须经批准的项目外，凭营业执照依法自主开展经营活动）', '机构简介': '公司是1988年11月10日经山东省体改委鲁体改生字(1988)第56号文批准，由山东农药厂发起，采取社会募集方式组建的以公有股份为主体的股份制企业。1988年12月15日,经中国人民银行淄博市分行以淄银字(1988)230号文批准，公开发行股票。 1988年12月经淄博市工商行政管理局批准正式成立山东农药工业股份有限公司(营业执照:16410234)。', '每股面值': '1.0', '首发价格': '1.0', '首发募资净额': '4950.0', '首发主承销商': ''}
        {'公司名称': '上海妙可蓝多食品科技股份有限公司', '公司简称': '妙可蓝多'}
    '''
    url = f"https://{domain}/law_api/s1_b/get_company_info"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "query_conds": query_conds,
        "need_fields": need_fields
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        company_info_dict = rsp.json()
        return company_info_dict
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {}


def get_company_register(query_conds: dict[str, str], need_fields: list[str]) -> dict[str, str]:
    '''
    1
    描述:
        根据公司名称，查询工商信息
    参数:
        query_conds (dict[str, str]): 查询条件的字典,键为'公司名称'
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
    返回:
        dict[str, str]: 包含公司工商信息的字典。
    示例输入:
        get_company_register("query_conds": {"公司名称": "上海妙可蓝多食品科技股份有限公司"}, "need_fields": []})
        get_company_register({"公司名称": "上海妙可蓝多食品科技股份有限公司"},['公司名称','登记状态'])
    示例输出:
        {'公司名称': '上海妙可蓝多食品科技股份有限公司', '登记状态': '存续', '统一社会信用代码': '91370000164102345T', '法定代表人': '柴琇', '注册资本': '51379.1647', '成立日期': '1988-11-29', '企业地址': '上海市奉贤区工业路899号8幢', '联系电话': '021-50185677', '联系邮箱': 'pr@milkground.cn', '注册号': '310000000165830', '组织机构代码': '16410234-5', '参保人数': '370', '行业一级': '科学研究和技术服务业', '行业二级': '科技推广和应用服务业', '行业三级': '其他科技推广服务业', '曾用名': '上海广泽食品科技股份有限公司,\n山东大成农药股份有限公司,\n山东农药工业股份有限公司', '企业简介': '上海妙可蓝多食品科技股份有限公司（简称广泽股份，曾用名：上海广泽食品科技股份有限公司）始创于1998年，总部设在有“东方美谷”之称的上海市奉贤区，系上海证券交易所主板上市公司（证券代码600882）。广泽股份主要生产奶酪和液态奶两大系列产品，拥有“妙可蓝多”“广泽”“澳醇牧场”等国内知名品牌。公司分别在上海、天津、长春和吉林建有4间奶酪和液态奶加工厂，是国内领先的奶酪生产企业。秉承“成为满足国人需求的奶酪专家”的品牌理念，广泽股份一直致力于整合全球资源，为国人提供最好的奶酪产品。公司聘请了一批资深专家加盟，在上海、天津设立了研发中心，并与来自欧洲、澳洲的奶酪公司展开合作，引进了国际先进的生产设备和技术。为从根本上保证产品品质，公司在吉林省建有万头奶牛生态牧场，奶牛全部为进口自澳洲的荷斯坦奶牛，奶质已达欧盟标准。目前，公司可为餐饮和工业客户提供黄油、稀奶油、炼乳、车达和马苏里拉奶酪、奶油芝士、芝士片、芝士酱等产品系列，可直接为消费者提供棒棒奶酪、成长奶酪、三角奶酪、小粒奶酪、新鲜奶酪、慕斯奶酪和辫子奶酪、雪球奶酪等特色产品系列。多年来，广泽股份一直坚持“广纳百川，泽惠四海”的经营理念，恪守“以客户为中心，以奋斗者为本，诚信感恩，务实进取”的核心价值观，努力提高研发和生产技术，不断开发满足消费者需求的奶酪产品，成为深受消费者喜爱的乳品行业知名品牌。', '经营范围': '许可项目：食品经营；食品互联网销售；互联网直播服务（不含新闻信息服务、网络表演、网络视听节目）；互联网信息服务；进出口代理。（依法须经批准的项目，经相关部门批准后方可开展经营活动，具体经营项目以相关部门批准文件或许可证件为准）一般项目：乳制品生产技术领域内的技术开发、技术咨询、技术服务、技术转让；互联网销售（除销售需要许可的商品）；互联网数据服务；信息系统集成服务；软件开发；玩具销售。（除依法须经批准的项目外，凭营业执照依法自主开展经营活动）'}
        {'公司名称': '上海妙可蓝多食品科技股份有限公司', '登记状态': '存续'}
    '''
    url = f"https://{domain}/law_api/s1_b/get_company_register"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "query_conds": query_conds,
        "need_fields": need_fields
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        company_register_dict = rsp.json()
        return company_register_dict
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {}


def get_company_register_name(query_conds: dict[str, str], need_fields: list[str] = []) -> dict[str, str]:
    '''
    2
    描述:
        根据统一社会信用代码查询公司名称
    参数:
        query_conds (dict[str, str]): 查询条件的字典,键为'统一社会信用代码'
        need_fields (list[str]): 在本函数中无用，所以设默认值为[]
    返回:
        dict[str, str]: {'公司名称': str}
    示例输入:
        get_company_register_name({"统一社会信用代码": "913305007490121183"},[])
    示例输出:
        {'公司名称': '天能电池集团股份有限公司'}
    '''
    url = f"https://{domain}/law_api/s1_b/get_company_register_name"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "query_conds": query_conds,
        "need_fields": need_fields
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        company_register_name_dict = rsp.json()
        return company_register_name_dict
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {'公司名称': ''}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {'公司名称': ''}


def get_sub_company_info(query_conds: dict[str, str], need_fields: list[str]) -> dict[str, str]:
    '''
    3
    描述:
        根据被投资的子公司名称获得投资该公司的上市公司、投资比例、投资金额等信息
    参数:
        query_conds (dict[str, str]): 查询条件的字典,键为'公司名称'
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
    返回:
        dict[str, str]: 投资该公司的上市公司、投资比例、投资金额等信息的字典。
    示例输入:
        get_sub_company_info({"公司名称": "上海爱斯达克汽车空调系统有限公司"},[])
        get_sub_company_info({"公司名称": "上海爱斯达克汽车空调系统有限公司"},['关联上市公司全称'])
    示例输出:
        {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '87.5', '上市公司投资金额': '8.54亿', '公司名称': '上海爱斯达克汽车空调系统有限公司'}
        {'关联上市公司全称': '上海航天汽车机电股份有限公司'}
    '''
    url = f"https://{domain}/law_api/s1_b/get_sub_company_info"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "query_conds": query_conds,
        "need_fields": need_fields
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        sub_company_info_dict = rsp.json()
        return sub_company_info_dict
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {}


def get_sub_company_info_list(query_conds: dict[str, str], need_fields: list[str]) -> list[dict[str, str]]:
    '''
    4
    描述:
        根据上市公司（母公司）的名称查询该公司投资的所有子公司信息list
    参数:
        query_conds (dict[str, str]): 查询条件的字典,键为'关联上市公司全称'
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
    返回:
        list[dict[str, str]]: 该公司投资的所有子公司信息list。
    示例输入:
        get_sub_company_info_list({"关联上市公司全称": "上海航天汽车机电股份有限公司"},[])
        get_sub_company_info_list({"关联上市公司全称": "上海航天汽车机电股份有限公司"},['公司名称'])
    示例输出:
        [{'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '8800.00万', '公司名称': '甘肃神舟光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '1.19亿', '公司名称': '甘肃张掖神舟光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '3400.00万', '公司名称': '嘉峪关恒能光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '5600.00万', '公司名称': '金昌太科光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '8700.00万', '公司名称': '喀什太科光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '65.0', '上市公司投资金额': '1296.99万', '公司名称': '科尔沁左翼后旗太科光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '100.00万', '公司名称': '兰坪太科光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '', '公司名称': '兰州恒能光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '81.76', '上市公司投资金额': '2.50亿', '公司名称': '连云港神舟新能源有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '7000.00万', '公司名称': '内蒙古上航新能源有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '95.0', '上市公司投资金额': '1.26亿', '公司名称': '内蒙古神舟光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '100.00万', '公司名称': '丘北太科光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '87.5', '上市公司投资金额': '8.54亿', '公司名称': '上海爱斯达克汽车空调系统有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '3.41亿', '公司名称': '上海能航机电发展有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '51.0', '上市公司投资金额': '2040.00万', '公司名称': '上饶市太科光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '1600.00万', '公司名称': '威海浩阳光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '59.4', '上市公司投资金额': '2620.00万', '公司名称': '文山太科光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '1.45亿', '公司名称': '阳泉太科光伏电力有限公司'}]
        [{'公司名称': '甘肃神舟光伏电力有限公司'}, {'公司名称': '甘肃张掖神舟光伏电力有限公司'}, {'公司名称': '嘉峪关恒能光伏电力有限公司'}, {'公司名称': '金昌太科光伏电力有限公司'}, {'公司名称': '喀什太科光伏电力有限公司'}, {'公司名称': '科尔沁左翼后旗太科光伏电力有限公司'}, {'公司名称': '兰坪太科光伏电力有限公司'}, {'公司名称': '兰州恒能光伏电力有限公司'}, {'公司名称': '连云港神舟新能源有限公司'}, {'公司名称': '内蒙古上航新能源有限公司'}, {'公司名称': '内蒙古神舟光伏电力有限公司'}, {'公司名称': '丘北太科光伏电力有限公司'}, {'公司名称': '上海爱斯达克汽车空调系统有限公司'}, {'公司名称': '上海能航机电发展有限公司'}, {'公司名称': '上饶市太科光伏电力有限公司'}, {'公司名称': '威海浩阳光伏电力有限公司'}, {'公司名称': '文山太科光伏电力有限公司'}, {'公司名称': '阳泉太科光伏电力有限公司'}]
    '''
    url = f"https://{domain}/law_api/s1_b/get_sub_company_info_list"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "query_conds": query_conds,
        "need_fields": need_fields
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        sub_company_info_list = rsp.json()
        return sub_company_info_list
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return [{}]
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return [{}]


def get_legal_document(query_conds: dict[str, str], need_fields: list[str]) -> dict[str, str]:
    '''
    5
    描述:
        根据案号查询裁判文书相关信息,现在返回列表多一个表项"起诉日期"
    参数:
        query_conds (dict[str, str]): 查询条件的字典,键为'案号'
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
    返回:
        dict[str, str]: 裁判文书相关信息的字典。
    示例输入:
        get_legal_document({"案号": "(2019)沪0115民初61975号"},[]
        get_legal_document({"案号": "(2019)沪0115民初61975号"},['关联公司','标题']
    示例输出:
        {'关联公司': '上海爱斯达克汽车空调系统有限公司', '标题': '上海爱斯达克汽车空调系统有限公司与上海逸测检测技术服务有限公司服务合同纠纷一审民事判决书', '案号': '(2019)沪0115民初61975号', '文书类型': '民事判决书', '原告': '上海爱斯达克汽车空调系统有限公司', '被告': '上海逸测检测技术服务有限公司', '原告律师事务所': '', '被告律师事务所': '上海世韬律师事务所', '案由': '服务合同纠纷', '涉案金额': '1254802.58', '判决结果': '一、被告上海逸测检测技术服务有限公司应于本判决生效之日起十日内支付原告上海爱斯达克汽车空调系统有限公司测试费1,254,802.58元; \\n \\n二、被告上海逸测检测技术服务有限公司应于本判决生效之日起十日内支付原告上海爱斯达克汽车空调系统有限公司违约金71,399.68元 。  \\n \\n负有金钱给付义务的当事人如未按本判决指定的期间履行给付金钱义务,应当依照《中华人民共和国民事诉讼法》第二百五十三条之规定,加倍支付迟延履行期间的债务利息 。  \\n \\n案件受理费16,736元,减半收取计8,368元,由被告上海逸测检测技术服务有限公司负担 。  \\n \\n如不服本判决,可在判决书送达之日起十五日内向本院递交上诉状,并按对方当事人的人数提出副本,上诉于上海市第一中级人民法院 。 ', '日期': '2019-12-09 00:00:00', '文件名': '（2019）沪0115民初61975号.txt'}
        {'关联公司': '上海爱斯达克汽车空调系统有限公司', '标题': '上海爱斯达克汽车空调系统有限公司与上海逸测检测技术服务有限公司服务合同纠纷一审民事判决书'}
    '''
    url = f"https://{domain}/law_api/s1_b/get_legal_document"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "query_conds": query_conds,
        "need_fields": need_fields
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        legal_document_dict = rsp.json()
        legal_document_dict["起诉日期"] = legal_document_dict["案号"][1:5]  # 添加进字典
        return legal_document_dict
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {}


def get_legal_document_list(query_conds: dict[str, str], need_fields: list[str]) -> list[dict[str, str]]:
    '''
    6
    描述:
        根据关联公司查询所有裁判文书相关信息list，现在返回列表多一个表项"起诉日期"
    参数:
        query_conds (dict[str, str]): 查询条件的字典,键为'关联公司'
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
    返回:
        list[dict[str, str]]: 所有裁判文书相关信息list。
    示例输入:
        get_legal_document_list({"关联公司": "上海爱斯达克汽车空调系统有限公司"},[])
        get_legal_document_list({"关联公司": "上海爱斯达克汽车空调系统有限公司"},['案号','原告律师事务所','被告律师事务所','涉案金额','日期'])
    示例输出:
        [{'关联公司': '上海爱斯达克汽车空调系统有限公司', '标题': '上海爱斯达克汽车空调系统有限公司与上海逸测检测技术服务有限公司服务合同纠纷一审民事判决书', '案号': '(2019)沪0115民初61975号', '文书类型': '民事判决书', '原告': '上海爱斯达克汽车空调系统有限公司', '被告': '上海逸测检测技术服务有限公司', '原告律师事务所': '', '被告律师事务所': '上海世韬律师事务所', '案由': '服务合同纠纷', '涉案金额': '1254802.58', '判决结果': '一、被告上海逸测检测技术服务有限公司应于本判决生效之日起十日内支付原告上海爱斯达克汽车空调系统有限公司测试费1,254,802.58元; \\n \\n二、被告上海逸测检测技术服务有限公司应于本判决生效之日起十日内支付原告上海爱斯达克汽车空调系统有限公司违约金71,399.68元 。  \\n \\n负有金钱给付义务的当事人如未按本判决指定的期间履行给付金钱义务,应当依照《中华人民共和国民事诉讼法》第二百五十三条之规定,加倍支付迟延履行期间的债务利息 。  \\n \\n案件受理费16,736元,减半收取计8,368元,由被告上海逸测检测技术服务有限公司负担 。  \\n \\n如不服本判决,可在判决书送达之日起十五日内向本院递交上诉状,并按对方当事人的人数提出副本,上诉于上海市第一中级人民法院 。 ', '日期': '2019-12-09 00:00:00', '文件名': '（2019）沪0115民初61975号.txt'}, {'关联公司': '上海爱斯达克汽车空调系统有限公司', '标题': '吴某某与上海爱斯达克汽车空调系统有限公司追索劳动报酬纠纷一审民事判决书', '案号': '(2019)沪0115民初91149号', '文书类型': '民事判决书', '原告': '吴某某', '被告': '上海爱斯达克汽车空调系统有限公司', '原告律师事务所': '上海国策律师事务所', '被告律师事务所': '上海市罗顿律师事务所', '案由': '追索劳动报酬纠纷', '涉案金额': '0', '判决结果': '一、被告上海爱斯达克汽车空调系统有限公司于本判决生效之日起十日内支付原告吴某某2019年4月1日至2019年5月31日期间延时加班工资差额9,094.50元; \\n \\n二、驳回原告吴某某的其余诉讼请求 。  \\n \\n负有金钱给付义务的当事人,如果未按本判决指定的期间履行给付金钱义务,应当依照《中华人民共和国民事诉讼法》第二百五十三条之规定,加倍支付迟延履行期间的债务利息 。  \\n \\n案件受理费10元,减半计5元,免予收取 。  \\n \\n如不服本判决,可在判决书送达之日起十五日内,向本院递交上诉状,并按对方当事人的人数提出副本,上诉于上海市第一中级人民法院 。 ', '日期': '2020-01-20 00:00:00', '文件名': '（2019）沪0115民初91149号.txt'}, {'关联公司': '上海爱斯达克汽车空调系统有限公司', '标题': '上海贝众汽车零部件有限公司与上海爱斯达克汽车空调系统有限公司技术委托开发合同纠纷民事一审案件民事判决书', '案号': '(2020)沪0115民初3857号', '文书类型': '民事判决书', '原告': '上海贝众汽车零部件有限公司', '被告': '上海爱斯达克汽车空调系统有限公司', '原告律师事务所': '上海远同律师事务所', '被告律师事务所': '上海步界律师事务所', '案由': '技术委托开发合同纠纷', '涉案金额': '21849', '判决结果': '一、被告上海爱斯达克汽车空调系统有限公司于本判决生效之日起十日内支付原告上海贝众汽车零部件有限公司差旅费21,849元; \\n \\n二、驳回原告上海贝众汽车零部件有限公司的其余诉讼请求 。  \\n \\n如果未按本判决指定的期间履行给付义务,应当依照《中华人民共和国民事诉讼法》第二百五十三条的规定,加倍支付迟延履行期间的债务利息 。  \\n \\n案件受理费14,225元,由原告上海贝众汽车零部件有限公司负担9,225元,被告上海爱斯达克汽车空调系统有限公司负担5,000元 。  \\n \\n如不服本判决,可在判决书送达之日起十五日内,向本院递交上诉状,并按照对方当事人或者代表人的人数提出副本,上诉于上海知识产权法院 。 ', '日期': '2021-04-28 00:00:00', '文件名': '（2020）沪0115民初3857号.txt'}]
        [{'案号': '(2019)沪0115民初61975号', '原告律师事务所': '', '被告律师事务所': '上海世韬律师事务所', '涉案金额': '1254802.58', '日期': '2019-12-09 00:00:00'}, {'案号': '(2019)沪0115民初91149号', '原告律师事务所': '上海国策律师事务所', '被告律师事务所': '上海市罗顿律师事务所', '涉案金额': '0', '日期': '2020-01-20 00:00:00'}, {'案号': '(2020)沪0115民初3857号', '原告律师事务所': '上海远同律师事务所', '被告律师事务所': '上海步界律师事务所', '涉案金额': '21849', '日期': '2021-04-28 00:00:00'}]
    '''
    url = f"https://{domain}/law_api/s1_b/get_legal_document_list"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "query_conds": query_conds,
        "need_fields": need_fields
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        legal_document_list = rsp.json()
        qisu_date_list = []
        for case in legal_document_list:
            qisu_date_list.append(case["案号"][1:5])     # 获取起诉日期
            case["起诉日期"] = qisu_date_list[-1]     # 添加进字典
        return legal_document_list
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return [{}]
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return [{}]


def get_court_info(query_conds: dict[str, str], need_fields: list[str]) -> dict[str, str]:
    '''
    7
    描述:
        根据法院名称查询法院名录相关信息
    参数:
        query_conds (dict[str, str]): 查询条件的字典,键为'法院名称'
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
    返回:
        dict[str, str]: 法院名录相关信息的字典。
    示例输入:
        get_court_info({"法院名称": "上海市浦东新区人民法院"},[])
        get_court_info({"法院名称": "上海市浦东新区人民法院"},['法院地址','法院联系电话'])
    示例输出:
        {'法院名称': '上海市浦东新区人民法院', '法院负责人': '朱丹', '成立日期': '2019-05-16', '法院地址': '上海市浦东新区丁香路611号', '法院联系电话': '-', '法院官网': '-'}
        {'法院地址': '上海市浦东新区丁香路611号', '法院联系电话': '-'}
   '''
    url = f"https://{domain}/law_api/s1_b/get_court_info"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "query_conds": query_conds,
        "need_fields": need_fields
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        court_info_dict = rsp.json()
        return court_info_dict
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {}


def get_court_code(query_conds: dict[str, str], need_fields: list[str]) -> dict[str, str]:
    '''
    8
    描述:
        根据法院名称或者法院代字查询法院代字等相关数据
    参数:
        query_conds (dict[str, str]): 查询条件的字典,键为'法院名称'或'法院代字'
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
    返回:
        dict[str, str]: 法院代字等相关数据的字典。
    示例输入:
        get_court_code({"法院名称": "上海市浦东新区人民法院"},[])
        get_court_code({"法院名称": "上海市浦东新区人民法院"},['法院代字','法院级别'])
        get_court_code({'法院代字': '沪0115'},[])
    示例输出:
        {'法院名称': '上海市浦东新区人民法院', '行政级别': '市级', '法院级别': '基层法院', '法院代字': '沪0115', '区划代码': '310115', '级别': '1'}
        {'法院代字': '沪0115', '法院级别': '基层法院'}
        {'法院名称': '上海市浦东新区人民法院', '行政级别': '市级', '法院级别': '基层法院', '法院代字': '沪0115', '区划代码': '310115', '级别': '1'}
   '''
    url = f"https://{domain}/law_api/s1_b/get_court_code"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "query_conds": query_conds,
        "need_fields": need_fields
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        court_code_dict = rsp.json()
        return court_code_dict
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {}


def get_lawfirm_info(query_conds: dict[str, str], need_fields: list[str]) -> dict[str, str]:
    '''
    9
    描述:
        根据律师事务所查询律师事务所名录
    参数:
        query_conds (dict[str, str]): 查询条件的字典,键为'律师事务所名称'
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
    返回:
        dict[str, str]: 律师事务所名录的字典。
    示例输入:
        get_lawfirm_info({"律师事务所名称": "爱德律师事务所"},[])
        get_lawfirm_info({"律师事务所名称": "爱德律师事务所"},['律所登记机关','律师事务所唯一编码'])
    示例输出:
        {'律师事务所名称': '爱德律师事务所', '律师事务所唯一编码': '31150000E370803331', '律师事务所负责人': '巴布', '事务所注册资本': '10万元人民币', '事务所成立日期': '1995-03-14', '律师事务所地址': '呼和浩特市赛罕区大学西街110号丰业大厦11楼', '通讯电话': '0471-3396155', '通讯邮箱': 'kehufuwubu@ardlaw.cn', '律所登记机关': '内蒙古自治区呼和浩特市司法局'}
        {'律所登记机关': '内蒙古自治区呼和浩特市司法局', '律师事务所唯一编码': '31150000E370803331'}
   '''
    url = f"https://{domain}/law_api/s1_b/get_lawfirm_info"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "query_conds": query_conds,
        "need_fields": need_fields
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        lawfirm_info_dict = rsp.json()
        return lawfirm_info_dict
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {}


def get_lawfirm_log(query_conds: dict[str, str], need_fields: list[str]) -> dict[str, str]:
    '''
    10
    描述:
        根据律师事务所查询律师事务所统计数据
    参数:
        query_conds (dict[str, str]): 查询条件的字典,键为'律师事务所名称'
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
    返回:
        dict[str, str]: 律师事务所统计数据的字典。
    示例输入:
        get_lawfirm_log({"律师事务所名称": "北京市金杜律师事务所"},[])
    示例输出:
        {'律师事务所名称': '北京市金杜律师事务所', '业务量排名': '2', '服务已上市公司': '68', '报告期间所服务上市公司违规事件': '23', '报告期所服务上市公司接受立案调查': '3'}
   '''
    url = f"https://{domain}/law_api/s1_b/get_lawfirm_log"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "query_conds": query_conds,
        "need_fields": need_fields
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        lawfirm_log_dict = rsp.json()
        return lawfirm_log_dict
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {}


def get_address_info(query_conds: dict[str, str], need_fields: list[str]) -> dict[str, str]:
    '''
    11
    描述:
        根据地址查该地址对应的省份城市区县
    参数:
        query_conds (dict[str, str]): 查询条件的字典,键为'地址'
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
    返回:
        dict[str, str]: 该地址对应的省份城市区县的字典。
    示例输入:
        get_address_info({"地址": "西藏自治区那曲地区安多县帕那镇中路13号"},[])
    示例输出:
        {'地址': '西藏自治区那曲地区安多县帕那镇中路13号', '省份': '西藏自治区', '城市': '那曲市', '区县': '安多县'}
   '''
    url = f"https://{domain}/law_api/s1_b/get_address_info"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "query_conds": query_conds,
        "need_fields": need_fields
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        address_info_dict = rsp.json()
        return address_info_dict
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {}


def get_address_code(query_conds: dict[str, str], need_fields: list[str]) -> dict[str, str]:
    '''
    12
    描述:
        根据省市区查询区划代码，会返回两个码：城市区划代码，区县区划代码
    参数:
        query_conds (dict[str, str]): 要查询代码的省市区字典（三个条件缺一不可）
        need_fields (list[str]): 这里默认是空的
    返回:
        dict[str, str] 包含省市区信息，城市区划代码，区县区划代码
    示例输入:
        get_address_code({"省份": "西藏自治区", "城市": "拉萨市", "区县": "城关区"}, [])
    示例输出:
        {'省份': '西藏自治区', '城市': '拉萨市', '城市区划代码': '540100000000', '区县': '城关区', '区县区划代码': '540102000000'}
    '''
    url = f"https://{domain}/law_api/s1_b/get_address_code"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "query_conds": query_conds,
        "need_fields": need_fields
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        address_code = rsp.json()
        return address_code
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {}


def get_temp_info(query_conds: dict[str, str], need_fields: list[str]) -> dict[str, str]:
    '''
    13
    描述:
        根据日期及省份城市查询天气相关信息
    参数:
        query_conds (dict[str, str]): 要查询天气的省份，城市，日期字典（三个条件缺一不可）
        need_fields (list[str]): 这里默认是空的
    返回:
        dict[str, str] 包含日期，省份，城市，天气，最高温度，最低温度，湿度
    示例输入:
        get_temp_info({"省份": "北京市", "城市": "北京市", "日期": "2020年1月1日"}, [])
    示例输出:
        {'日期': '2020年1月1日', '省份': '北京市', '城市': '北京市', '天气': '晴', '最高温度': '11', '最低温度': '1', '湿度': '55'}
    '''
    url = f"https://{domain}/law_api/s1_b/get_temp_info"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "query_conds": query_conds,
        "need_fields": need_fields
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        temp_info = rsp.json()
        return temp_info
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {}


def get_legal_abstract(query_conds: dict[str, str], need_fields: list[str]) -> dict[str, str]:
    '''
    14
    描述:
        根据案号查询文本摘要
    参数:
        query_conds (dict[str, str]): 案号
        need_fields (list[str]): 这里默认是空的
    返回:
        dict[str, str] 包含文件名，文本摘要，案号
    示例输入:
        get_legal_abstract({"案号": "（2019）沪0115民初61975号"}, [])
    示例输出:
        {'文件名': '（2019）沪0115民初61975号.txt', '案号': '（2019）沪0115民初61975号', '文本摘要': '原告上海爱斯达克汽车空调系统有限公司与被告上海逸测检测技术服务有限公司因服务合同纠纷一案，原告请求被告支付检测费1,254,802.58元、延迟履行违约金71,399.68元及诉讼费用。被告辩称，系争合同已终止，欠款金额应为499,908元，且不认可违约金。\n法院认为，原告与腾双公司签订的测试合同适用于原被告，原告提供的测试服务应得到被告支付。依照《中华人民共和国合同法》第六十条、第一百零九条,《中华人民共和国民事诉讼法》第六十四条第一款,《最高人民法院关于适用〈中华人民共和国民事诉讼法〉的解释》第九十条之规定判决被告支付原告检测费1,254,802.58元及违约金71,399.68元。'}
    '''
    url = f"https://{domain}/law_api/s1_b/get_legal_abstract"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "query_conds": query_conds,
        "need_fields": need_fields
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        abstract = rsp.json()
        return abstract
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {}


def get_xzgxf_info(query_conds: dict[str, str], need_fields: list[str]) -> dict[str, str]:
    '''
    15
    描述:
        根据案号查询限制高消费相关信息
    参数:
        query_conds (dict[str, str]): 案号
        need_fields (list[str]): 这里默认是空的
    返回:
        dict[str, str] 包含限制高消费企业名称，案号，法定代表人，申请人，涉案金额，执行法院，立案日期，限高发布日期
    示例输入:
        get_xzgxf_info({"案号": "（2018）鲁0403执1281号"}, [])
    示例输出:
        {'限制高消费企业名称': '枣庄西能新远大天然气利用有限公司',
        '案号': '（2018）鲁0403执1281号',
        '法定代表人': '高士其',
        '申请人': '枣庄市人力资源和社会保障局',
        '涉案金额': '12000',
        '执行法院': '山东省枣庄市薛城区人民法院',
        '立案日期': '2018-11-16 00:00:00',
        '限高发布日期': '2019-02-13 00:00:00'}
    '''
    url = f"https://{domain}/law_api/s1_b/get_xzgxf_info"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "query_conds": query_conds,
        "need_fields": need_fields
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        xzgxf_info = rsp.json()
        return xzgxf_info
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {}


def get_xzgxf_info_list(query_conds: dict[str, str], need_fields: list[str]) -> list[dict[str, str]]:
    '''
    16
    描述:
        根据企业名称查询所有限制高消费相关信息list
        （也就是说一个企业可能有多条限制高消费相关信息)
    参数:
        query_conds (dict[str, str]): 企业名称
        need_fields (list[str]): 这里默认是空的
    返回:
        list[dict]，一个dict代表一条高消费信息
    示例输入:
        get_xzgxf_info_list({"限制高消费企业名称": "欣水源生态环境科技有限公司"}, [])
    示例输出:
        [{'限制高消费企业名称': '欣水源生态环境科技有限公司',
        '案号': '（2023）黔2731执恢130号',
        '法定代表人': '刘福云',
        '申请人': '四川省裕锦建设工程有限公司惠水分公司',
        '涉案金额': '7500000',
        '执行法院': '贵州省黔南布依族苗族自治州惠水县人民法院',
        '立案日期': '2023-08-04 00:00:00',
        '限高发布日期': '2023-11-09 00:00:00'}]
    '''
    url = f"https://{domain}/law_api/s1_b/get_xzgxf_info_list"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "query_conds": query_conds,
        "need_fields": need_fields
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        xzgxf_info_list = rsp.json()
        if isinstance(xzgxf_info_list, dict):
            xzgxf_info_list = [xzgxf_info_list]
        return xzgxf_info_list
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {}


def get_sum(nums: list[int] or list[float] or list[str]):
    '''
    17
    描述:
        求和，可以对传入的int、float、str数组进行求和，str数组只能转换字符串里的千万亿，如"1万"
        int和float可以直接相加，str的只能和str相加
    参数:
        nums[int or float or str] 三种输入
    返回:
        int or float 取决于输入类型
    示例输入:
        get_sum([1,2,3,4,5])
        get_sum(["1", "2", "3", "4", "5"])
        get_sum(["1万", "1亿", "2千"])
    示例输出:
        15
        15
        100012000.0
    '''
    url = f"https://{domain}/law_api/s1_b/get_sum"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = nums

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        sum = rsp.json()
        return sum
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {}


def rank(dict: dict[str, str], is_desc: bool = False) -> list[any]:
    '''
    18
    描述:
        排序接口，返回按照values排序的keys
    参数:
        dict  要排序的字典
        is_desc: bool = False   是否降序
        其中dict包括：
        keys: list[any]   排序字段对应的键
        values: list[float]   排序字段的值
    返回:
        list[any]  返回排序后的键列表
    示例输入:
        rank({"keys": ["a", "b", "c"], "values": [2, 1, 3]})
    示例输出:
        ['b', 'a', 'c']
    '''
    url = f"https://{domain}/law_api/s1_b/rank"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "keys": dict["keys"],
        "values": dict["values"],
        "is_desc": is_desc
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        list = rsp.json()
        return list
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {}


def save_dict_list_to_word(company_name: str, dict_list: str):
    '''
    19
    描述:
        通过传入结构化信息，制作生成公司数据报告（demo）
    参数:
        company_name: str,     公司名称
        dict_list: str      一整个大字符串，包含数据信息的字典
    返回:
        无
    示例输入:
    示例输出:
    '''
    url = f"https://{domain}/law_api/s1_b/save_dict_list_to_word"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = {
        "company_name": company_name,
        "dict_list": dict_list
    }

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        print(rsp.text)

    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return {}
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return {}


def get_citizens_sue_citizens(data: dict[str, str])->str:
    '''
    20
    描述:
        民事起诉状(公民起诉公民)
    参数:
        data: dict[str, str]: 传入的民事起诉状(公民起诉公民)的字典信息
    返回:
        str: 民事起诉状(公民起诉公民)。
    示例输入:
        get_citizens_sue_citizens({ '原告': '张三', '原告性别': '男', '原告生日': '1976-10-2', '原告民族': '汉', '原告工作单位': 'XXX', '原告地址': '中国', '原告联系方式': '123456', '原告委托诉讼代理人': '李四', '原告委托诉讼代理人联系方式': '421313', '被告': '王五', '被告性别': '女', '被告生日': '1975-02-12', '被告民族': '汉', '被告工作单位': 'YYY', '被告地址': '江苏', '被告联系方式': '56354321', '被告委托诉讼代理人': '赵六', '被告委托诉讼代理人联系方式': '09765213', '诉讼请求': 'AA纠纷', '事实和理由': '上诉', '证据': 'PPPPP', '法院名称': '最高法', '起诉日期': '2012-09-08' })
    示例输出:
        "民事起诉状（公民起诉公民）\n原告：张三，性别：男，出生日期：1976-10-2，民族：汉，工作单位：XXX，地址：中国，联系方式：123456。\n原告委托诉讼代理人：李四，联系方式：421313。\n被告：王五，性别：女，出生日期：1975-02-12，民族：汉，工作单位：YYY，地址：江苏，联系方式：56354321。\n被告委托诉讼代理人：赵六，联系方式：09765213。\n诉讼请求：\nAA纠纷\n事实和理由：\n上诉\n证据和证据来源，证人姓名和住所：\nPPPPP\n此致\n最高法\n\n附:本起诉状副本x份\n\n起诉人(签名)\n2012-09-08"
   '''
    url = f"https://{domain}/law_api/s1_b/get_citizens_sue_citizens"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = data

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        citizens_sue_citizens_str = rsp.text
        return citizens_sue_citizens_str
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return ''
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return ''


def get_company_sue_citizens(data: dict[str, str])->str:
    '''
    21
    描述:
        民事起诉状(公司起诉公民)
    参数:
        data: dict[str, str]: 传入的民事起诉状(公司起诉公民)的字典信息
    返回:
        str: 民事起诉状(公司起诉公民)。
    示例输入:
        get_company_sue_citizens({ '原告': '上海公司', '原告地址': '上海', '原告法定代表人': '张三', '原告联系方式': '872638', '原告委托诉讼代理人': 'B律师事务所', '原告委托诉讼代理人联系方式': '5678900', '被告': '王五', '被告性别': '女', '被告生日': '1975-02-12', '被告民族': '汉', '被告工作单位': 'YYY', '被告地址': '江苏', '被告联系方式': '56354321', '被告委托诉讼代理人': '赵六', '被告委托诉讼代理人联系方式': '09765213', '诉讼请求': 'AA纠纷', '事实和理由': '上诉', '证据': 'PPPPP', '法院名称': '最高法', '起诉日期': '2012-09-08' })
    示例输出:
        "民事起诉状（公司起诉公民）\n原告：上海公司，地址：上海。法定代表人（负责人）：张三，联系方式：872638。\n原告委托诉讼代理人：B律师事务所，联系方式：5678900。\n被告：王五，性别：女，出生日期：1975-02-12，民族：汉，工作单位：YYY，地址：江苏，联系方式：56354321。\n被告委托诉讼代理人：赵六，联系方式：09765213。\n诉讼请求：\nAA纠纷\n事实和理由：\n上诉\n证据和证据来源，证人姓名和住所：\nPPPPP\n此致\n最高法\n\n附:本起诉状副本x份\n\n起诉人(签名)\n2012-09-08"
   '''
    url = f"https://{domain}/law_api/s1_b/get_company_sue_citizens"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = data

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        company_sue_citizens_str = rsp.text
        return company_sue_citizens_str
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return ''
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return ''

def get_citizens_sue_company(data: dict[str, str])->str:
    '''
    22
    描述:
        民事起诉状(公民起诉公司)
    参数:
        data: dict[str, str]: 传入的民事起诉状(公民起诉公司)的字典信息
    返回:
        str: 民事起诉状(公民起诉公司)。
    示例输入:
        get_citizens_sue_company({ '原告': '张三', '原告性别': '男', '原告生日': '1976-10-2', '原告民族': '汉', '原告工作单位': 'XXX', '原告地址': '中国', '原告联系方式': '123456', '原告委托诉讼代理人': '李四', '原告委托诉讼代理人联系方式': '421313', '被告': '王五公司', '被告地址': '公司地址', '被告法定代表人': '赵四', '被告联系方式': '98766543', '被告委托诉讼代理人': 'C律师事务所', '被告委托诉讼代理人联系方式': '425673398', '诉讼请求': 'AA纠纷', '事实和理由': '上诉', '证据': 'PPPPP', '法院名称': '最高法', '起诉日期': '2012-09-08' })
    示例输出:
        "民事起诉状（公民起诉公司）\n原告：张三，性别：男，出生日期：1976-10-2，民族：汉，工作单位：XXX，地址：中国，联系方式：123456。\n原告委托诉讼代理人：李四，联系方式：421313。\n被告：王五公司，地址：公司地址。法定代表人（负责人）：赵四，联系方式：98766543。\n被告委托诉讼代理人：C律师事务所，联系方式：425673398。\n诉讼请求：\nAA纠纷\n事实和理由：\n上诉\n证据和证据来源，证人姓名和住所：\nPPPPP\n此致\n最高法\n\n附:本起诉状副本x份\n\n起诉人(签名)\n2012-09-08"
   '''
    url = f"https://{domain}/law_api/s1_b/get_citizens_sue_company"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = data

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        citizens_sue_company_str = rsp.text
        return citizens_sue_company_str
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return ''
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return ''


def get_company_sue_company(data: dict[str, str])->str:
    '''
    23
    描述:
        民事起诉状(公司起诉公司)
    参数:
        data: dict[str, str]: 传入的民事起诉状(公司起诉公司)的字典信息
    返回:
        str: 民事起诉状(公司起诉公司)。
    示例输入:
        get_company_sue_company({ '原告': '上海公司', '原告地址': '上海', '原告法定代表人': '张三', '原告联系方式': '872638', '原告委托诉讼代理人': 'B律师事务所', '原告委托诉讼代理人联系方式': '5678900', '被告': '王五公司', '被告地址': '公司地址', '被告法定代表人': '赵四', '被告联系方式': '98766543', '被告委托诉讼代理人': 'C律师事务所', '被告委托诉讼代理人联系方式': '425673398', '诉讼请求': 'AA纠纷', '事实和理由': '上诉', '证据': 'PPPPP', '法院名称': '最高法', '起诉日期': '2012-09-08' })
    示例输出:
        "民事起诉状（公司起诉公司）\n原告：上海公司，地址：上海。法定代表人（负责人）：张三，联系方式：872638。\n原告委托诉讼代理人：B律师事务所，联系方式：5678900。\n被告：王五公司，地址：公司地址。法定代表人（负责人）：赵四，联系方式：98766543。\n被告委托诉讼代理人：C律师事务所，联系方式：425673398。\n诉讼请求：\nAA纠纷\n事实和理由：\n上诉\n证据和证据来源，证人姓名和住所：\nPPPPP\n此致\n最高法\n\n附:本起诉状副本x份\n\n起诉人(签名)\n2012-09-08"
   '''
    url = f"https://{domain}/law_api/s1_b/get_company_sue_company"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer F7B3620F2977B362DC1E2889C9D495A93543CA87F67219E8'
    }
    data = data

    try:
        # 发送POST请求
        rsp = requests.post(url, json=data, headers=headers)
        rsp.raise_for_status()  # 检查HTTP请求是否成功
        company_sue_company_str = rsp.text
        return company_sue_company_str
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(f"请求错误: {e}")
        return ''
    except ValueError as e:
        # JSON解码错误处理
        print(f"JSON解码错误: {e}")
        return ''


def find_all_attribute(attrs: dict[str, str] or list[dict[str, str]]) -> list[str]:
    if isinstance(attrs, list):
        attrs = attrs[0]
    attr_keys = list(attrs.keys())
    return attr_keys


# 一个通用性很强的筛选接口！
def filter_(input_list: list[dict], input_info: list[dict]):
    # input_list = [{"属性名称1": {"判别类别": '大于小于等于或其他', '判断条件':[]}}, {"属性名称2": {"判别类别": '大于小于等于或其他', '判断条件':[]}}...]
    # input_info = [{"属性名称1": "", "属性名称2": "",...,},{"属性名称1": "", "属性名称2": "",...,},...,] 待筛选的数据
    new_info_list = []
    for i, attr in enumerate(input_list):
        if i != 0:
            input_info = new_info_list
        new_info_list = []
        for attr_name, attr_control in attr.items():
            if isinstance(attr_control['判断条件'][0], str):        # 如果是字符串就转换成int
                attr_control['判断条件'][0] = int(attr_control['判断条件'][0])
            if attr_control['判别类别'] == '大于':
                for info_dict in input_info:
                    if float(info_dict[attr_name]) > attr_control['判断条件'][0]:
                        new_info_list.append(info_dict)
            elif attr_control['判别类别'] == '等于':
                for info_dict in input_info:
                    if float(info_dict[attr_name]) == attr_control['判断条件'][0]:
                        new_info_list.append(info_dict)
            elif attr_control['判别类别'] == '小于':
                for info_dict in input_info:
                    if float(info_dict[attr_name]) < attr_control['判断条件'][0]:
                        new_info_list.append(info_dict)
            elif attr_control['判别类别'] == '区间':
                for info_dict in input_info:
                    sorted(attr_control['判断条件'])
                    if attr_control['判断条件'][0] < float(info_dict[attr_name]) < attr_control['判断条件'][1]:
                        new_info_list.append(info_dict)
            else:
                raise Exception("未定义的判别类别！")
    return new_info_list


if __name__ == '__main__':
    # print("get_company_info:")
    # print(get_company_info({"公司名称": "上海妙可蓝多食品科技股份有限公司"}, []))
    # print(find_all_attribute(get_company_info({"公司名称": "上海妙可蓝多食品科技股份有限公司"}, [])))
    # # 输出：{'公司名称': '上海妙可蓝多食品科技股份有限公司', '公司简称': '妙可蓝多', '英文名称': 'Shanghai Milkground Food Tech Co., Ltd.', '关联证券': '', '公司代码': '600882', '曾用简称': '大成股份>> *ST大成>> 华联矿业>> 广泽股份', '所属市场': '上交所', '所属行业': '食品制造业', '成立日期': '1988-11-29', '上市日期': '1995-12-06', '法人代表': '柴琇', '总经理': '柴琇', '董秘': '谢毅', '邮政编码': '200136', '注册地址': '上海市奉贤区工业路899号8幢', '办公地址': '上海市浦东新区金桥路1398号金台大厦10楼', '联系电话': '021-50188700', '传真': '021-50188918', '官方网址': 'www.milkground.cn', '电子邮箱': 'ir@milkland.com.cn', '入选指数': '国证Ａ指,巨潮小盘', '主营业务': '以奶酪、液态奶为核心的特色乳制品的研发、生产和销售，同时公司也从事以奶粉、黄油为主的乳制品贸易业务。', '经营范围': '许可项目：食品经营；食品互联网销售；互联网直播服务（不含新闻信息服务、网络表演、网络视听节目）；互联网信息服务；进出口代理。（依法须经批准的项目，经相关部门批准后方可开展经营活动，具体经营项目以相关部门批准文件或许可证件为准）。一般项目：乳制品生产技术领域内的技术开发、技术咨询、技术服务、技术转让；互联网销售（除销售需要许可的商品）；互联网数据服务；信息系统集成服务；软件开发；玩具销售。（除依法须经批准的项目外，凭营业执照依法自主开展经营活动）', '机构简介': '公司是1988年11月10日经山东省体改委鲁体改生字(1988)第56号文批准，由山东农药厂发起，采取社会募集方式组建的以公有股份为主体的股份制企业。1988年12月15日,经中国人民银行淄博市分行以淄银字(1988)230号文批准，公开发行股票。 1988年12月经淄博市工商行政管理局批准正式成立山东农药工业股份有限公司(营业执照:16410234)。', '每股面值': '1.0', '首发价格': '1.0', '首发募资净额': '4950.0', '首发主承销商': ''}
    # # 全部属性：['公司名称', '公司简称', '英文名称', '关联证券', '公司代码', '曾用简称', '所属市场', '所属行业', '成立日期', '上市日期', '法人代表', '总经理', '董秘', '邮政编码', '注册地址', '办公地址', '联系电话', '传真', '官方网址', '电子邮箱', '入选指数', '主营业务', '经营范围', '机构简介', '每股面值', '首发价格', '首发募资净额', '首发主承销商']
    # print("get_company_register:")
    # print(get_company_register({"公司名称": "上海妙可蓝多食品科技股份有限公司"}, []))
    # print(find_all_attribute(get_company_register({"公司名称": "上海妙可蓝多食品科技股份有限公司"}, [])))
    # # 输出：{'公司名称': '上海妙可蓝多食品科技股份有限公司', '登记状态': '存续', '统一社会信用代码': '91370000164102345T', '法定代表人': '柴琇', '注册资本': '51379.1647', '成立日期': '1988-11-29', '企业地址': '上海市奉贤区工业路899号8幢', '联系电话': '021-50185677', '联系邮箱': 'pr@milkground.cn', '注册号': '310000000165830', '组织机构代码': '16410234-5', '参保人数': '370', '行业一级': '科学研究和技术服务业', '行业二级': '科技推广和应用服务业', '行业三级': '其他科技推广服务业', '曾用名': '上海广泽食品科技股份有限公司,\n山东大成农药股份有限公司,\n山东农药工业股份有限公司', '企业简介': '上海妙可蓝多食品科技股份有限公司（简称广泽股份，曾用名：上海广泽食品科技股份有限公司）始创于1998年，总部设在有“东方美谷”之称的上海市奉贤区，系上海证券交易所主板上市公司（证券代码600882）。广泽股份主要生产奶酪和液态奶两大系列产品，拥有“妙可蓝多”“广泽”“澳醇牧场”等国内知名品牌。公司分别在上海、天津、长春和吉林建有4间奶酪和液态奶加工厂，是国内领先的奶酪生产企业。秉承“成为满足国人需求的奶酪专家”的品牌理念，广泽股份一直致力于整合全球资源，为国人提供最好的奶酪产品。公司聘请了一批资深专家加盟，在上海、天津设立了研发中心，并与来自欧洲、澳洲的奶酪公司展开合作，引进了国际先进的生产设备和技术。为从根本上保证产品品质，公司在吉林省建有万头奶牛生态牧场，奶牛全部为进口自澳洲的荷斯坦奶牛，奶质已达欧盟标准。目前，公司可为餐饮和工业客户提供黄油、稀奶油、炼乳、车达和马苏里拉奶酪、奶油芝士、芝士片、芝士酱等产品系列，可直接为消费者提供棒棒奶酪、成长奶酪、三角奶酪、小粒奶酪、新鲜奶酪、慕斯奶酪和辫子奶酪、雪球奶酪等特色产品系列。多年来，广泽股份一直坚持“广纳百川，泽惠四海”的经营理念，恪守“以客户为中心，以奋斗者为本，诚信感恩，务实进取”的核心价值观，努力提高研发和生产技术，不断开发满足消费者需求的奶酪产品，成为深受消费者喜爱的乳品行业知名品牌。', '经营范围': '许可项目：食品经营；食品互联网销售；互联网直播服务（不含新闻信息服务、网络表演、网络视听节目）；互联网信息服务；进出口代理。（依法须经批准的项目，经相关部门批准后方可开展经营活动，具体经营项目以相关部门批准文件或许可证件为准）一般项目：乳制品生产技术领域内的技术开发、技术咨询、技术服务、技术转让；互联网销售（除销售需要许可的商品）；互联网数据服务；信息系统集成服务；软件开发；玩具销售。（除依法须经批准的项目外，凭营业执照依法自主开展经营活动）'}
    # # 全部属性：['公司名称', '登记状态', '统一社会信用代码', '法定代表人', '注册资本', '成立日期', '企业地址', '联系电话', '联系邮箱', '注册号', '组织机构代码', '参保人数', '行业一级', '行业二级', '行业三级', '曾用名', '企业简介', '经营范围']
    # print("get_company_register_name:")
    # print(get_company_register_name({"统一社会信用代码": "913305007490121183"}))
    # print(find_all_attribute(get_company_register_name({"统一社会信用代码": "913305007490121183"})))
    # # 输出：{'公司名称': '天能电池集团股份有限公司'}
    # # 全部属性：['公司名称']
    # print("get_sub_company_info:")
    # print(get_sub_company_info({"公司名称": "上海爱斯达克汽车空调系统有限公司"}, []))
    # print(find_all_attribute(get_sub_company_info({"公司名称": "上海爱斯达克汽车空调系统有限公司"}, [])))
    # # 输出：{'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '87.5', '上市公司投资金额': '8.54亿', '公司名称': '上海爱斯达克汽车空调系统有限公司'}
    # # 全部属性：['关联上市公司全称', '上市公司关系', '上市公司参股比例', '上市公司投资金额', '公司名称']
    # print("get_sub_company_info_list:")
    # print(get_sub_company_info_list({"关联上市公司全称": "上海航天汽车机电股份有限公司"}, []))
    # print(find_all_attribute(get_sub_company_info_list({"关联上市公司全称": "上海航天汽车机电股份有限公司"}, [])))
    # # 输出：[{'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '8800.00万', '公司名称': '甘肃神舟光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '1.19亿', '公司名称': '甘肃张掖神舟光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '3400.00万', '公司名称': '嘉峪关恒能光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '5600.00万', '公司名称': '金昌太科光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '8700.00万', '公司名称': '喀什太科光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '65.0', '上市公司投资金额': '1296.99万', '公司名称': '科尔沁左翼后旗太科光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '100.00万', '公司名称': '兰坪太科光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '', '公司名称': '兰州恒能光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '81.76', '上市公司投资金额': '2.50亿', '公司名称': '连云港神舟新能源有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '7000.00万', '公司名称': '内蒙古上航新能源有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '95.0', '上市公司投资金额': '1.26亿', '公司名称': '内蒙古神舟光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '100.00万', '公司名称': '丘北太科光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '87.5', '上市公司投资金额': '8.54亿', '公司名称': '上海爱斯达克汽车空调系统有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '3.41亿', '公司名称': '上海能航机电发展有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '51.0', '上市公司投资金额': '2040.00万', '公司名称': '上饶市太科光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '1600.00万', '公司名称': '威海浩阳光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '59.4', '上市公司投资金额': '2620.00万', '公司名称': '文山太科光伏电力有限公司'}, {'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': '100.0', '上市公司投资金额': '1.45亿', '公司名称': '阳泉太科光伏电力有限公司'}]
    # # 全部属性：['关联上市公司全称', '上市公司关系', '上市公司参股比例', '上市公司投资金额', '公司名称']
    # print("get_legal_document:")
    # print(get_legal_document({"案号": "(2019)沪0115民初61975号"}, []))
    # print(find_all_attribute(get_legal_document({"案号": "(2019)沪0115民初61975号"}, [])))
    # # 输出：{'关联公司': '上海爱斯达克汽车空调系统有限公司', '标题': '上海爱斯达克汽车空调系统有限公司与上海逸测检测技术服务有限公司服务合同纠纷一审民事判决书', '案号': '(2019)沪0115民初61975号', '文书类型': '民事判决书', '原告': '上海爱斯达克汽车空调系统有限公司', '被告': '上海逸测检测技术服务有限公司', '原告律师事务所': '', '被告律师事务所': '上海世韬律师事务所', '案由': '服务合同纠纷', '涉案金额': '1254802.58', '判决结果': '一、被告上海逸测检测技术服务有限公司应于本判决生效之日起十日内支付原告上海爱斯达克汽车空调系统有限公司测试费1,254,802.58元; \\n \\n二、被告上海逸测检测技术服务有限公司应于本判决生效之日起十日内支付原告上海爱斯达克汽车空调系统有限公司违约金71,399.68元 。  \\n \\n负有金钱给付义务的当事人如未按本判决指定的期间履行给付金钱义务,应当依照《中华人民共和国民事诉讼法》第二百五十三条之规定,加倍支付迟延履行期间的债务利息 。  \\n \\n案件受理费16,736元,减半收取计8,368元,由被告上海逸测检测技术服务有限公司负担 。  \\n \\n如不服本判决,可在判决书送达之日起十五日内向本院递交上诉状,并按对方当事人的人数提出副本,上诉于上海市第一中级人民法院 。 ', '日期': '2019-12-09 00:00:00', '文件名': '（2019）沪0115民初61975号.txt'}
    # # 全部属性：['关联公司', '标题', '案号', '文书类型', '原告', '被告', '原告律师事务所', '被告律师事务所', '案由', '涉案金额', '判决结果', '日期', '文件名']
    # print("get_legal_document_list:")
    # print(get_legal_document_list({"关联公司": "上海爱斯达克汽车空调系统有限公司"}, []))
    # print(find_all_attribute(get_legal_document_list({"关联公司": "上海爱斯达克汽车空调系统有限公司"}, [])))
    # 输出：[{'关联公司': '上海爱斯达克汽车空调系统有限公司', '标题': '上海爱斯达克汽车空调系统有限公司与上海逸测检测技术服务有限公司服务合同纠纷一审民事判决书', '案号': '(2019)沪0115民初61975号', '文书类型': '民事判决书', '原告': '上海爱斯达克汽车空调系统有限公司', '被告': '上海逸测检测技术服务有限公司', '原告律师事务所': '', '被告律师事务所': '上海世韬律师事务所', '案由': '服务合同纠纷', '涉案金额': '1254802.58', '判决结果': '一、被告上海逸测检测技术服务有限公司应于本判决生效之日起十日内支付原告上海爱斯达克汽车空调系统有限公司测试费1,254,802.58元; \\n \\n二、被告上海逸测检测技术服务有限公司应于本判决生效之日起十日内支付原告上海爱斯达克汽车空调系统有限公司违约金71,399.68元 。  \\n \\n负有金钱给付义务的当事人如未按本判决指定的期间履行给付金钱义务,应当依照《中华人民共和国民事诉讼法》第二百五十三条之规定,加倍支付迟延履行期间的债务利息 。  \\n \\n案件受理费16,736元,减半收取计8,368元,由被告上海逸测检测技术服务有限公司负担 。  \\n \\n如不服本判决,可在判决书送达之日起十五日内向本院递交上诉状,并按对方当事人的人数提出副本,上诉于上海市第一中级人民法院 。 ', '日期': '2019-12-09 00:00:00', '文件名': '（2019）沪0115民初61975号.txt'}, {'关联公司': '上海爱斯达克汽车空调系统有限公司', '标题': '吴某某与上海爱斯达克汽车空调系统有限公司追索劳动报酬纠纷一审民事判决书', '案号': '(2019)沪0115民初91149号', '文书类型': '民事判决书', '原告': '吴某某', '被告': '上海爱斯达克汽车空调系统有限公司', '原告律师事务所': '上海国策律师事务所', '被告律师事务所': '上海市罗顿律师事务所', '案由': '追索劳动报酬纠纷', '涉案金额': '0', '判决结果': '一、被告上海爱斯达克汽车空调系统有限公司于本判决生效之日起十日内支付原告吴某某2019年4月1日至2019年5月31日期间延时加班工资差额9,094.50元; \\n \\n二、驳回原告吴某某的其余诉讼请求 。  \\n \\n负有金钱给付义务的当事人,如果未按本判决指定的期间履行给付金钱义务,应当依照《中华人民共和国民事诉讼法》第二百五十三条之规定,加倍支付迟延履行期间的债务利息 。  \\n \\n案件受理费10元,减半计5元,免予收取 。  \\n \\n如不服本判决,可在判决书送达之日起十五日内,向本院递交上诉状,并按对方当事人的人数提出副本,上诉于上海市第一中级人民法院 。 ', '日期': '2020-01-20 00:00:00', '文件名': '（2019）沪0115民初91149号.txt'}, {'关联公司': '上海爱斯达克汽车空调系统有限公司', '标题': '上海贝众汽车零部件有限公司与上海爱斯达克汽车空调系统有限公司技术委托开发合同纠纷民事一审案件民事判决书', '案号': '(2020)沪0115民初3857号', '文书类型': '民事判决书', '原告': '上海贝众汽车零部件有限公司', '被告': '上海爱斯达克汽车空调系统有限公司', '原告律师事务所': '上海远同律师事务所', '被告律师事务所': '上海步界律师事务所', '案由': '技术委托开发合同纠纷', '涉案金额': '21849', '判决结果': '一、被告上海爱斯达克汽车空调系统有限公司于本判决生效之日起十日内支付原告上海贝众汽车零部件有限公司差旅费21,849元; \\n \\n二、驳回原告上海贝众汽车零部件有限公司的其余诉讼请求 。  \\n \\n如果未按本判决指定的期间履行给付义务,应当依照《中华人民共和国民事诉讼法》第二百五十三条的规定,加倍支付迟延履行期间的债务利息 。  \\n \\n案件受理费14,225元,由原告上海贝众汽车零部件有限公司负担9,225元,被告上海爱斯达克汽车空调系统有限公司负担5,000元 。  \\n \\n如不服本判决,可在判决书送达之日起十五日内,向本院递交上诉状,并按照对方当事人或者代表人的人数提出副本,上诉于上海知识产权法院 。 ', '日期': '2021-04-28 00:00:00', '文件名': '（2020）沪0115民初3857号.txt'}]
    # 全部属性：['关联公司', '标题', '案号', '文书类型', '原告', '被告', '原告律师事务所', '被告律师事务所', '案由', '涉案金额', '判决结果', '日期', '文件名']
    # print("get_court_document:")
    # print(get_court_info({"法院名称": "上海市浦东新区人民法院"}, []))
    # print(find_all_attribute(get_court_info({"法院名称": "上海市浦东新区人民法院"}, [])))
    # # 输出：{'法院名称': '上海市浦东新区人民法院', '法院负责人': '朱丹', '成立日期': '2019-05-16', '法院地址': '上海市浦东新区丁香路611号', '法院联系电话': '-', '法院官网': '-'}
    # # 全部属性：['法院名称', '法院负责人', '成立日期', '法院地址', '法院联系电话', '法院官网']
    # print("get_court_code:")
    # print(get_court_code({'法院代字': '沪0115'}, []))
    # print(find_all_attribute(get_court_code({'法院代字': '沪0115'}, [])))
    # # 输出：{'法院名称': '上海市浦东新区人民法院', '行政级别': '市级', '法院级别': '基层法院', '法院代字': '沪0115', '区划代码': '310115', '级别': '1'}
    # # 全部属性：['法院名称', '行政级别', '法院级别', '法院代字', '区划代码', '级别']
    # print("get_lawfirm_info:")
    # print(get_lawfirm_info({"律师事务所名称": "爱德律师事务所"}, ['律所登记机关', '律师事务所唯一编码']))
    # print(find_all_attribute(get_lawfirm_info({"律师事务所名称": "爱德律师事务所"}, ['律所登记机关', '律师事务所唯一编码'])))
    # # 输出：{'律师事务所名称': '爱德律师事务所', '律师事务所唯一编码': '31150000E370803331', '律师事务所负责人': '巴布', '事务所注册资本': '10万元人民币', '事务所成立日期': '1995-03-14', '律师事务所地址': '呼和浩特市赛罕区大学西街110号丰业大厦11楼', '通讯电话': '0471-3396155', '通讯邮箱': 'kehufuwubu@ardlaw.cn', '律所登记机关': '内蒙古自治区呼和浩特市司法局'}{'律师事务所名称': '爱德律师事务所', '律师事务所唯一编码': '31150000E370803331', '律师事务所负责人': '巴布', '事务所注册资本': '10万元人民币', '事务所成立日期': '1995-03-14', '律师事务所地址': '呼和浩特市赛罕区大学西街110号丰业大厦11楼', '通讯电话': '0471-3396155', '通讯邮箱': 'kehufuwubu@ardlaw.cn', '律所登记机关': '内蒙古自治区呼和浩特市司法局'}
    # # 全部属性：['律所登记机关', '律师事务所唯一编码']
    # print("get_lawfirm_log:")
    # print(get_lawfirm_log({"律师事务所名称": "北京市金杜律师事务所"}, []))
    # print(find_all_attribute(get_lawfirm_log({"律师事务所名称": "北京市金杜律师事务所"}, [])))
    # # 输出：{'律师事务所名称': '北京市金杜律师事务所', '业务量排名': '2', '服务已上市公司': '68', '报告期间所服务上市公司违规事件': '23', '报告期所服务上市公司接受立案调查': '3'}
    # # 全部属性：['律师事务所名称', '业务量排名', '服务已上市公司', '报告期间所服务上市公司违规事件', '报告期所服务上市公司接受立案调查']
    # print("get_address_info:")
    # print(get_address_info({"地址": "西藏自治区那曲地区安多县帕那镇中路13号"}, []))
    # print(find_all_attribute(get_address_info({"地址": "西藏自治区那曲地区安多县帕那镇中路13号"}, [])))
    # # 输出：{'地址': '西藏自治区那曲地区安多县帕那镇中路13号', '省份': '西藏自治区', '城市': '那曲市', '区县': '安多县'}
    # # 全部属性：['地址', '省份', '城市', '区县']
    # print("get_citizens_sue_citizens:")
    # print(get_citizens_sue_citizens({ '原告': '张三', '原告性别': '男', '原告生日': '1976-10-2', '原告民族': '汉', '原告工作单位': 'XXX', '原告地址': '中国', '原告联系方式': '123456', '原告委托诉讼代理人': '李四', '原告委托诉讼代理人联系方式': '421313', '被告': '王五', '被告性别': '女', '被告生日': '1975-02-12', '被告民族': '汉', '被告工作单位': 'YYY', '被告地址': '江苏', '被告联系方式': '56354321', '被告委托诉讼代理人': '赵六', '被告委托诉讼代理人联系方式': '09765213', '诉讼请求': 'AA纠纷', '事实和理由': '上诉', '证据': 'PPPPP', '法院名称': '最高法', '起诉日期': '2012-09-08' }))
    # print(find_all_attribute({ '原告': '张三', '原告性别': '男', '原告生日': '1976-10-2', '原告民族': '汉', '原告工作单位': 'XXX', '原告地址': '中国', '原告联系方式': '123456', '原告委托诉讼代理人': '李四', '原告委托诉讼代理人联系方式': '421313', '被告': '王五', '被告性别': '女', '被告生日': '1975-02-12', '被告民族': '汉', '被告工作单位': 'YYY', '被告地址': '江苏', '被告联系方式': '56354321', '被告委托诉讼代理人': '赵六', '被告委托诉讼代理人联系方式': '09765213', '诉讼请求': 'AA纠纷', '事实和理由': '上诉', '证据': 'PPPPP', '法院名称': '最高法', '起诉日期': '2012-09-08' }))
    # # 输出："民事起诉状（公民起诉公民）\n原告：张三，性别：男，出生日期：1976-10-2，民族：汉，工作单位：XXX，地址：中国，联系方式：123456。\n原告委托诉讼代理人：李四，联系方式：421313。\n被告：王五，性别：女，出生日期：1975-02-12，民族：汉，工作单位：YYY，地址：江苏，联系方式：56354321。\n被告委托诉讼代理人：赵六，联系方式：09765213。\n诉讼请求：\nAA纠纷\n事实和理由：\n上诉\n证据和证据来源，证人姓名和住所：\nPPPPP\n此致\n最高法\n\n附:本起诉状副本x份\n\n起诉人(签名)\n2012-09-08"
    # # 全部属性：['原告', '原告性别', '原告生日', '原告民族', '原告工作单位', '原告地址', '原告联系方式', '原告委托诉讼代理人', '原告委托诉讼代理人联系方式', '被告', '被告性别', '被告生日', '被告民族', '被告工作单位', '被告地址', '被告联系方式', '被告委托诉讼代理人', '被告委托诉讼代理人联系方式', '诉讼请求', '事实和理由', '证据', '法院名称', '起诉日期']
    # print("get_company_sue_citizens:")
    # print(get_company_sue_citizens({ '原告': '上海公司', '原告地址': '上海', '原告法定代表人': '张三', '原告联系方式': '872638', '原告委托诉讼代理人': 'B律师事务所', '原告委托诉讼代理人联系方式': '5678900', '被告': '王五', '被告性别': '女', '被告生日': '1975-02-12', '被告民族': '汉', '被告工作单位': 'YYY', '被告地址': '江苏', '被告联系方式': '56354321', '被告委托诉讼代理人': '赵六', '被告委托诉讼代理人联系方式': '09765213', '诉讼请求': 'AA纠纷', '事实和理由': '上诉', '证据': 'PPPPP', '法院名称': '最高法', '起诉日期': '2012-09-08' }))
    # print(find_all_attribute({ '原告': '上海公司', '原告地址': '上海', '原告法定代表人': '张三', '原告联系方式': '872638', '原告委托诉讼代理人': 'B律师事务所', '原告委托诉讼代理人联系方式': '5678900', '被告': '王五', '被告性别': '女', '被告生日': '1975-02-12', '被告民族': '汉', '被告工作单位': 'YYY', '被告地址': '江苏', '被告联系方式': '56354321', '被告委托诉讼代理人': '赵六', '被告委托诉讼代理人联系方式': '09765213', '诉讼请求': 'AA纠纷', '事实和理由': '上诉', '证据': 'PPPPP', '法院名称': '最高法', '起诉日期': '2012-09-08' }))
    # # 输出："民事起诉状（公司起诉公民）\n原告：上海公司，地址：上海。法定代表人（负责人）：张三，联系方式：872638。\n原告委托诉讼代理人：B律师事务所，联系方式：5678900。\n被告：王五，性别：女，出生日期：1975-02-12，民族：汉，工作单位：YYY，地址：江苏，联系方式：56354321。\n被告委托诉讼代理人：赵六，联系方式：09765213。\n诉讼请求：\nAA纠纷\n事实和理由：\n上诉\n证据和证据来源，证人姓名和住所：\nPPPPP\n此致\n最高法\n\n附:本起诉状副本x份\n\n起诉人(签名)\n2012-09-08"
    # # 全部属性：['原告', '原告地址', '原告法定代表人', '原告联系方式', '原告委托诉讼代理人', '原告委托诉讼代理人联系方式', '被告', '被告性别', '被告生日', '被告民族', '被告工作单位', '被告地址', '被告联系方式', '被告委托诉讼代理人', '被告委托诉讼代理人联系方式', '诉讼请求', '事实和理由', '证据', '法院名称', '起诉日期']
    # print("get_citizens_sue_company:")
    # print(get_citizens_sue_company({ '原告': '张三', '原告性别': '男', '原告生日': '1976-10-2', '原告民族': '汉', '原告工作单位': 'XXX', '原告地址': '中国', '原告联系方式': '123456', '原告委托诉讼代理人': '李四', '原告委托诉讼代理人联系方式': '421313', '被告': '王五公司', '被告地址': '公司地址', '被告法定代表人': '赵四', '被告联系方式': '98766543', '被告委托诉讼代理人': 'C律师事务所', '被告委托诉讼代理人联系方式': '425673398', '诉讼请求': 'AA纠纷', '事实和理由': '上诉', '证据': 'PPPPP', '法院名称': '最高法', '起诉日期': '2012-09-08' }))
    # print(find_all_attribute({ '原告': '张三', '原告性别': '男', '原告生日': '1976-10-2', '原告民族': '汉', '原告工作单位': 'XXX', '原告地址': '中国', '原告联系方式': '123456', '原告委托诉讼代理人': '李四', '原告委托诉讼代理人联系方式': '421313', '被告': '王五公司', '被告地址': '公司地址', '被告法定代表人': '赵四', '被告联系方式': '98766543', '被告委托诉讼代理人': 'C律师事务所', '被告委托诉讼代理人联系方式': '425673398', '诉讼请求': 'AA纠纷', '事实和理由': '上诉', '证据': 'PPPPP', '法院名称': '最高法', '起诉日期': '2012-09-08' }))
    # # 输出："民事起诉状（公民起诉公司）\n原告：张三，性别：男，出生日期：1976-10-2，民族：汉，工作单位：XXX，地址：中国，联系方式：123456。\n原告委托诉讼代理人：李四，联系方式：421313。\n被告：王五公司，地址：公司地址。法定代表人（负责人）：赵四，联系方式：98766543。\n被告委托诉讼代理人：C律师事务所，联系方式：425673398。\n诉讼请求：\nAA纠纷\n事实和理由：\n上诉\n证据和证据来源，证人姓名和住所：\nPPPPP\n此致\n最高法\n\n附:本起诉状副本x份\n\n起诉人(签名)\n2012-09-08"
    # # 全部属性：['原告', '原告性别', '原告生日', '原告民族', '原告工作单位', '原告地址', '原告联系方式', '原告委托诉讼代理人', '原告委托诉讼代理人联系方式', '被告', '被告地址', '被告法定代表人', '被告联系方式', '被告委托诉讼代理人', '被告委托诉讼代理人联系方式', '诉讼请求', '事实和理由', '证据', '法院名称', '起诉日期']
    # print("get_company_sue_company:")
    # print(get_company_sue_company({ '原告': '上海公司', '原告地址': '上海', '原告法定代表人': '张三', '原告联系方式': '872638', '原告委托诉讼代理人': 'B律师事务所', '原告委托诉讼代理人联系方式': '5678900', '被告': '王五公司', '被告地址': '公司地址', '被告法定代表人': '赵四', '被告联系方式': '98766543', '被告委托诉讼代理人': 'C律师事务所', '被告委托诉讼代理人联系方式': '425673398', '诉讼请求': 'AA纠纷', '事实和理由': '上诉', '证据': 'PPPPP', '法院名称': '最高法', '起诉日期': '2012-09-08' }))
    # print(find_all_attribute({ '原告': '上海公司', '原告地址': '上海', '原告法定代表人': '张三', '原告联系方式': '872638', '原告委托诉讼代理人': 'B律师事务所', '原告委托诉讼代理人联系方式': '5678900', '被告': '王五公司', '被告地址': '公司地址', '被告法定代表人': '赵四', '被告联系方式': '98766543', '被告委托诉讼代理人': 'C律师事务所', '被告委托诉讼代理人联系方式': '425673398', '诉讼请求': 'AA纠纷', '事实和理由': '上诉', '证据': 'PPPPP', '法院名称': '最高法', '起诉日期': '2012-09-08' }))
    # # 输出："民事起诉状（公司起诉公司）\n原告：上海公司，地址：上海。法定代表人（负责人）：张三，联系方式：872638。\n原告委托诉讼代理人：B律师事务所，联系方式：5678900。\n被告：王五公司，地址：公司地址。法定代表人（负责人）：赵四，联系方式：98766543。\n被告委托诉讼代理人：C律师事务所，联系方式：425673398。\n诉讼请求：\nAA纠纷\n事实和理由：\n上诉\n证据和证据来源，证人姓名和住所：\nPPPPP\n此致\n最高法\n\n附:本起诉状副本x份\n\n起诉人(签名)\n2012-09-08"
    # # 全部属性：['原告', '原告地址', '原告法定代表人', '原告联系方式', '原告委托诉讼代理人', '原告委托诉讼代理人联系方式', '被告', '被告地址', '被告法定代表人', '被告联系方式', '被告委托诉讼代理人', '被告委托诉讼代理人联系方式', '诉讼请求', '事实和理由', '证据', '法院名称', '起诉日期']

    '''
    上面是0-11,20-23的样例
    下面是12-19的，还有一个筛选函数
    '''


    # print(get_address_code({"省份": "西藏自治区", "城市": "拉萨市", "区县": "城关区"}, []))
    # print(get_address_code({"省份": "河南省", "城市": "洛阳市", "区县": "洛龙区"}, []))
    # # {'省份': '西藏自治区', '城市': '拉萨市', '城市区划代码': '540100000000', '区县': '城关区', '区县区划代码': '540102000000'}
    #
    # print(get_temp_info({"省份": "北京市", "城市": "北京市", "日期": "2020年1月1日"}, []))
    # # {'日期': '2020年1月1日', '省份': '北京市', '城市': '北京市', '天气': '晴', '最高温度': '11', '最低温度': '1', '湿度': '55'}
    #
    # print(get_legal_abstract({"案号": "（2019）沪0115民初61975号"}, []))
    # '''
    # {'文件名': '（2019）沪0115民初61975号.txt',
    # '案号': '（2019）沪0115民初61975号',
    # '文本摘要': '原告上海爱斯达克汽车空调系统有限公司与被告上海逸测检测技术服务有限公司因服务合同纠纷一案，原告请求被告支付检测费1,254,802.58元、延迟履行违约金71,399.68元及诉讼费用。被告辩称，系争合同已终止，欠款金额应为499,908元，且不认可违约金。\n法院认为，原告与腾双公司签订的测试合同适用于原被告，原告提供的测试服务应得到被告支付。依照《中华人民共和国合同法》第六十条、第一百零九条,《中华人民共和国民事诉讼法》第六十四条第一款,《最高人民法院关于适用〈中华人民共和国民事诉讼法〉的解释》第九十条之规定判决被告支付原告检测费1,254,802.58元及违约金71,399.68元。'}
    # '''
    #
    # print(get_xzgxf_info({"案号": "（2018）鲁0403执1281号"}, []))
    # '''
    # {'限制高消费企业名称': '枣庄西能新远大天然气利用有限公司',
    # '案号': '（2018）鲁0403执1281号',
    # '法定代表人': '高士其',
    # '申请人': '枣庄市人力资源和社会保障局',
    # '涉案金额': '12000',
    # '执行法院': '山东省枣庄市薛城区人民法院',
    # '立案日期': '2018-11-16 00:00:00',
    # '限高发布日期': '2019-02-13 00:00:00'}
    # '''
    #
    # print(get_xzgxf_info_list({"限制高消费企业名称": "欣水源生态环境科技有限公司"}, []))
    # '''
    # {'限制高消费企业名称': '欣水源生态环境科技有限公司',
    # '案号': '（2023）黔2731执恢130号',
    # '法定代表人': '刘福云',
    # '申请人': '四川省裕锦建设工程有限公司惠水分公司',
    # '涉案金额': '7500000',
    # '执行法院': '贵州省黔南布依族苗族自治州惠水县人民法院',
    # '立案日期': '2023-08-04 00:00:00',
    # '限高发布日期': '2023-11-09 00:00:00'}
    # '''
    #
    # print(get_xzgxf_info_list({"限制高消费企业名称": '枣庄西能新远大天然气利用有限公司'}, []))
    # '''
    # [{'限制高消费企业名称': '枣庄西能新远大天然气利用有限公司', '案号': '（2019）苏0582执2600号', '法定代表人': '高士其', '申请人': '张家港富瑞特种装备股份有限公司', '涉案金额': '2145921.24', '执行法院': '江苏省苏州市张家港市人民法院', '立案日期': '2019-04-02 00:00:00', '限高发布日期': '2019-09-25 00:00:00'},
    # {'限制高消费企业名称': '枣庄西能新远大天然气利用有限公司', '案号': '（2018）鲁0403执1281号', '法定代表人': '高士其', '申请人': '枣庄市人力资源和社会保障局', '涉案金额': '12000', '执行法院': '山东省枣庄市薛城区人民法院', '立案日期': '2018-11-16 00:00:00', '限高发布日期': '2019-02-13 00:00:00'}]
    # '''
    #
    # print(get_sum([1, 2, 3, 4, 5]))
    # print(get_sum(["1", "2", "3", "4", "5"]))
    # print(get_sum(["1万", "1亿", "2千"]))
    # '''
    # 15
    # 15
    # 100012000.0
    # '''
    #
    # print(rank({"keys": ["a", "b", "c"], "values": [2, 1, 3]}))
    # # ['b', 'a', 'c']
    #
    # save_dict_list_to_word('北京碧水源科技股份有限公司',"{'工商信息': [{'公司名称': '北京碧水源科技股份有限公司', '登记状态': '存续', '统一社会信用代码': '91110000802115985Y', '参保人数': '351', '行业一级': '科学研究和技术服务业', '行业二级': '科技推广和应用服务业', '行业三级': '其他科技推广服务业'}], '子公司信息': [{'关联上市公司全称': '北京碧水源科技股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': 100.0, '上市公司投资金额': '1.06亿', '公司名称': '北京碧海环境科技有限公司'}], '裁判文书': [{'关联公司': '北京碧水源科技股份有限公司', '原告': '四川帝宇水利水电工程有限公司', '被告': '成都碧水源江环保科技有限公司,北京碧水源科技股份有限公司', '案由': '建设工程施工合同纠纷', '涉案金额': 0.0, '日期': Timestamp('2019-07-23 00:00:00')}], '限制高消费': [{'限制高消费企业名称': '南京仙林碧水源污水处理有限公司', '案号': '（2024）苏0113执1601号', '申请人': '苏华建设集团有限公司', '涉案金额': '-', '立案日期': Timestamp('2024-04-07 00:00:00'), '限高发布日期': Timestamp('2024-06-24 00:00:00')}]}")
    # # "Word_北京碧水源科技股份有限公司_companyregister1_7_subcompanyinfo1_5_legallist1_6_xzgxflist1_6"

    # info_list = get_legal_document_list({"关联公司": "上海爱斯达克汽车空调系统有限公司"}, [])
    # # input_list = [{"属性名称1": {"判别类别": '大于小于等于或其他', '判断条件':[]}}, {"属性名称2": {"判别类别": '大于小于等于或其他', '判断条件':[]}}...]
    # # input_info = [{"属性名称1": "", "属性名称2": "",...,},{"属性名称1": "", "属性名称2": "",...,},...,] 待筛选的数据
    # input_list = [{"起诉日期": {"判别类别": "等于", "判断条件": ["2019"]}}, {"涉案金额": {"判别类别": "大于", "判断条件": [10000]}}]
    # print("过滤结果")
    # print(filter_(input_list, info_list))
