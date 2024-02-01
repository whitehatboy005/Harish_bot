import streamlit as st
import google.generativeai as genai


genai.configure(api_key=st.secrets["gemini_api"])
def ai(txt):
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Harish created this AI "+txt)
    return response.text

st.title("Welcome to Harish AI")

command = st.chat_input("how can I help you?")

if "message" not in st.session_state:
    st.session_state.message = []

for chat in st.session_state.message:
    with st.chat_message(chat["role"]):
        st.write(chat["message"])


if command:
    with st.chat_message("USER"):
        st.write(command)
        st.session_state.message.append({"role":"USER","message":command})
    if "hello" in command:
        with st.chat_message("BOT"):
            st.write("Hi How are you?")
            st.session_state.message.append({"role":"BOT","message":"Hi How are you?"})
    elif "Hello" in command:
        with st.chat_message("BOT"):
            st.write("Hi,How are you?")
            st.session_state.message.append({"role":"BOT","message":"Hi,How are you?"})

    elif "who are you" in command:
        with st.chat_message("BOT"):
            st.write("I am Harish AI Assistant")
            st.session_state.message.append({"role":"BOT","message":"I am Harish AI Assistant"})
    elif "Who are you" in command:
        with st.chat_message("BOT"):
            st.write("I am Harish AI Assistant")
            st.session_state.message.append({"role":"BOT","message":"I am Harish AI Assistant"})
    
    elif "fine" in command:
        with st.chat_message("BOT"):
            st.write("Good")
            st.session_state.message.append({"role":"BOT","message":"Good"})
    elif "Fine" in command:
        with st.chat_message("BOT"):
            st.write("Good")
            st.session_state.message.append({"role":"BOT","message":"Good"})
    
    elif "karthi" in command:
        with st.chat_message("BOT"):
            st.write("Hello Karthi bro I know you are Harish friend and Harish says you are another name is KK. How are you KK?")
            st.session_state.message.append({"role":"BOT","message":"Hello Karthi bro I know you are Harish friend and Harish says you are another name is KK. How are you KK?"})
    elif "Karthi" in command:
        with st.chat_message("BOT"):
            st.write("Hello Karthi bro I know you are Harish friend and Harish says you are another name is KK. How are you KK?")
            st.session_state.message.append({"role":"BOT","message":"Hello Karthi bro I know you are Harish friend and Harish says you are another name is KK. How are you KK?"})

    elif "Farith" in command:
        with st.chat_message("BOT"):
            st.write("Hello Farith bro I know you are Harish friend. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Farith bro I know you are Harish friend. How are you friend?"})
    elif "farith" in command:
        with st.chat_message("BOT"):
            st.write("Hello Farith bro I know you are Harish friend. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Farith bro I know you are Harish friend. How are you friend?"})

    elif "selvarajan" in command:
        with st.chat_message("BOT"):
            st.write("Hello Selva bro I know you are Harish friend and Harish says you are loosu k*. Anywere, how are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Selva bro I know you are Harish friend and Harish says you are loosu k*. Anywere, how are you friend?"})
    elif "Selvarajan" in command:
        with st.chat_message("BOT"):
            st.write("Hello Selva bro I know you are Harish friend and my Harish says you are loosu k*. Anywere, how are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Selva bro I know you are Harish friend and Harish says you are loosu k*. Anywere, how are you friend?"})

    elif "arikaran" in command:
        with st.chat_message("BOT"):
            st.write("Hello Arikaran bro I know you are Harish friend. How are you friend")
            st.session_state.message.append({"role":"BOT","message":"Hello Arikaran bro I know you are Harish friend. How are you friend?"})
    elif "Arikaran" in command:
        with st.chat_message("BOT"):
            st.write("Hello Arikaran bro I know you are Harish friend. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Arikaran bro I know you are Harish friend. How are you friend?"})

    elif "siva" in command:
        with st.chat_message("BOT"):
            st.write("Hello Siva bro I know you are Harish friend. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Siva bro I know you are Harish friend. How are you friend?"})
    elif "Siva" in command:
        with st.chat_message("BOT"):
            st.write("Hello Siva bro I know you are Harish friend. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Siva bro I know you are Harish friend. How are you friend?"})

    elif "mohanraj" in command:
        with st.chat_message("BOT"):
            st.write("Hello Mohan bro I know you are Harish friend and your another name is CM. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Mohan bro I know you are Harish friend and your another name is CM. How are you friend?"})
    elif "Mohanraj" in command:
        with st.chat_message("BOT"):
            st.write("Hello Mohan bro I know you are Harish friend and your another name is CM. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Mohan bro I know you are Harish friend and your another name is CM. How are you friend?"})

    elif "Arun" in command:
        with st.chat_message("BOT"):
            st.write("Hello Arun bro I know you are Harish friend. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Arun bro I know you are Harish friend. How are you friend?"})
    elif "arun" in command:
        with st.chat_message("BOT"):
            st.write("Hello Arun bro I know you are Harish friend. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Arun bro I know you are Harish friend. How are you friend?"})

    elif "saranraj" in command:
        with st.chat_message("BOT"):
            st.write("Hello Saran bro I know you are Harish friend. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Saran bro I know you are Harish friend. How are you friend?"})
    elif "Saranraj" in command:
        with st.chat_message("BOT"):
            st.write("Hello Saran bro I know you are Harish friend. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Saran bro I know you are Harish friend. How are you friend?"})

    elif "manibalan" in command:
        with st.chat_message("BOT"):
            st.write("Hello Manibalan bro I know you are Harish friend. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Manibalan bro I know you are Harish friend. How are you friend?"})
    elif "Manibalan" in command:
        with st.chat_message("BOT"):
            st.write("Hello Manibalan bro I know you are Harish friend. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Manibalan bro I know you are Harish friend. How are you friend?"})

    elif "Vinoth" in command:
        with st.chat_message("BOT"):
            st.write("Hello Vinoth bro I know you are Harish friend. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Vinoth bro I know you are Harish friend. How are you friend?"})
    elif "vinoth" in command:
        with st.chat_message("BOT"):
            st.write("Hello Vinoth bro I know you are Harish friend. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Vinoth bro I know you are Harish friend. How are you friend?"})

    elif "Srikanth" in command:
        with st.chat_message("BOT"):
            st.write("Hello Srikanth bro I know you are Harish friend. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Srikanth bro I know you are Harish friend. How are you friend?"})
    elif "srikanth" in command:
        with st.chat_message("BOT"):
            st.write("Hello srikanth bro I know you are Harish friend. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Srikanth bro I know you are Harish friend. How are you friend?"})

    elif "jaghan" in command:
        with st.chat_message("BOT"):
            st.write("Hello Jaghan bro I know you are Harish friend. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Jaghan bro I know you are Harish friend. How are you friend?"})
    elif "Jaghan" in command:
        with st.chat_message("BOT"):
            st.write("Hello Jaghan bro I know you are Harish friend. How are you friend?")
            st.session_state.message.append({"role":"BOT","message":"Hello Jaghan bro I know you are Harish friend. How are you friend?"})

    else:
        with st.chat_message("BOT"):
            data = ai(command)
            st.write(data)
            st.session_state.message.append({"role":"BOT","message":data})

print(st.session_state.message)



