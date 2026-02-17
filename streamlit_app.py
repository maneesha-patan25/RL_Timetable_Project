import streamlit as st
import pandas as pd
from timetable_env import TimetableEnv

st.title("Smart RL Timetable Generator")

st.subheader("Enter Constraints")

rooms = st.number_input("Number of Rooms",min_value=1,value=3)
teachers = st.number_input("Number of Teachers",min_value=1,value=3)
subjects_input = st.text_input("Enter Subjects (comma separated)")

if st.button("Generate Timetable"):

    subjects = [s.strip() for s in subjects_input.split(",") if s.strip()!=""]

    teacher_list = [f"T{i+1}" for i in range(teachers)]
    room_list = [f"R{i+1}" for i in range(rooms)]

    env = TimetableEnv(subjects,teacher_list,room_list)
    timetable = env.generate_timetable()

    df = pd.DataFrame(timetable,
        index=["Monday","Tuesday","Wednesday","Thursday","Friday"],
        columns=["9-10","10-11","11-12","12-1","2-3","3-4"]
    )

    st.subheader("AI Generated Timetable")
    st.table(df)
