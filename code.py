import google.generativeai as genai
client=genai.Client(api_key="AIzaSyBnA2N4x0pW4a6XnedNAB92PlXZRs5AFLY")
counter=1
text="""FARHAN SIDDIQUE Dept: Electronics & Communication Engineering 
    Year of Graduation: 2019 Degree: B-TechCollege: Durgapur Institute of Advanced Technology & Management
    .E-Mail:farhansiddique027@gmail.com Phone No:09064654440(M)/8927141595 OBJECTIVE:Seeking a position in well renowned sector
    in well renowned sector where I can utilize my skills & abilities achieve professional growth while being innovative and 
    flexible exploring my internal smartness VISION: My vision is to earn success from this lovely world and thereby to establish
    myself as an honest and ideal perso. Strength: My strength is positive attitude and self-confidence. HOBBIES Playing Cricket. 
    TECHNICAL EXPOSURE: LANGUAGE:–Basics of CORE JAVA,PYTHON. PROFICIENT IN COMPUTER OPERATING,
    INTERNET SURFING, MS OFFICE, MS WORD , MS EXCEL ETC. Sem-1 6.89 Sem-2 6.00"""
while counter!=0:
    user_prompt=input("You: ")
    
    if user_prompt=="exit" :
        counter=0
        break
    
    prompt=f""" user asked "{user_prompt}", you have this data"{text}",
    Respond to the user based on the data. If the query is out of context, reply with 'Not known'."""

    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=[{"role": "user", "parts": [{"text": prompt}]}]
    )
    print("Gemini:",response.text)
