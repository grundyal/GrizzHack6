 

from openai import OpenAI
client = OpenAI(api_key = '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')
 
while True: 
    message = input("User : ") 
    if message: 
        response = client.chat.completions.create(
            model="ft:gpt-3.5-turbo-1106:personal::90xE7Lwg",
            messages=[
                {"role": "user", "content": message}
            ]
            )
    print(f"ChatGPT: {response}") 