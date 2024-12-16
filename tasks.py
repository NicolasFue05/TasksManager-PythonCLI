import streamlit as st
from db import session
from models import Task

def addTask():
    st.write("""
        ## Add new Task
    """)
    task_title = st.text_input("Task Title", key="task_title")
    task_description = st.text_input("Task Description", key="task_description")
    task_priority = st.selectbox("Task Priority:", ["Low", "Urgent"], key="task_priority")

    if st.button("Add"):
        if task_title.strip() and task_description.strip():
            task = Task(title=task_title, description=task_description, priority=task_priority, status="Pending")
            session.add(task)
            session.commit()
            st.success(f"Task added successfully: {task_title}")
        else: 
            st.error("Task title or description cannot be empty")

def listTasks():
    st.write("""
        ## Tasks
    """)
    tasks = session.query(Task).all()
    if tasks:
        for task in tasks:
            st.write(f"### Title: {task.title}")
            st.write(f"Description: ***{task.description}***")
            st.write(f"Priority: {task.priority}")
            st.write(f"Status: {task.status}")
            st.write("-----------------------------------------")
        else:
            st.info("No tasks found")

