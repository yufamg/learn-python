from openai import OpenAI


def get_response():
    client = OpenAI(
        # 若没有配置环境变量，请用阿里云百炼API Key将下行替换为：api_key="sk-xxx",
        # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
        api_key="sk-ws-H.RYXILXR.jCvS.MEUCIHw_gOk_8M3FTe3veBywu-Pef1oOYcx9KkICmtBwjFtCAiEA9hz7f6x0jXlJR0ahcFBWELVrWeFPPy6hpiLTYa7lIoY",
        # 以下是北京地域base_url
        base_url="https://llm-ezp2v93jgqlt4vum.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
    )
    response = client.responses.create(
        model="qwen-plus",
        input="写一个关于独角兽的短 bedtime story。使用中文简体",
    )

    print(response)
    # completion = client.chat.completions.create(
    #     model="qwen-plus",  # 此处以qwen-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    #     messages=[{'role': 'system', 'content': 'You are a helpful assistant.'},
    #               {'role': 'user', 'content': '你是谁？'}]
    #     )
    # print(completion.model_dump_json())


if __name__ == "__main__":
    get_response()
# #  面向对象编程
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def say_hello(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old")


# person = Person("John", 20)
# person.say_hello()
# print(pi, sin(pi / 2))
