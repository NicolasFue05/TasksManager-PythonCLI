import streamlit as st
from db import Base, engine
from tasks import addTask, listTasks


Base.metadata.create_all(engine)

# streamlit app
st.title("Tasks Manager")
addTask()
listTasks()
