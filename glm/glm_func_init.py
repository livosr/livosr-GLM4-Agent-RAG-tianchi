from zhipuai import ZhipuAI
import requests
import json

api_key = "8f5594ef782d24752c0e875d8da33592.ElGxsEuPuzU9ra6C"
client = ZhipuAI(api_key=api_key)  # 请填写您自己的APIKey


def get_company_info(query: str, info: str) -> str:
    tools = [
        # 0、get_company_info
        {
            "type": "function",
            "function": {
                "name": "get_company_info",
                "description": '''
        根据上市公司名称、简称或代码查找上市公司信息
        入参：query_conds (dict[str, str]): 查询条件的字典,键为'公司名称'或'公司简称'或'公司代码'，\
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
        出参：dict[str, str]: 包含公司信息的字典。

                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_conds": {
                            "type": "dict[str, str]",
                            "description": "查询条件的字典,键为'公司名称'或'公司简称'或'公司代码'",
                        },
                        "need_fields": {
                            "type": "list[str]",
                            "description": '''need_fields, 属性名称(列表中的字段)包含，公司名称，公司简称，英文名称，关联证券，公司代码，曾用简称，所属市场，\
所属行业，成立日期，上市日期，法人代表，总经理，董秘，邮政编码，注册地址，办公地址，联系电话，传真，官方网址，电子邮箱，入选指数，\
主营业务，经营范围，机构简介，每股面值，首发价格，首发募资净额，首发主承销商。\
你需要找出最符合query的一个或几个需要查询的属性,属性必须是上述特征，一个字不能变。
'''}

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
    #print(response_arguments)
    return response_arguments, func_name

def get_company_register(query: str, info: str) -> str:
    tools = [
        # 1、get_company_register
        {
            "type": "function",
            "function": {
                "name": "get_company_register",
                "description": '''
        根据公司名称，查询工商信息
        入参：query_conds (dict[str, str]): 查询条件的字典,键为'公司名称'，\
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
        出参：dict[str, str]: 包含公司信息的字典。

                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_conds": {
                            "type": "dict[str, str]",
                            "description": "查询条件的字典,键为'公司名称'",
                        },
                        "need_fields": {
                            "type": "list[str]",
                            "description": '''need_fields, 属性名称(列表中的字段)包含，公司名称，登记状态，统一社会信用代码，\
法定代表人，注册资本，成立日期，企业地址，联系电话，联系邮箱，注册号，组织机构代码，参保人数，行业一级，行业二级，行业三级，曾用名，企业简介，经营范围。\
你需要找出最符合query的一个或几个需要查询的属性,属性必须是上述特征，一个字不能变。
'''}

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
    #print(response_arguments)
    return response_arguments, func_name


def get_company_register_name(query: str, info: str) -> str:
    tools = [
        # 2、get_company_register_name
        {
            "type": "function",
            "function": {
                "name": "get_company_register_name",
                "description": '''
        根据统一社会信用代码查询公司名称。
        入参：query_conds (dict[str, str]): 查询条件的字典,键为'统一社会信用代码'，\
        出参：dict[str, str]: {'公司名称': str}

                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_conds": {
                            "type": "dict[str, str]",
                            "description": "查询条件的字典,键为'统一社会信用代码'",
                        },


                    },
                    "required": ["query_conds"],
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
    #print(response_arguments)
    return response_arguments, func_name

def get_sub_company_info(query: str, info: str) -> str:
    tools = [
        # 3、get_sub_company_info
        {
            "type": "function",
            "function": {
                "name": "get_sub_company_info",
                "description": '''
        根据被投资的子公司名称获得投资该公司的上市公司、投资比例、投资金额等信息。
        入参：query_conds (dict[str, str]): 查询条件的字典,键为'公司名称'，\
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
        出参：dict[str, str]: 投资该公司的上市公司、投资比例、投资金额等信息的字典。

                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_conds": {
                            "type": "dict[str, str]",
                            "description": "查询条件的字典,键为'公司名称'",
                        },
                        "need_fields": {
                            "type": "list[str]",
                            "description": '''need_fields, 属性名称(列表中的字段)包含，关联上市公司全称，上市公司关系，上市公司参股比例，上市公司投资金额，公司名称。\
你需要找出最符合query的一个或几个需要查询的属性,属性必须是上述特征，一个字不能变。注意：关联上市公司全称字段就是母公司。
'''}

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
    #print(response_arguments)
    return response_arguments, func_name

def get_sub_company_info_list(query: str, info: str) -> str:
    tools = [
        # 4、get_sub_company_info_list
        {
            "type": "function",
            "function": {
                "name": "get_sub_company_info_list",
                "description": '''
        根据上市公司（母公司）的名称查询该公司投资的所有子公司信息list
        入参：query_conds (dict[str, str]): 查询条件的字典,键为'关联上市公司全称'，\
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
        出参：list[dict[str, str]]: 该公司投资的所有子公司信息list。

                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_conds": {
                            "type": "dict[str, str]",
                            "description": "查询条件的字典,键为'关联上市公司全称'",
                        },
                        "need_fields": {
                            "type": "list[str]",
                            "description": '''need_fields, 属性名称(列表中的字段)包含，关联上市公司全称，上市公司关系，上市公司参股比例，上市公司投资金额，公司名称。\
你需要找出最符合query的一个或几个需要查询的属性,属性必须是上述特征，一个字不能变。
'''}

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
    #print(response_arguments)
    return response_arguments, func_name

def get_legal_document(query: str, info: str) -> str:
    tools = [
        # 5、get_legal_document
        {
            "type": "function",
            "function": {
                "name": "get_legal_document",
                "description": '''
        根据案号查询裁判文书相关信息
        入参：query_conds (dict[str, str]): 查询条件的字典,键为'案号'，\
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
        出参：dict[str, str]: 裁判文书相关信息的字典。

                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_conds": {
                            "type": "dict[str, str]",
                            "description": "查询条件的字典,键为'案号'",
                        },
                        "need_fields": {
                            "type": "list[str]",
                            "description": '''need_fields, 属性名称(列表中的字段)包含，关联公司，标题，案号，文书类型，原告，被告，\
原告律师事务所，被告律师事务所，案由，涉案金额，判决结果，日期，文件名。\
你需要找出最符合query的一个或几个需要查询的属性,属性必须是上述特征，一个字不能变。
'''}

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
    #print(response_arguments)
    return response_arguments, func_name

def get_legal_document_list(query: str, info: str) -> str:
    tools = [
        # 6、get_legal_document_list
        {
            "type": "function",
            "function": {
                "name": "get_legal_document_list",
                "description": '''
        根据关联公司查询所有裁判文书相关信息list
        入参：query_conds (dict[str, str]): 查询条件的字典,键为'关联公司'，\
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
        出参：list[dict[str, str]]: 所有裁判文书相关信息list。

                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_conds": {
                            "type": "dict[str, str]",
                            "description": "查询条件的字典,键为'关联公司'",
                        },
                        "need_fields": {
                            "type": "list[str]",
                            "description": '''need_fields, 属性名称(列表中的字段)包含，关联公司，标题，案号，文书类型，\
原告，被告，原告律师事务所，被告律师事务所，案由，涉案金额，判决结果，日期，文件名。\
你需要找出最符合query的一个或几个需要查询的属性,属性必须是上述特征，一个字不能变。
'''}

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
    #print(response_arguments)
    return response_arguments, func_name

def get_court_info(query: str, info: str) -> str:
    tools = [
        # 7、get_court_info
        {
            "type": "function",
            "function": {
                "name": "get_court_info",
                "description": '''
        根据法院名称查询法院名录相关信息
        入参：query_conds (dict[str, str]): 查询条件的字典,键为'法院名称'，\
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
        出参：dict[str, str]: 法院名录相关信息的字典。

                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_conds": {
                            "type": "dict[str, str]",
                            "description": "查询条件的字典,键为'法院名称'",
                        },
                        "need_fields": {
                            "type": "list[str]",
                            "description": '''need_fields, 属性名称(列表中的字段)包含，法院名称，法院负责人，成立日期，法院地址，法院联系电话，法院官网。\
你需要找出最符合query的一个或几个需要查询的属性,属性必须是上述特征，一个字不能变。
'''}

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
    #print(response_arguments)
    return response_arguments, func_name

def get_court_code(query: str, info: str) -> str:
    tools = [
        # 8、get_court_code
        {
            "type": "function",
            "function": {
                "name": "get_court_code",
                "description": '''
        根据法院名称或者法院代字查询法院代字等相关数据
        入参：query_conds (dict[str, str]): 查询条件的字典,键为'法院名称'或'法院代字'，\
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
        出参：dict[str, str]: 法院代字等相关数据的字典。

                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_conds": {
                            "type": "dict[str, str]",
                            "description": "查询条件的字典,键为'法院名称'或'法院代字'",
                        },
                        "need_fields": {
                            "type": "list[str]",
                            "description": '''need_fields, 属性名称(列表中的字段)包含，法院名称，行政级别，法院级别，法院代字，区划代码，级别。\
你需要找出最符合query的一个或几个需要查询的属性,属性必须是上述特征，一个字不能变。
'''}

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
    #print(response_arguments)
    return response_arguments, func_name

def get_lawfirm_info(query: str, info: str) -> str:
    tools = [
        # 9、get_lawfirm_info
        {
            "type": "function",
            "function": {
                "name": "get_lawfirm_info",
                "description": '''
        根据律师事务所查询律师事务所名录
        入参：query_conds (dict[str, str]): 查询条件的字典,键为'律师事务所名称'，\
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
        出参：dict[str, str]: 律师事务所名录的字典。

                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_conds": {
                            "type": "dict[str, str]",
                            "description": "查询条件的字典,键为'律师事务所名称'",
                        },
                        "need_fields": {
                            "type": "list[str]",
                            "description": '''need_fields, 属性名称(列表中的字段)包含，律师事务所名称，律师事务所唯一编码，律师事务所负责人，事务所注册资本，事务所成立日期，律师事务所地址，通讯电话，通讯邮箱，律所登记机关。\
你需要找出最符合query的一个或几个需要查询的属性,属性必须是上述特征，一个字不能变。
'''}

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
    #print(response_arguments)
    return response_arguments, func_name

def get_lawfirm_log(query: str, info: str) -> str:
    tools = [
        # 10、get_lawfirm_log
        {
            "type": "function",
            "function": {
                "name": "get_lawfirm_log",
                "description": '''
        根据律师事务所查询律师事务所统计数据
        入参：query_conds (dict[str, str]): 查询条件的字典,键为'律师事务所名称'，\
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
        出参：dict[str, str]: 律师事务所统计数据的字典。

                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_conds": {
                            "type": "dict[str, str]",
                            "description": "查询条件的字典,键为'律师事务所名称'",
                        },
                        "need_fields": {
                            "type": "list[str]",
                            "description": '''need_fields, 属性名称(列表中的字段)包含，律师事务所名称，业务量排名，服务已上市公司，报告期间所服务上市公司违规事件，报告期所服务上市公司接受立案调查。\
你需要找出最符合query的一个或几个需要查询的属性,属性必须是上述特征，一个字不能变。
'''}

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
    #print(response_arguments)
    return response_arguments, func_name


def get_address_info(query: str, info: str) -> str:
    tools = [
        # 11、get_address_info
        {
            "type": "function",
            "function": {
                "name": "get_address_info",
                "description": '''
        根据地址查该地址对应的省份城市区县
        入参：query_conds (dict[str, str]): 查询条件的字典,键为'地址'，\
        need_fields (list[str]): 需要返回的字段列表。need_fields传入空列表，则表示返回所有字段，否则返回填入的字段
        出参：dict[str, str]: 该地址对应的省份城市区县的字典。

                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_conds": {
                            "type": "dict[str, str]",
                            "description": "查询条件的字典,键为'地址'",
                        },
                        "need_fields": {
                            "type": "list[str]",
                            "description": '''need_fields, 属性名称(列表中的字段)包含，地址，省份，城市，区县。\
你需要找出最符合query的一个或几个需要查询的属性,属性必须是上述特征，一个字不能变。
'''}

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
    #print(response_arguments)
    return response_arguments, func_name


def get_citizens_sue_citizens(query: str, info: str) -> str:
    tools = [
        # 20、get_citizens_sue_citizens
        {
            "type": "function",
            "function": {
                "name": "get_citizens_sue_citizens",
                "description": '''
        民事起诉状(公民起诉公民)
        入参：data: dict[str, str]: 传入的民事起诉状(公民起诉公民)的字典信息
        出参：str: 民事起诉状(公民起诉公民)。

                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "data": {
                            "type": "dict[str, str]",
                            "description": '''data, 属性名称(列表中的字段)包含，原告，原告性别，\
原告生日，原告民族，原告工作单位，原告地址，原告联系方式，原告委托诉讼代理人，原告委托诉讼代理人联系方式，\
被告，被告性别，被告生日，被告民族，被告工作单位，被告地址，被告联系方式，被告委托诉讼代理人，被告委托诉讼代理人联系方式，\
诉讼请求，事实和理由，证据，法院名称，起诉日期。\
你需要找出最符合query的一个或几个需要查询的属性,属性必须是上述特征，一个字不能变。
'''}

                    },
                    "required": ["data"],
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
    #print(response_arguments)
    return response_arguments, func_name

def get_company_sue_citizens(query: str, info: str) -> str:
    tools = [
        # 21、get_company_sue_citizens
        {
            "type": "function",
            "function": {
                "name": "get_company_sue_citizens",
                "description": '''
        民事起诉状(公司起诉公民)
        入参：data: dict[str, str]: 传入的民事起诉状(公司起诉公民)的字典信息
        出参：str: 民事起诉状(公司起诉公民)。

                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "data": {
                            "type": "dict[str, str]",
                            "description": '''data, 属性名称(列表中的字段)包含，原告，原告地址，\
原告法定代表人，原告联系方式，原告委托诉讼代理人，原告委托诉讼代理人联系方式，被告，被告性别，被告生日，被告民族，\
被告工作单位，被告地址，被告联系方式，被告委托诉讼代理人，被告委托诉讼代理人联系方式，诉讼请求，事实和理由，证据，法院名称，起诉日期。\
你需要找出最符合query的一个或几个需要查询的属性,属性必须是上述特征，一个字不能变。
'''}

                    },
                    "required": ["data"],
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
    #print(response_arguments)
    return response_arguments, func_name

def get_citizens_sue_company(query: str, info: str) -> str:
    tools = [
        # 22、get_citizens_sue_company
        {
            "type": "function",
            "function": {
                "name": "get_citizens_sue_company",
                "description": '''
        民事起诉状(公民起诉公司)
        入参：data: dict[str, str]: 传入的民事起诉状(公民起诉公司)的字典信息
        出参：str: 民事起诉状(公民起诉公司)。

                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "data": {
                            "type": "dict[str, str]",
                            "description": '''data, 属性名称(列表中的字段)包含，原告，原告性别，原告生日，\
原告民族，原告工作单位，原告地址，原告联系方式，原告委托诉讼代理人，原告委托诉讼代理人联系方式，被告，被告地址，被告法定代表人，\
被告联系方式，被告委托诉讼代理人，被告委托诉讼代理人联系方式，诉讼请求，事实和理由，证据，法院名称，起诉日期。\
你需要找出最符合query的一个或几个需要查询的属性,属性必须是上述特征，一个字不能变。
'''}

                    },
                    "required": ["data"],
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
    #print(response_arguments)
    return response_arguments, func_name

def get_company_sue_company(query: str, info: str) -> str:
    tools = [
        # 23、get_company_sue_company
        {
            "type": "function",
            "function": {
                "name": "get_company_sue_company",
                "description": '''
        民事起诉状(公司起诉公司)
        入参：data: dict[str, str]: 传入的民事起诉状(公司起诉公司)的字典信息
        出参：str: 民事起诉状(公司起诉公司)。

                        ''',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "data": {
                            "type": "dict[str, str]",
                            "description": '''data, 属性名称(列表中的字段)包含，原告，原告地址，原告法定代表人，\
原告联系方式，原告委托诉讼代理人，原告委托诉讼代理人联系方式，被告，被告地址，被告法定代表人，被告联系方式，被告委托诉讼代理人，\
被告委托诉讼代理人联系方式，诉讼请求，事实和理由，证据，法院名称，起诉日期。\
你需要找出最符合query的一个或几个需要查询的属性,属性必须是上述特征，一个字不能变。
'''}

                    },
                    "required": ["data"],
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
    #print(response_arguments)
    return response_arguments, func_name



# response_arguments, func_name = get_company_info(query="我想了解一下山东南山智尚科技股份有限公司的股票代码和股票简称是？",info='')
# print(response_arguments)
# print(func_name)