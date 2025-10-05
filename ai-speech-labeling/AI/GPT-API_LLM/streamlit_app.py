import os
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

# .envからAPIキーを読み込む
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit設定
st.set_page_config(page_title="GPT Chat App", page_icon="🤖")
st.title("🤖 GPT Chat App")
st.write("Chat with GPT in your browser!")

# 入力欄
if "messages" not in st.session_state:
    st.session_state["messages"] = []

user_input = st.text_input("質問を入力してください:")

# 送信ボタンを押したら応答を取得
if st.button("送信"):
    if user_input:
        # ユーザーの入力を保存
        st.session_state["messages"].append({"role": "user", "content": user_input})

        with st.spinner("GPTが考えています..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state["messages"]
            )
            answer = response.choices[0].message.content

        # GPTの返答を保存
        st.session_state["messages"].append({"role": "assistant", "content": answer})

# チャット履歴を表示
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**あなた:** {msg['content']}")
    else:
        st.markdown(f"**GPT:** {msg['content']}")
