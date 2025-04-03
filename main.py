import streamlit as st
import subprocess

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot với Streamlit")

# Ô nhập cho người dùng
user_input = st.text_input("Nhập câu hỏi của bạn:")

# Đường dẫn đến llama.cpp (chỉnh lại nếu cần)
LLAMA_PATH = r"llama.cpp\build\bin\release\llama-cli.exe"
MODEL_PATH = r"model\model.gguf"

# Nút gửi yêu cầu
if st.button("Gửi"):
    if user_input:
        # Lệnh chạy Llama.cpp
        command = [LLAMA_PATH, "-m", MODEL_PATH, "-c", "256", "-p", user_input]

        try:
            # Chạy lệnh bằng subprocess
            result = subprocess.run(command, capture_output=True, text=True)

            # Kiểm tra kết quả
            if result.returncode == 0:
                st.success(f"AI: {result.stdout.strip()}")
            else:
                st.error(f"Lỗi khi chạy Llama.cpp: {result.stderr.strip()}")

        except Exception as e:
            st.error(f"Lỗi hệ thống: {str(e)}")


#  ./llama.cpp/build/bin/release/llama-cli.exe -m model/model.gguf -c 256
