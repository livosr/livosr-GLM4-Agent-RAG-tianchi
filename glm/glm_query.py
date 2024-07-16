from zhipuai import ZhipuAI
import json
api_key = "8f5594ef782d24752c0e875d8da33592.ElGxsEuPuzU9ra6C"  # 肖的token
client = ZhipuAI(api_key=api_key) # 请填写您自己的APIKey

def get_answer(info_dict, query):
    messages = [
        {
            "role": "system",
            "content": "你是一个优秀的问答机器人，可以根据给定的query和给定的python字典信息,生成答案。要求如下：\n1、请确认你的答案是包含题干信息与查询结果\n2.不要输出多余的信息（不要输出‘根据查询结果’等语句）"
        },
        {
            "role": "user",
            "content": "查询结果包括：{}\n, query:{}\n".format(str(info_dict), query)
        }
    ]

    #print(messages)
    response = client.chat.completions.create(
        model="glm-4", # 填写需要调用的模型名称
        messages=messages,
        # tools=tools_get_attribution,
        tool_choice="auto",
        temperature=0,
    )
    #print(response)
    response_arguments = response.choices[0].message.content
    return response_arguments