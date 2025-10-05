import os
from openai import OpenAI
from dotenv import load_dotenv

# .env から APIキーを読み込み
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # 軽量＆高速モデル
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("=== GPT Chat App ===")
    while True:
        user = input("あなた: ")
        if user.lower() in ["exit", "quit"]:
            print("終了します。")
            break
        answer = ask_gpt(user)
        print("GPT:", answer)

