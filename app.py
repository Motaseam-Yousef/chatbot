import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set the API key
api_key = os.getenv("OPENAI_API_KEY")

# Load data from file
file_path = 'data/data_01.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.readlines()

# Chatbot prompt setup
prompt = f"""
أنت مساعد ذكاء اصطناعي للشركة، مهمتك تقديم إجابات دقيقة ومفصلة حول بيانات وخدمات الشركة بناءً على المعلومات المتاحة. يجب أن تكون جميع إجاباتك باللغة العربية، وتقتصر فقط على معلومات الشركة. تأكد من أن تكون استجاباتك واضحة ومباشرة وتلبي استفسارات العملاء بشكل احترافي.

لتقديم تجربة ممتازة، قم باتباع التعليمات التالية:

1. استخدم دائمًا اللغة العربية الفصحى، واجعل أسلوبك ودودًا واحترافيًا.
2. التزم بالمعلومات المتاحة فقط ضمن بيانات الشركة، وتجنب الإجابة عن أي استفسارات لا تتعلق بالشركة أو لا تتوفر لها معلومات في قاعدة البيانات الخاصة بها.
3. قدم استجابات مختصرة وشاملة، مع توضيح التفاصيل ذات الصلة فقط حسب احتياج السؤال.

معلومات الشركة:
{data}
"""

openai.api_key = api_key
MODEL = "gpt-4o"

# Define a function to respond as a customer service chatbot
def chatbot_response(user_input):
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

# Streamlit app layout
st.set_page_config(page_title="سواعد بوت", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS for RTL styling and improved UI
st.markdown("""
    <style>
        .rtl {direction: rtl; text-align: right;}
        .stTextArea textarea {direction: rtl; text-align: right; font-size: 1.1em; background-color: #fdfdfd; padding: 10px; border-radius: 8px; border: 1px solid #ddd;}
        .stButton button {width: 100%; font-size: 1.2em; padding: 10px; background-color: #4CAF50; color: white; border: none; border-radius: 8px; cursor: pointer;}
        .stButton button:hover {background-color: #45a049;}
        .chat-container {background-color: #f9f9f9; padding: 15px; border-radius: 8px; border: 1px solid #ddd; margin-top: 10px;}
        .chat-response {background-color: #e8f5e9; padding: 15px; border-radius: 8px; font-size: 1.1em;}
    </style>
    """, unsafe_allow_html=True)

# Main Interface
st.title('🤖 سواعد بوت')
st.markdown('<div class="rtl">مرحبا بك في سواعد بوت، نحن هنا لمساعدتك في أي استفسارات حول خدماتنا. 💼</div>', unsafe_allow_html=True)

# Chat Input
user_input = st.text_area("✍️ كيف يمكنني مساعدتك؟", key="user_input", max_chars=300, help="اكتب استفسارك هنا")

# Submit button
if st.button('إرسال'):
    with st.spinner('جاري معالجة استفسارك...'):
        chatbot_reply = chatbot_response(user_input)
        
        # Display response
        st.markdown('<div class="rtl stTextInput">✅ تم الرد:</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="rtl chat-response">{chatbot_reply}</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <hr>
    <div style="text-align: center; font-size: 0.9em; color: #888;">
        جميع الحقوق محفوظة © 2024 سواعد.
    </div>
    """, unsafe_allow_html=True)
