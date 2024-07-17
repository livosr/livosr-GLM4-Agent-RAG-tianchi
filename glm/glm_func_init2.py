from zhipuai import ZhipuAI
import requests
import json

api_key = "8f5594ef782d24752c0e875d8da33592.ElGxsEuPuzU9ra6C"
client = ZhipuAI(api_key=api_key) # 请填写您自己的APIKey

# 根据子问题和info，返回筛选出来的函数入参和需要调用的服务函数名称
# 返回值可能不是str了，但是我没改，好像无所谓


def get_address_code(query: str, info: str) -> str:
    # 12
    tools = [
        # get_address_code
        {
            "type": "function",
            "function": {
                "name": "get_address_code",
                "description": '''
            描述:根据省市区查询区划代码，会返回两个码：城市区划代码，区县区划代码
            入参:query_conds (dict[str, str]): 字典，包含省份，城市，区县信息
                need_fields (list[str]): 需要查找的属性列表，在本函数中默认为空
            返回:dict[str, str]: 包含省市区信息，城市区划代码，区县区划代码
                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_conds": {
                            "type": "dict[str, str]",
                            "description": "省市区信息，eg{省份:西藏自治区,城市:拉萨市,区县:城关区}->dict",
                        },
                        "need_fields": {
                            "type": "list[str]",
                            "description": "需要查找的属性列表，在本函数中默认为空",
                        }

                    },
                    "required": ["query_conds", "need_fields"],
                },
            }
        },
    ]

    messages = [
        {
            "role": "system",
            "content": '''
                    你是一个优秀的问题分类与信息提取机器人，我需要你根据输入的query以及info(info可能有也可能没有),给出函数输入参数,你的返回值需要包含需要使用的函数的全称:\n
        '''
        },
        {
            "role": "user",
            "content": " query:{}\ninfo{}\n".format(query, info)
        }
    ]

    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    func_name = response.choices[0].message.tool_calls[0].function.name
    response_arguments = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
    print(response_arguments)
    return response_arguments, func_name


def get_temp_info(query: str, info: str) -> str:
    # 13
    tools = [
        # get_temp_info
        {
            "type": "function",
            "function": {
                "name": "get_temp_info",
                "description": '''
            根据日期及省份城市查询天气相关信息
            入参:query_conds (dict[str, str]): 字典，包含省份，城市，日期信息
                need_fields (list[str]): 需要查找的属性列表，在本函数中默认为空
            返回:dict[str, str]: 天气信息字典，包含日期，省份，城市，天气，最高温度，最低温度，湿度
                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_conds": {
                            "type": "dict[str, str]",
                            "description": "要查询天气的省份，城市，日期字典，eg{省份: 北京市, 城市: 北京市, 日期: 2020年1月1日}->dict",
                        },
                        "need_fields": {
                            "type": "list[str]",
                            "description": "需要查找的属性列表，在本函数中默认为空",
                        }

                    },
                    "required": ["query_conds", "need_fields"],
                },
            }
        },
    ]

    messages = [
        {
            "role": "system",
            "content": '''
                    你是一个优秀的问题分类与信息提取机器人，我需要你根据输入的query以及info(info可能有也可能没有),给出函数输入参数,你的返回值需要包含需要使用的函数的全称:\n
        '''
        },
        {
            "role": "user",
            "content": " query:{}\ninfo{}\n".format(query, info)
        }
    ]

    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    func_name = response.choices[0].message.tool_calls[0].function.name
    response_arguments = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
    print(response_arguments)
    return response_arguments, func_name


def get_legal_abstract(query: str, info: str) -> str:
    # 14
    tools = [
        # get_legal_abstract
        {
            "type": "function",
            "function": {
                "name": "get_legal_abstract",
                "description": '''
            根据案号查询文本摘要
            入参:query_conds (dict[str, str]): 案号字典
                need_fields (list[str]): 需要查找的属性列表，在本函数中默认为空
            返回:dict[str, str]: 摘要信息字典，包含文件名，文本摘要，案号
                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_conds": {
                            "type": "dict[str, str]",
                            "description": "案号字典，eg{案号:（2019）沪0115民初61975号}->dict",
                        },
                        "need_fields": {
                            "type": "list[str]",
                            "description": "需要查找的属性列表，在本函数中默认为空",
                        }

                    },
                    "required": ["query_conds", "need_fields"],
                },
            }
        },
    ]

    messages = [
        {
            "role": "system",
            "content": '''
                    你是一个优秀的问题分类与信息提取机器人，我需要你根据输入的query以及info(info可能有也可能没有),给出函数输入参数,你的返回值需要包含需要使用的函数的全称:\n
        '''
        },
        {
            "role": "user",
            "content": " query:{}\ninfo{}\n".format(query, info)
        }
    ]

    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    func_name = response.choices[0].message.tool_calls[0].function.name
    response_arguments = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
    print(response_arguments)
    return response_arguments, func_name


def get_xzgxf_info(query: str, info: str) -> str:
    # 15
    tools = [
        # get_xzgxf_info
        {
            "type": "function",
            "function": {
                "name": "get_xzgxf_info",
                "description": '''
            根据案号查询限制高消费相关信息
            入参:query_conds (dict[str, str]): 案号字典
                need_fields (list[str]): 需要查找的属性列表，在本函数中默认为空
            返回:dict[str, str]: 限制高消费相关信息字典，包含限制高消费企业名称，案号，法定代表人，申请人，涉案金额，执行法院，立案日期，限高发布日期
                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_conds": {
                            "type": "dict[str, str]",
                            "description": "案号字典，eg{案号:（2018）鲁0403执1281号}->dict",
                        },
                        "need_fields": {
                            "type": "list[str]",
                            "description": "需要查找的属性列表，在本函数中默认为空",
                        }

                    },
                    "required": ["query_conds", "need_fields"],
                },
            }
        },
    ]

    messages = [
        {
            "role": "system",
            "content": '''
                    你是一个优秀的问题分类与信息提取机器人，我需要你根据输入的query以及info(info可能有也可能没有),给出函数输入参数,你的返回值需要包含需要使用的函数的全称:\n
        '''
        },
        {
            "role": "user",
            "content": " query:{}\ninfo{}\n".format(query, info)
        }
    ]

    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    func_name = response.choices[0].message.tool_calls[0].function.name
    response_arguments = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
    print(response_arguments)
    return response_arguments, func_name


def get_xzgxf_info_list(query: str, info: str) -> str:
    # 16
    tools = [
        # get_xzgxf_info_list
        {
            "type": "function",
            "function": {
                "name": "get_xzgxf_info_list",
                "description": '''
            根据企业名称查询所有限制高消费相关信息列表
            入参:query_conds (dict[str, str]): 企业名称字典
                need_fields (list[str]): 需要查找的属性列表，在本函数中默认为空
            返回:list[dict]: 限制高消费相关信息列表，由字典组成，字典中包括限制高消费企业名称，案号，法定代表人，申请人，涉案金额，执行法院，立案日期，限高发布日期
                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_conds": {
                            "type": "dict[str, str]",
                            "description": "企业名称字典，eg{限制高消费企业名称:欣水源生态环境科技有限公司}->dict",
                        },
                        "need_fields": {
                            "type": "list[str]",
                            "description": "需要查找的属性列表，在本函数中默认为空",
                        }

                    },
                    "required": ["query_conds", "need_fields"],
                },
            }
        },
    ]

    messages = [
        {
            "role": "system",
            "content": '''
                    你是一个优秀的问题分类与信息提取机器人，我需要你根据输入的query以及info(info可能有也可能没有),给出函数输入参数,你的返回值需要包含需要使用的函数的全称:\n
        '''
        },
        {
            "role": "user",
            "content": " query:{}\ninfo{}\n".format(query, info)
        }
    ]

    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    func_name = response.choices[0].message.tool_calls[0].function.name
    response_arguments = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
    print(response_arguments)
    return response_arguments, func_name


def get_sum(query: str, info: str) -> str:
    # 17
    tools = [
        # get_sum
        {
            "type": "function",
            "function": {
                "name": "get_sum",
                "description": '''
            求和函数，可以对传入的int、float、str数组进行求和，str数组可以转换字符串里包含的单位信息，如"1万"，只支持“千”，“万”，亿”
            入参:nums: list[int] or list[float] or list[str]: 需要求和的列表，里面的元素有三种类型，int,float和str    
            返回:int or float: 求和结果
                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "nums": {
                            "type": "list[int] or list[float] or list[str]",
                            "description": "需要求和的列表，里面的元素有三种类型，int,float和str，eg[1万, 1亿, 2千]",
                        },
                    },
                    "required": ["nums"],
                },
            }
        },
    ]

    messages = [
        {
            "role": "system",
            "content": '''
                    你是一个优秀的问题分类与信息提取机器人，我需要你根据输入的query以及info(info可能有也可能没有),给出函数输入参数,你的返回值需要包含需要使用的函数的全称:\n
        '''
        },
        {
            "role": "user",
            "content": " query:{}\ninfo{}\n".format(query, info)
        }
    ]

    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    func_name = response.choices[0].message.tool_calls[0].function.name
    response_arguments = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
    print(response_arguments)
    return response_arguments, func_name


def rank(query: str, info: str) -> str:
    # 18
    tools = [
        # rank
        {
            "type": "function",
            "function": {
                "name": "rank",
                "description": '''
            排序函数，返回按照values排序的keys
            入参:dict[str, str]: 要排序的字典
                is_desc: bool: 是否降序排序，默认为False
            返回:list[any]: 排序后的keys的列表
                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dict": {
                            "type": "dict[str, str]",
                            "description": "要排序的字典，其中包括keys: list[any]和values: list[float], eg{keys: [a, b, c], values: [2, 1, 3]}",
                        },
                        "is_desc": {
                            "type": "bool",
                            "description": "是否降序排序，默认为False",
                        }
                    },
                    "required": ["dict", "is_desc"],
                },
            }
        },
    ]

    messages = [
        {
            "role": "system",
            "content": '''
                    你是一个优秀的问题分类与信息提取机器人，我需要你根据输入的query以及info(info可能有也可能没有),给出函数输入参数,你的返回值需要包含需要使用的函数的全称:\n
        '''
        },
        {
            "role": "user",
            "content": " query:{}\ninfo{}\n".format(query, info)
        }
    ]

    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    func_name = response.choices[0].message.tool_calls[0].function.name
    response_arguments = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
    print(response_arguments)
    return response_arguments, func_name


def save_dict_list_to_word(query: str, info: str) -> str:
    # 19
    tools = [
        # save_dict_list_to_word
        {
            "type": "function",
            "function": {
                "name": "save_dict_list_to_word",
                "description": '''
            通过传入结构化信息，制作生成公司数据报告（demo）
            入参:company_name: str : 公司名称
                dict_list: str: 一整个大字符串，包含数据信息的字典
            返回:无
                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "company_name": {
                            "type": "str",
                            "description": "公司名称, eg 北京碧水源科技股份有限公司",
                        },
                        "dict_list": {
                            "type": "str",
                            "description": "一整个大字符串，包含数据信息的字典",
                        }
                    },
                    "required": ["company_name", "dict_list"],
                },
            }
        },
    ]

    messages = [
        {
            "role": "system",
            "content": '''
                    你是一个优秀的问题分类与信息提取机器人，我需要你根据输入的query以及info(info可能有也可能没有),给出函数输入参数,你的返回值需要包含需要使用的函数的全称:\n
        '''
        },
        {
            "role": "user",
            "content": " query:{}\ninfo{}\n".format(query, info)
        }
    ]

    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    func_name = response.choices[0].message.tool_calls[0].function.name
    response_arguments = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
    print(response_arguments)
    return response_arguments, func_name


def filter_(query: str, info) -> str:
    # 筛选函数
    tools = [
        # filter_
        {
            "type": "function",
            "function": {
                "name": "filter_",
                "description": '''
            通过传入待筛选属性名称，判别类别和判断条件，进行多轮筛选，
            对于每种待筛选属性，根据指定的判别类别和判断条件，筛选出符合要求的input_info中的数据项
            例如，给定妙可蓝多公司的涉案信息列表，筛选出起诉日期在2020年，涉案金额大于100万小于1000万的案件
            那么这个例子中，待筛选属性1就是起诉日期，判别类别为等于，判断条件为2020，待筛选属性2是涉案金额，判别类别为区间，判断条件为['1000000','10000000']
            入参:input_list: list[dict] : 待筛选属性名称，判别类别和判断条件
                input_info: list[dict]: 待筛选的原数据
            返回:筛选出的数据项
                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "input_list": {
                            "type": "list[dict]",
                            "description": "由待筛选的属性组成的列表，每种属性分别存储一个字典内，字典的键为属性名，字典的值包含判别类别和判断条件, eg [{'起诉日期': {'判别类别': '等于', '判断条件': ['2019']}}, {'涉案金额': {'判别类别': '大于', '判断条件': ['10000']}}]"
                                           "判别类别一共有四种，'大于'，'小于'，'等于'和'区间'"
                                            "判断条件是一个列表，由从query中提取出的，可以作为筛选参考值的数据组成。注意，判断条件中应当只含有数字元素，不能包含'万'，'亿'，'千'等单位，你需要把类似单位转化为正确的数值"
                                            "例如，给定妙可蓝多公司的涉案信息列表，筛选出起诉日期在2020年，涉案金额大于100万小于1000万的案件"
                                            "那么这个例子中，待筛选属性1就是'起诉日期'，判别类别为'等于'，判断条件为['2020']，待筛选属性2是'涉案金额'，判别类别为'区间'，判断条件为['1000000','10000000']"
                                            "你需要从query中，智慧地找出待筛选属性，正确地选择判别类别，并提取出全部的判断条件，最终组成input_list应有的数据结构",
                        },
                    },
                    "required": ["input_list"],
                },
            }
        },
    ]

    messages = [
        {
            "role": "system",
            "content": '''
                    你是一个优秀的问题分类与信息提取机器人，我需要你根据输入的query以及info(info可能有也可能没有),给出函数输入参数,你的返回值需要包含需要使用的函数的全称:\n
        '''
        },
        {
            "role": "user",
            "content": " query:{}\ninfo{}\n".format(query, info)
        }
    ]

    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
    func_name = response.choices[0].message.tool_calls[0].function.name
    response_arguments = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
    i = 0
    while i < 15:
        if response_arguments is None:
            response = client.chat.completions.create(
                model="glm-4",  # 填写需要调用的模型名称
                messages=messages,
                tools=tools,
                tool_choice="auto"
            )
            func_name = response.choices[0].message.tool_calls[0].function.name
            response_arguments = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
            i += 1
            continue
        else:
            print(i)
            print(response_arguments)
            if isinstance(info, list):
                input_info_value = info
            elif isinstance(info, tuple):
                input_info_value = info[1]
            response_arguments['input_info'] = input_info_value
            return response_arguments, func_name

#
# def filter(query: str, info: str) -> str:
#     i = 0
#     while i < 10:
#         func_name = response.choices[0].message.tool_calls[0].function.name
#         response_arguments = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
#         if response[0] is None:
#             i += 1
#             continue
#         else:
#             print(i)
#             return response

#
# def filter_(query: str, info: str) -> str:
#     # 筛选函数
#     tools = [
#         # filter_
#         {
#             "type": "function",
#             "function": {
#                 "name": "filter_",
#                 "description": '''
#             通过传入待筛选属性名称，判别类别和判断条件，进行多轮筛选，
#             对于每种待筛选属性，根据指定的判别类别和判断条件，筛选出符合要求的input_info中的数据项
#             例如，给定妙可蓝多公司的涉案信息列表，筛选出起诉日期在2020年，涉案金额大于100万小于1000万的案件
#             那么这个例子中，待筛选属性1就是起诉日期，判别类别为等于，判断条件为2020，待筛选属性2是涉案金额，判别类别为区间，判断条件为['1000000','10000000']
#             入参:input_list: list[dict] : 待筛选属性名称，判别类别和判断条件
#                 input_info: list[dict]: 待筛选的原数据
#             返回:筛选出的数据项
#                         ''',
#                 "parameters": {
#                     "type": "object",
#                     "properties": {
#                         "input_list": {
#                             "type": "list[dict]",
#                             "description": '''由待筛选的属性组成的列表，每种属性分别存储一个字典内，字典的键为属性名，字典的值包含判别类别和判断条件, eg [{'起诉日期': {'判别类别': '等于', '判断条件': ['2019']}}, {'涉案金额': {'判别类别': '大于', '判断条件': ['10000']}}]
#                                            判别类别一共有四种，'大于'，'小于'，'等于'和'区间'
#                                            判断条件是一个列表，由从query中提取出的，可以作为筛选参考值的数据组成。注意，判断条件中应当只含有数字元素，不能包含'万'，'亿'，'千'等单位，你需要把类似单位转化为正确的数值
#                                            例如，给定妙可蓝多公司的涉案信息列表，筛选出起诉日期在2020年，涉案金额大于100万小于1000万的案件
#                                            那么这个例子中，待筛选属性1就是'起诉日期'，判别类别为'等于'，判断条件为['2020']，待筛选属性2是'涉案金额'，判别类别为'区间'，判断条件为['1000000','10000000']
#                                            你需要从query中，智慧地找出待筛选属性，正确地选择判别类别，并提取出全部的判断条件，最终组成input_list应有的数据结构''',
#                         },
#                         "input_info": {
#                             "type": "list[dict]",
#                             "description": "input_info就是info",
#                         }
#                     },
#                     "required": ["input_list", "input_info"],
#                 },
#             }
#         },
#     ]
#
#     messages = [
#         {
#             "role": "system",
#             "content": '''
#                     你是一个优秀的问题分类与信息提取机器人，我需要你根据输入的query以及info(info可能有也可能没有),给出函数输入参数,你的返回值需要包含需要使用的函数的全称:\n
#         '''
#         },
#         {
#             "role": "user",
#             "content": " query:{}\ninfo:{}\n".format(query, info)
#         }
#     ]
#
#     for i in range(15):
#         try:
#             response = client.chat.completions.create(
#                 model="glm-4",  # 填写需要调用的模型名称
#                 messages=messages,
#                 tools=tools,
#                 tool_choice="auto"
#             )
#
#             # 打印整个响应，帮助调试
#             print(f"Attempt {i+1} - Response: {response}")
#
#             # 检查响应结构并提取信息
#             if response and response.choices and response.choices[0].message.tool_calls:
#                 func_name = response.choices[0].message.tool_calls[0].function.name
#                 response_arguments = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
#                 if response_arguments:
#                     # 根据info的类型来决定input_info的值
#                     if isinstance(info, str):
#                         info_data = json.loads(info)
#                     elif isinstance(info, tuple):
#                         info_data = json.loads(info[1])
#                     else:
#                         info_data = info
#
#                     response_arguments['input_info'] = info_data
#                     print(f"Attempt {i + 1} - Response Arguments: {response_arguments}")
#                     return response_arguments, func_name
#             else:
#                 print(f"Attempt {i + 1} - Invalid response structure.")
#         except Exception as e:
#             print(f"Attempt {i + 1} - Error: {e}")
#
#     # 如果所有尝试都失败，返回 None
#     print("All attempts failed.")
#     return None, None


if __name__ == '__main__':
    info = (3, [{'关联公司': '上海爱斯达克汽车空调系统有限公司', '标题': '上海爱斯达克汽车空调系统有限公司与上海逸测检测技术服务有限公司服务合同纠纷一审民事判决书', '案号': '(2019)沪0115民初61975号', '文书类型': '民事判决书', '原告': '上海爱斯达克汽车空调系统有限公司', '被告': '上海逸测检测技术服务有限公司', '原告律师事务所': '', '被告律师事务所': '上海世韬律师事务所', '案由': '服务合同纠纷', '涉案金额': '1254802.58', '判决结果': '一、被告上海逸测检测技术服务有限公司应于本判决生效之日起十日内支付原告上海爱斯达克汽车空调系统有限公司测试费1,254,802.58元; \\n \\n二、被告上海逸测检测技术服务有限公司应于本判决生效之日起十日内支付原告上海爱斯达克汽车空调系统有限公司违约金71,399.68元 。  \\n \\n负有金钱给付义务的当事人如未按本判决指定的期间履行给付金钱义务,应当依照《中华人民共和国民事诉讼法》第二百五十三条之规定,加倍支付迟延履行期间的债务利息 。  \\n \\n案件受理费16,736元,减半收取计8,368元,由被告上海逸测检测技术服务有限公司负担 。  \\n \\n如不服本判决,可在判决书送达之日起十五日内向本院递交上诉状,并按对方当事人的人数提出副本,上诉于上海市第一中级人民法院 。 ', '日期': '2019-12-09 00:00:00', '文件名': '（2019）沪0115民初61975号.txt', '起诉日期': '2019'}, {'关联公司': '上海爱斯达克汽车空调系统有限公司', '标题': '吴某某与上海爱斯达克汽车空调系统有限公司追索劳动报酬纠纷一审民事判决书', '案号': '(2019)沪0115民初91149号', '文书类型': '民事判决书', '原告': '吴某某', '被告': '上海爱斯达克汽车空调系统有限公司', '原告律师事务所': '上海国策律师事务所', '被告律师事务所': '上海市罗顿律师事务所', '案由': '追索劳动报酬纠纷', '涉案金额': '0', '判决结果': '一、被告上海爱斯达克汽车空调系统有限公司于本判决生效之日起十日内支付原告吴某某2019年4月1日至2019年5月31日期间延时加班工资差额9,094.50元; \\n \\n二、驳回原告吴某某的其余诉讼请求 。  \\n \\n负有金钱给付义务的当事人,如果未按本判决指定的期间履行给付金钱义务,应当依照《中华人民共和国民事诉讼法》第二百五十三条之规定,加倍支付迟延履行期间的债务利息 。  \\n \\n案件受理费10元,减半计5元,免予收取 。  \\n \\n如不服本判决,可在判决书送达之日起十五日内,向本院递交上诉状,并按对方当事人的人数提出副本,上诉于上海市第一中级人民法院 。 ', '日期': '2020-01-20 00:00:00', '文件名': '（2019）沪0115民初91149号.txt', '起诉日期': '2019'}, {'关联公司': '上海爱斯达克汽车空调系统有限公司', '标题': '上海贝众汽车零部件有限公司与上海爱斯达克汽车空调系统有限公司技术委托开发合同纠纷民事一审案件民事判决书', '案号': '(2020)沪0115民初3857号', '文书类型': '民事判决书', '原告': '上海贝众汽车零部件有限公司', '被告': '上海爱斯达克汽车空调系统有限公司', '原告律师事务所': '上海远同律师事务所', '被告律师事务所': '上海步界律师事务所', '案由': '技术委托开发合同纠纷', '涉案金额': '21849', '判决结果': '一、被告上海爱斯达克汽车空调系统有限公司于本判决生效之日起十日内支付原告上海贝众汽车零部件有限公司差旅费21,849元; \\n \\n二、驳回原告上海贝众汽车零部件有限公司的其余诉讼请求 。  \\n \\n如果未按本判决指定的期间履行给付义务,应当依照《中华人民共和国民事诉讼法》第二百五十三条的规定,加倍支付迟延履行期间的债务利息 。  \\n \\n案件受理费14,225元,由原告上海贝众汽车零部件有限公司负担9,225元,被告上海爱斯达克汽车空调系统有限公司负担5,000元 。  \\n \\n如不服本判决,可在判决书送达之日起十五日内,向本院递交上诉状,并按照对方当事人或者代表人的人数提出副本,上诉于上海知识产权法院 。 ', '日期': '2021-04-28 00:00:00', '文件名': '（2020）沪0115民初3857号.txt', '起诉日期': '2020'}])
    print(filter_(query="这些案件中，起诉时间发生在2019年且涉案金额大于1万的有哪些？", info=info))