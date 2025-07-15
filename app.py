import streamlit as st
import pandas as pd
from scheduler import schedule_sessions

st.set_page_config(page_title="OptiSched", layout="wide")

st.title("🗓 OptiSched — Weekly Scheduling Assistant")
st.markdown("""
Upload your tutor availability and student session requests.
The app will generate an optimized weekly schedule that you can review and download.
""")

st.subheader("1. Upload Tutor Availability")
staff_file = st.file_uploader("Upload a CSV with tutor info", type="csv")

st.subheader("2. Upload Student Requests")
client_file = st.file_uploader("Upload a CSV with student requests", type="csv")

if staff_file and client_file:
    staff_df = pd.read_csv(staff_file)
    client_df = pd.read_csv(client_file)

    if st.button("🧠 Generate Schedule"):
        result_df = schedule_sessions(staff_df, client_df)
        st.success("Schedule generated below! ✅")
        st.write("### 📋 Optimized Weekly Schedule")
        st.dataframe(result_df)

        st.download_button("⬇️ Download Schedule", result_df.to_csv(index=False), "schedule.csv", "text/csv")

st.markdown("---")
st.markdown("Built by Igor Ratnere — [Contact](mailto:igorratn@yahoo.com)")