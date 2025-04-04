import streamlit as st
# import google.generativeai as genai
# api_key = st.secrets["GENAI_API_KEY"]
# genai.configure(api_key=api_key)
counter=1
st.set_page_config(page_title="Gemini Chatbot", layout="centered")
st.title("🤖 Gemini Chatbot")
st.write("Ask me anything based on the given data. If I don't know the answer, I'll reply with 'Not known'.")

text="""FARHAN SIDDIQUE Dept: Electronics & Communication Engineering 
    Year of Graduation: 2019 Degree: B-TechCollege: Durgapur Institute of Advanced Technology & Management
    .E-Mail:farhansiddique027@gmail.com Phone No:09064654440(M)/8927141595 OBJECTIVE:Seeking a position in well renowned sector
    in well renowned sector where I can utilize my skills & abilities achieve professional growth while being innovative and 
    flexible exploring my internal smartness VISION: My vision is to earn success from this lovely world and thereby to establish
    myself as an honest and ideal perso. Strength: My strength is positive attitude and self-confidence. HOBBIES Playing Cricket. 
    TECHNICAL EXPOSURE: LANGUAGE:–Basics of CORE JAVA,PYTHON. PROFICIENT IN COMPUTER OPERATING,
    INTERNET SURFING, MS OFFICE, MS WORD , MS EXCEL ETC. Sem-1 6.89 Sem-2 6.00"""
while counter!=0:
    user_prompt = st.text_input("💬 You:", "")
    if user_prompt=="exit" :
        break
    
    # prompt=f""" user asked "{user_prompt}", you have this data"{text}",
    # Respond to the user based on the data. If the query is out of context, reply with 'Not known'."""

    # response = genai.generate_content(
    # model="gemini-2.0-flash", contents=[{"role": "user", "parts": [{"text": prompt}]}]
    #)
   
    # st.markdown(f"**🤖 Gemini:** {response.text}")

# Exit button
if st.button("🚪 Exit Chat"):
    st.stop()
