import streamlit as st
import google.generativeai as generativeai
generativeai.configure(api_key=st.secrets["AIzaSyByN6qu5xoyB4asbKH-IT2VMBeA0mToHDU"])
def generativeai(txt):

    for m in generativeai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = generativeai.GenerativeModel('gemini-pro')
    response = model.generate_content("Harish AI: "+txt)
    return response.text



st.title("Harish AI Assistant")






if "message" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["message"])

message = st.chat_input("Your message")

if message:
    with st.chat_message("user"):
        st.write(message)
        st.session_state.messages.append({"role": "user", "message": message})
    if message.lower() == "hi":
        with st.chat_message("bot"):
            st.write("Hello")
            st.session_state.messages.append({"role": "bot", "message": "Hello"})
    elif message.lower() == "good morning":
        with st.chat_message("bot"):
            st.write("Good morning! Have a nice day")
            st.session_state.messages.append({"role": "bot", "message": "Good morning! Have a nice day"})
    else:
        with st.chat_message("bot"):
            data = generativeai(message)
            st.write(data)
            st.session_state.messages.append({"role": "bot", "message": data})

print(st.session_state.message)