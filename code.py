from google import genai
import PyPDF2
import streamlit as st
api_key = st.secrets["GENAI_API_KEY"]
client=genai.Client(api_key=api_key)
counter=1
text=""" """
st.set_page_config(page_title="Pdf based Chatbot", layout="centered")
st.title("Pdf based Chatbot")
st.write("Ask me anything based on the given pdf.")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Check if a file is uploaded
if uploaded_file is not None:
    # Read the PDF content
    reader = PyPDF2.PdfReader(uploaded_file)
    st.success("PDF Uploaded Successfully!")
    for page in reader.pages:
        texxt = page.extract_text()
        if texxt:
            text += texxt + "\n"

    st.success("Text extracted and stored in 'doc' variable ✅")
if 'clicked' not in st.session_state:
    st.session_state.clicked = False
def click_button():
    st.session_state.clicked=True
user_prompt = st.text_input("Ask:", "")
st.button('Generate Text', on_click=click_button)
def generate_t(user_prompt):
    prompt=f""" user asked "{user_prompt}", you have this data"{text}",
    Respond to the user based on the data. If the query is out of context, reply with 'I don't have any information about this context.'.
    If user ask any generic question reply it.
    """

    response=client.models.generate_content(
    model="gemini-2.0-flash", contents=[{"role": "user", "parts": [{"text": prompt}]}])
   
    st.markdown(f"**Gemini:** {response.text}")
    
if st.session_state.clicked:
    # The message and nested widget will remain on the page
    generate_t(user_prompt)

# while counter!=0:
#     user_prompt = st.text_input("💬 You:", "")
#     if user_prompt=="exit" :
#         counter=0
#         break
#     generate_t(user_prompt)
    
    

# Exit button
