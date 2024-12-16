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
            st.experimental_rerun()  # Recargar la página para ver la tarea añadida
        else: 
            st.error("Task title or description cannot be empty")

def updateTask(task):
    # Actualizar el título, descripción y prioridad de una tarea
    new_task_title = st.text_input("Update Task Title", value=task.title)
    new_task_description = st.text_input("Update Task Description", value=task.description)
    new_task_priority = st.selectbox("Update Task Priority:", ["Low", "Urgent"], index=["Low", "Urgent"].index(task.priority))

    if st.button("Update"):
        if new_task_title.strip() and new_task_description.strip():
            # Modificar las propiedades del objeto
            task.title = new_task_title
            task.description = new_task_description
            task.priority = new_task_priority

            # Hacer commit para guardar los cambios
            session.commit()
            st.session_state.task.title = new_task_title
            st.success(f"Task updated successfully: {task.title}")
            st.experimental_rerun()  # Recargar la página para ver la tarea actualizada
        else:
            st.error("Task title or description cannot be empty")

def deleteTask(task):
    if st.button(f"Delete Task '{task.title}'"):
        # Eliminar la tarea de la base de datos
        session.delete(task)
        session.commit()
        st.success(f"Task '{task.title}' deleted successfully")
        st.session()
        st.experimental_rerun()  # Recargar la página para ver que la tarea se ha eliminado

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
            
            # Botones para actualizar y eliminar tareas
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Update {task.title}", key=f"update_{task.id}"):
                    updateTask(task)
            with col2:
                if st.button(f"Delete {task.title}", key=f"delete_{task.id}"):
                    deleteTask(task)
            st.write("-----------------------------------------")
    else:
        st.info("No tasks found")

