
from zhipuai import ZhipuAI
client = ZhipuAI(api_key="3781d8b976c5d1f75aacb3f957a3e36b.96ddhBau7UjekRId")
while True:
    prompt=input("user:")
    response = client.chat.completions.create(
        model="glm-4-0520",  # 填写需要调用的模型编码
        messages=[
            {"role": "user", "content": prompt},
        ],
        )
    print(response.choices[0].message.content)