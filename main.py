import streamlit as st
from db import Base, engine
from tasks import addTask, listTasks, updateTask, deleteTask


Base.metadata.create_all(engine)

# streamlit app
st.title("Tasks Manager")
addTask()
listTasks()
