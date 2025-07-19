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

        # --- Share section ---
        st.markdown("---")
        st.markdown("### 📣 Help Others Find This Tool")
        st.markdown("If this saved you time, share it with a colleague:")

        st.code("https://optisched.streamlit.app", language="markdown")

        st.markdown(
            '[🐦 Tweet This](https://twitter.com/intent/tweet?text=Check+out+this+free+tool+for+tutoring+schedules:+https://optisched.streamlit.app)',
            unsafe_allow_html=True,
        )
        st.markdown(
            '[📧 Email a Friend](mailto:?subject=Check%20out%20OptiSched&body=Try%20this%20free%20tool%20for%20tutoring%20scheduling:%20https://optisched.streamlit.app)',
            unsafe_allow_html=True,
        )

with st.expander("❓ Help — How to Use OptiSched"):
    st.markdown("""
### 📁 What files should I upload?

#### 🧑‍🏫 Tutor Availability (CSV)
This file should contain:
- `Name` — Tutor name
- `Subject` — Subject or topic they can teach
- `Available Slots` — Semicolon-separated list of times available (e.g., `"Mon 10am;Tue 1pm"`)

**Example:**

| Name  | Subject  | Available Slots              |
|-------|----------|------------------------------|
| Alice | Math     | Mon 10am;Tue 1pm;Thu 11am     |
| Bob   | English  | Mon 9am;Wed 3pm;Fri 10am      |
""")

    with open("sample_data/staff.csv", "rb") as f:
        st.download_button("📥 Download Example Tutor CSV", f, file_name="tutor.csv")

    st.markdown("""
---

#### 🎓 Student Requests (CSV)
This file should contain:
- `Name` — Student name
- `Subject` — Subject requested
- `Preferred Slots` — Preferred time (only one per request for now)

**Example:**

| Name  | Subject  | Preferred Slots |
|-------|----------|------------------|
| Tom   | Math     | Mon 10am         |
| Jill  | English  | Wed 3pm          |
""")

    with open("sample_data/client.csv", "rb") as f:
        st.download_button("📥 Download Example Student CSV", f, file_name="student.csv")

    st.markdown("""
---

### 🧠 How does scheduling work?

After uploading both files, click **"Generate Schedule"**.

The system will:
- Match students to tutors based on subject
- Match times when both are available
- Generate a weekly schedule

---

### 💾 Can I download the results?

Yes! After the schedule is displayed, click the **"⬇️ Download Schedule"** button to save it as a CSV file.

---

If you have any questions, feel free to reach out using the contact link below.
""")

st.markdown("---")
st.markdown("Built by Igor Ratneré — [Contact](mailto:igorratn@yahoo.com)")