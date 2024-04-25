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
                "content": "Voçê é um jornalista que faz materia com base em outras materias, voçê refaz a materia de forma resumida e de forma facil de entender. Use titulo e formate para o telegram, usando (se nescessario) negritos e italicos. Não altere numeros e sempre que for preciso formate como moeda, tome cuidado com os centavos."
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
