import json
import sys

sys.path.append(r'C:\PycharmProjects\yuyuelin_b')
import glm.glm_query as glm
import glm.glm_func_init as glm_func_init
import glm.glm_func_init2 as glm_func_init2

import api.get_api_response as get_api_response


def str_to_bool(s):
    # 使用字典映射常见的布尔字符串表示
    true_values = {"true", "1", "yes", "y", "on"}
    false_values = {"false", "0", "no", "n", "off"}

    s = s.lower()

    if s in true_values:
        return True
    elif s in false_values:
        return False
    else:
        raise ValueError(f"Cannot convert string '{s}' to bool")


# 第一步：函数序号与对应的函数名称（根据提取的子问题分割的函数序号来映射到相应的函数名称）
func_dict = {
    "0": "get_company_info",
    "1": "get_company_register",
    "2": "get_company_register_name",
    "3": "get_sub_company_info",
    "4": "get_sub_company_info_list",
    "5": "get_legal_document",
    "6": "get_legal_document_list",
    "7": "get_court_document",
    "8": "get_court_code",
    "9": "get_lawfirm_info",
    "10": "get_lawfirm_log",
    "11": "get_address_info",
    "12": "get_address_code",
    "13": "get_temp_info",
    "14": "get_legal_abstract",
    "15": "get_xzgxf_info",
    "16": "get_xzgxf_info_list",
    "17": "get_sum",
    "18": "rank",
    "19": "save_dict_list_to_word",
    "20": "get_citizens_sue_citizens",
    "21": "get_company_sue_citizens",
    "22": "get_citizens_sue_company",
    "23": "get_company_sue_company",
    "24": "filter_"
}


# 第二步：调用大模型，通过query和info获取服务的输入参数
def get_function_init(function_name, query, info):
    if function_name == "get_company_info":
        return glm_func_init.get_company_info(query=query, info=info)
    elif function_name == "get_company_register":
        return glm_func_init.get_company_register(query=query, info=info)
    elif function_name == "get_company_register_name":
        return glm_func_init.get_company_register_name(query=query, info=info)
    elif function_name == "get_sub_company_info":
        return glm_func_init.get_sub_company_info(query=query, info=info)
    elif function_name == "get_sub_company_info_list":
        return glm_func_init.get_sub_company_info_list(query=query, info=info)
    elif function_name == "get_legal_document":
        return glm_func_init.get_legal_document(query=query, info=info)
    elif function_name == "get_legal_document_list":
        return glm_func_init.get_legal_document_list(query=query, info=info)
    elif function_name == "get_court_info":
        return glm_func_init.get_court_info(query=query, info=info)
    elif function_name == "get_court_code":
        return glm_func_init.get_court_code(query=query, info=info)
    elif function_name == "get_lawfirm_info":
        return glm_func_init.get_lawfirm_info(query=query, info=info)
    elif function_name == "get_lawfirm_log":
        return glm_func_init.get_lawfirm_log(query=query, info=info)
    elif function_name == "get_address_info":
        return glm_func_init.get_address_info(query=query, info=info)
    elif function_name == "get_address_code":
        return glm_func_init2.get_address_code(query=query, info=info)
    elif function_name == "get_temp_info":
        return glm_func_init2.get_temp_info(query=query, info=info)
    elif function_name == "get_legal_abstract":
        return glm_func_init2.get_legal_abstract(query=query, info=info)
    elif function_name == "get_xzgxf_info":
        return glm_func_init2.get_xzgxf_info(query=query, info=info)
    elif function_name == "get_xzgxf_info_list":
        return glm_func_init2.get_xzgxf_info_list(query=query, info=info)
    elif function_name == "get_sum":
        return glm_func_init2.get_sum(query=query, info=info)
    elif function_name == "rank":
        return glm_func_init2.rank(query=query, info=info)
    elif function_name == "save_dict_list_to_word":
        return glm_func_init2.save_dict_list_to_word(query=query, info=info)
    elif function_name == "get_citizens_sue_citizens":
        return glm_func_init.get_citizens_sue_citizens(query=query, info=info)
    elif function_name == "get_company_sue_citizens":
        return glm_func_init.get_company_sue_citizens(query=query, info=info)
    elif function_name == "get_citizens_sue_company":
        return glm_func_init.get_citizens_sue_company(query=query, info=info)
    elif function_name == "get_company_sue_company":
        return glm_func_init.get_company_sue_company(query=query, info=info)
    elif function_name == "filter_":
        return glm_func_init2.filter_(query=query, info_=info)
    else:
        raise EOFError("Function not found")


# 第三步：调用服务
def service_execution(func_config_dict, function_name):
    if function_name == "get_company_info":  # 0

        query_conds = func_config_dict["query_conds"]
        need_fields = func_config_dict["need_fields"]
        query_conds_keys = list(query_conds.keys())
        if "Items" in query_conds_keys:
            query_conds = query_conds["Items"]
        if isinstance(need_fields, dict):
            need_fields = need_fields["Items"]
        info = get_api_response.get_company_info(query_conds, need_fields)
        return info

    elif function_name == "get_company_register":  # 1
        query_conds = func_config_dict["query_conds"]
        need_fields = func_config_dict["need_fields"]
        query_conds_keys = list(query_conds.keys())
        if "Items" in query_conds_keys:
            query_conds = query_conds["Items"]
        if isinstance(need_fields, dict):
            need_fields = need_fields["Items"]
        info = get_api_response.get_company_register(query_conds, need_fields)
        return info


    elif function_name == "get_company_register_name":  # 2

        query_conds = func_config_dict["query_conds"]
        query_conds_keys = list(query_conds.keys())
        if "Items" in query_conds_keys:
            query_conds = query_conds["Items"]
        info = get_api_response.get_company_register_name(query_conds)
        return info


    elif function_name == "get_sub_company_info":  # 3

        query_conds = func_config_dict["query_conds"]
        need_fields = func_config_dict["need_fields"]
        query_conds_keys = list(query_conds.keys())
        if "Items" in query_conds_keys:
            query_conds = query_conds["Items"]
        if isinstance(need_fields, dict):
            need_fields = need_fields["Items"]
        info = get_api_response.get_sub_company_info(query_conds, need_fields)
        return info


    elif function_name == "get_sub_company_info_list":  # 4

        query_conds = func_config_dict["query_conds"]
        need_fields = func_config_dict["need_fields"]
        query_conds_keys = list(query_conds.keys())
        if "Items" in query_conds_keys:
            query_conds = query_conds["Items"]
        if isinstance(need_fields, dict):
            need_fields = need_fields["Items"]
        info = get_api_response.get_sub_company_info_list(query_conds, need_fields)
        return info


    elif function_name == "get_legal_document":  # 5

        query_conds = func_config_dict["query_conds"]
        need_fields = func_config_dict["need_fields"]
        query_conds_keys = list(query_conds.keys())
        if "Items" in query_conds_keys:
            query_conds = query_conds["Items"]
        if isinstance(need_fields, dict):
            need_fields = need_fields["Items"]
        info = get_api_response.get_legal_document(query_conds, need_fields)
        return info


    elif function_name == "get_legal_document_list":  # 6
        # try:

        query_conds = func_config_dict["query_conds"]
        need_fields = func_config_dict["need_fields"]
        query_conds_keys = list(query_conds.keys())
        print("===========6============")
        if "Items" in query_conds_keys:
            query_conds = query_conds["Items"]
        print(query_conds)
        print(need_fields)

        if isinstance(need_fields, dict):
            need_fields = need_fields["Items"]
        print(query_conds, need_fields)

        info = get_api_response.get_legal_document_list(query_conds, need_fields)
        return info
    # except Exception as e:
    #     print(e)
    #     return ""

    elif function_name == "get_court_info":  # 7

        query_conds = func_config_dict["query_conds"]
        need_fields = func_config_dict["need_fields"]
        query_conds_keys = list(query_conds.keys())
        if "Items" in query_conds_keys:
            query_conds = query_conds["Items"]
        if isinstance(need_fields, dict):
            need_fields = need_fields["Items"]
        info = get_api_response.get_court_info(query_conds, need_fields)
        return info


    elif function_name == "get_court_code":  # 8

        query_conds = func_config_dict["query_conds"]
        need_fields = func_config_dict["need_fields"]
        query_conds_keys = list(query_conds.keys())
        if "Items" in query_conds_keys:
            query_conds = query_conds["Items"]
        if isinstance(need_fields, dict):
            need_fields = need_fields["Items"]
        info = get_api_response.get_court_code(query_conds, need_fields)
        return info


    elif function_name == "get_lawfirm_info":  # 9

        query_conds = func_config_dict["query_conds"]
        need_fields = func_config_dict["need_fields"]
        query_conds_keys = list(query_conds.keys())
        if "Items" in query_conds_keys:
            query_conds = query_conds["Items"]
        if isinstance(need_fields, dict):
            need_fields = need_fields["Items"]
        info = get_api_response.get_lawfirm_info(query_conds, need_fields)
        return info


    elif function_name == "get_lawfirm_log":  # 10

        query_conds = func_config_dict["query_conds"]
        need_fields = func_config_dict["need_fields"]
        query_conds_keys = list(query_conds.keys())
        if "Items" in query_conds_keys:
            query_conds = query_conds["Items"]
        if isinstance(need_fields, dict):
            need_fields = need_fields["Items"]
        info = get_api_response.get_lawfirm_log(query_conds, need_fields)
        return info


    elif function_name == "get_address_info":  # 11

        query_conds = func_config_dict["query_conds"]
        need_fields = func_config_dict["need_fields"]
        query_conds_keys = list(query_conds.keys())
        if "Items" in query_conds_keys:
            query_conds = query_conds["Items"]
        if isinstance(need_fields, dict):
            need_fields = need_fields["Items"]
        info = get_api_response.get_address_info(query_conds, need_fields)
        return info


    elif function_name == "get_address_code":  # 12

        query_conds = func_config_dict["query_conds"]
        need_fields = func_config_dict["need_fields"]
        query_conds_keys = list(query_conds.keys())
        if "Items" in query_conds_keys:
            query_conds = query_conds["Items"]
        if isinstance(need_fields, dict):
            need_fields = need_fields["Items"]
        info = get_api_response.get_address_code(query_conds, need_fields)
        return info


    elif function_name == "get_temp_info":  # 13

        query_conds = func_config_dict["query_conds"]
        need_fields = func_config_dict["need_fields"]
        query_conds_keys = list(query_conds.keys())
        if "Items" in query_conds_keys:
            query_conds = query_conds["Items"]
        if isinstance(need_fields, dict):
            need_fields = need_fields["Items"]
        info = get_api_response.get_temp_info(query_conds, need_fields)
        return info


    elif function_name == "get_legal_abstract":  # 14

        query_conds = func_config_dict["query_conds"]
        need_fields = func_config_dict["need_fields"]
        query_conds_keys = list(query_conds.keys())
        if "Items" in query_conds_keys:
            query_conds = query_conds["Items"]
        if isinstance(need_fields, dict):
            need_fields = need_fields["Items"]
        info = get_api_response.get_legal_abstract(query_conds, need_fields)
        return info


    elif function_name == "get_xzgxf_info":  # 15

        query_conds = func_config_dict["query_conds"]
        need_fields = func_config_dict["need_fields"]
        query_conds_keys = list(query_conds.keys())
        if "Items" in query_conds_keys:
            query_conds = query_conds["Items"]
        if isinstance(need_fields, dict):
            need_fields = need_fields["Items"]
        info = get_api_response.get_xzgxf_info(query_conds, need_fields)
        return info


    elif function_name == "get_xzgxf_info_list":  # 16

        query_conds = func_config_dict["query_conds"]
        need_fields = func_config_dict["need_fields"]
        query_conds_keys = list(query_conds.keys())
        if "Items" in query_conds_keys:
            query_conds = query_conds["Items"]
        if isinstance(need_fields, dict):
            need_fields = need_fields["Items"]
        info = get_api_response.get_xzgxf_info_list(query_conds, need_fields)
        return info


    elif function_name == "get_sum":  # 17

        nums = func_config_dict["nums"]
        nums_keys = list(nums.keys())
        if "Items" in nums_keys:
            nums = nums["Items"]
        info = get_api_response.get_sum(nums)
        return info


    elif function_name == "rank":  # 18

        dict_18 = func_config_dict["dict"]
        is_desc = func_config_dict["is_desc"]
        dict_keys = list(dict_18.keys())
        if "Items" in dict_keys:
            dict_18 = dict_18["Items"]
        if isinstance(is_desc, dict):
            is_desc = is_desc["Items"]
        info = get_api_response.rank(dict_18, is_desc)
        return info


    elif function_name == "save_dict_list_to_word":  # 19

        company_name = func_config_dict["company_name"]
        dict_list = func_config_dict["dict_list"]
        company_name_keys = list(company_name.keys())
        if "Items" in company_name_keys:
            company_name = company_name["Items"]
        if isinstance(dict_list, dict):
            dict_list = dict_list["Items"]
        info = get_api_response.save_dict_list_to_word(company_name, dict_list)
        return info


    elif function_name == "get_citizens_sue_citizens":  # 20

        data = func_config_dict["data"]
        data_keys = list(data.keys())
        if "Items" in data_keys:
            data = data["Items"]
        info = get_api_response.get_citizens_sue_citizens(data)
        return info


    elif function_name == "get_company_sue_citizens":  # 21

        data = func_config_dict["data"]
        data_keys = list(data.keys())
        if "Items" in data_keys:
            data = data["Items"]
        info = get_api_response.get_company_sue_citizens(data)
        return info

    elif function_name == "get_citizens_sue_company":  # 22

        data = func_config_dict["data"]
        data_keys = list(data.keys())
        if "Items" in data_keys:
            data = data["Items"]
        info = get_api_response.get_citizens_sue_company(data)
        return info


    elif function_name == "get_company_sue_company":  # 23

        data = func_config_dict["data"]
        data_keys = list(data.keys())
        if "Items" in data_keys:
            data = data["Items"]
        info = get_api_response.get_company_sue_company(data)
        return info


    elif function_name == "filter_":  # 24

        input_list = func_config_dict["input_list"]
        input_info = func_config_dict["input_info"]
        # print(input_list)
        # input_list_keys = list(input_list.keys())
        # if "Items" in input_list_keys:
        #     input_list = input_list["Items"]
        # if isinstance(input_info, dict):
        #     dict_list = input_info["Items"]
        print("input_list = ", input_list)
        info = get_api_response.filter_(input_list, input_info)
        return info


# agent执行函数，感觉都得查表，所以删除了最开始需不需要查表的二分类
def agent_chain(question_dict: dict) -> str:
    # 获取问题与子问题列表
    question = question_dict["question"]
    sub_question_list = question_dict["sub_question"]
    # 生成子问题列表
    print("sub_question_list:{}".format(sub_question_list))
    if isinstance(sub_question_list, str):
        sub_question_list = eval(sub_question_list)
    info = ''
    question_res_list = []
    for i, sub_question_dict in enumerate(sub_question_list):
        service_num = sub_question_dict["func"].strip().split('.')[0]  # 获取函数序号
        function_name = func_dict[service_num]  # 根据函数序号获取函数名称

        sub_question = sub_question_dict["sub_question"]  # 获取每个子问题
        print("\nsub_question_dict:{}".format(sub_question_dict))
        print("service_num:{}".format(service_num))
        print("function_name:{}".format(function_name))

        response_argument, func_name_glm = get_function_init(function_name=function_name, query=sub_question,
                                                             info=info)  # 获取函数名称、函数入参
        info = service_execution(func_config_dict=response_argument, function_name=function_name)  # 获取函数执行结果
        res_dict = {"question": sub_question, "result": info}  # 存储的获取函数名称、函数入参

        print("response_argument:{}".format(response_argument))
        print("func_name_glm:{}".format(func_name_glm))
        print("info:{}".format(info))

        if info == "":
            continue
        question_res_list.append(res_dict)
    print("question_res_list:{}".format(question_res_list))

    answer = glm.get_answer(question, question_res_list)  # 利用glm整合#获取函数名称、函数入参获得最终答案

    print("answer:", answer)
    return answer


if __name__ == '__main__':
    sub_question_filename = "sub_717_1.json"
    with open(file=sub_question_filename, encoding="utf-8", mode="r") as f:
        lines = f.readlines()
    for data in lines[:1]:
        sub_list = []

        try:
            # 第一次反序列化，将字符串转换为字典
            outer_dict = json.loads(data)

            #print("Outer dict:", outer_dict)  # 输出外层字典以调试

            # 第二次反序列化，处理 sub_question 字段中的嵌套 JSON 字符串
            sub_question_str = outer_dict['sub_question']
            #print("Sub-question string:", sub_question_str)  # 输出嵌套的 JSON 字符串以调试

            sub_question_list = eval(sub_question_str)
            # print("sub_question_list:{}".format(sub_question_list))
            # print("Is sub_question a list:", isinstance(sub_question_list, list))

            for sub_question_func_str in sub_question_list:
                #print("sub_question_func_str:{}".format(sub_question_func_str))
                sub_question_func_dict = json.loads(sub_question_func_str)
                sub_list.append({"sub_question":sub_question_func_dict['sub_question'] , "func": sub_question_func_dict['func'].split(" ")[0]})

            # 打印最终解析结果
            # print("Sub-question dict:", sub_question_dict)
            # print("Is sub_question a dict:", isinstance(sub_question_dict, dict))
            outer_dict['sub_question'] = sub_list

            answer = agent_chain(question_dict=outer_dict)

            print(outer_dict)
            outer_dict['answer'] = answer

            with open(file="ans.json", encoding="utf-8", mode="a") as f:
                f.write(json.dumps(outer_dict, ensure_ascii=False))

        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")
            continue
    exit(0)

    # question_dict = json.loads(lines[75])  # 获取sub_question文件中某个question及其子问题分割列表
    # 直接给question_dict赋值

    # question_dict = {"id": 3, "question": "保定市天威西路2222号地址对应的省市区县分别是？",
    #                  "sub_question": [{"sub_question": "保定市天威西路2222号地址对应的省市区县分别是？", "func": "11"}]}
    # print("question_dict:{}".format(question_dict))
    # print(agent_chain(question_dict=question_dict))
    # exit(0)
