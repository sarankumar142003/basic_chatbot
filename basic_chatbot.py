from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit  as st

#lode the env variable
load_dotenv()

#Streamlit page setup
st.set_page_config(
    page_title="CHATBOT",
    page_icon="🤖",
    layout="centered"
)
st.title("GEN AI CHATBOT")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"]=[]

#show chat history

for message in st.session_state["chat_history"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#LLM
llm=ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.1
)
#input box
user_prompt=st.chat_input("Ask chatbot")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user","content":user_prompt})

    response = llm.invoke(
        input= [{"role":"system","content":"you are a helpful assistant"},*st.session_state.chat_history]
    )
    assistant_response =response.content
    st.session_state.chat_history.append({"role":"assistant","content":assistant_response})
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

