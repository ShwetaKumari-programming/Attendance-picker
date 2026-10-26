import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabasee

import time

@st.dialog("Capture or upload photos")
def add_photos_dialog():
    st.write('Add classroom photos to scan for attendance')
    if 'photo_tab' not in st.session_state:
        st.session_state['photo_tab'] = 'camera'

    t1, t2 = st.columns(2)
    with t1:
        type_camera = "prm"