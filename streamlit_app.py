import streamlit as st
import fitz  # PyMuPDF
import time
from google import genai
import os, dotenv

st.set_page_config(page_title="مترجم هوش مصنوعی")
# CSS for RTL
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&display=swap');
    body {
        direction: rtl;
        text-align: right;
        font-family: "Vazirmatn", serif;
        font-optical-sizing: auto;
        font-weight: 300;
        font-style: normal;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("مترجم هوشمند")
st.subheader("با این ابزار می توانید فایل PDF خود را به سه زبان ترجمه کنید.")
uploaded_file = st.file_uploader("فایل PDF خود را آپلود کنید:", type="pdf")
lang = st.radio(
    "می خواهید به چه زبانی ترجمه شود؟",
    ["Persian", "Arabi", "English"],
)
bt = st.button("ترجمه کن")
dotenv.load_dotenv()
api_key = os.getenv("GEMAI_API_KEY")
client = genai.Client(api_key=api_key)
sys_instruction = f"translate all texts into fluent {lang} and just give me the test without explanation. if face formula, format it as a latex formula."
if bt and uploaded_file:
    pdf_doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    with st.spinner("شکیبا باشید...", show_time=True):
        for page_num in range(len(pdf_doc)):
            page = pdf_doc[page_num]
            page_text = page.get_text("text")
            response = client.models.generate_content(
                model="gemini-2.0-pro-exp-02-05",
                config=genai.types.GenerateContentConfig(
                    system_instruction=sys_instruction
                ),
                contents=[page_text],
            )
            st.markdown(response.text)
            time.sleep(1)
        st.success("ترجمه انجام شد.")
        st.button("ترجمه خوب نیست؟ مجدد اجرا کنید.")
