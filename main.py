import streamlit as st
import fitz  # PyMuPDF
from huggingface_hub import InferenceClient
import time
from google import genai
import os, dotenv


# CSS for RTL
# st.markdown(
#     """
#     <style>
#     body {
#         direction: rtl;
#         text-align: right;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

st.title("PDF Translator")
uploaded_file = st.file_uploader("Upload your pdf file:", type="pdf")
bt = st.button("Translate")
if bt and uploaded_file:
    pdf_doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page_num in range(len(pdf_doc)):
        page = pdf_doc[page_num]
        page_text = page.get_text("text")
        client = InferenceClient(
            model="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
            api_key="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",
        )
        msg = [
            {"role": "system", "content": "translate all texts into fluent persian"},
            {"role": "user", "content": page_text},
        ]
        completion = client.chat.completions.create(messages=msg)
        st.markdown(completion.choices[0].message.content)
        time.sleep(2)
