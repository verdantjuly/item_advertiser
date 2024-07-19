import os
from openai import OpenAI


def ai_text(prompt):
    
    os.environ["OPENAI_API_KEY"] = "API-KEY"

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{prompt}를 홍보하는 문구를 100자 이내로 적어 줘",
            }
        ],
        model="gpt-4o",
    )

    result = chat_completion.choices[0].message.content

    return result