import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def create(text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Faca um resumo dessa noticia, sem titulo."
            },
            {
                "role": "user",
                "content": text,
            }
        ],
        model="gpt-4-turbo-2024-04-09",
    )

    # print(chat_completion.choices[0].message.content)
    print(chat_completion.usage)

    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    pass
