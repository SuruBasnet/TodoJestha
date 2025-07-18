from groq import Groq
import os

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def create_description_with_ai(todo_title):
    completion = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
        {
            "role": "system",
            "content": "You are helpful AI agent. Respond in json."
        },
        {
            "role": "user",
            "content": f"Give me a brief description according to my todo : {todo_title}"
        }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        response_format={"type": "json_object"},
        stop=None,
    )

    return completion.choices[0].message.content
