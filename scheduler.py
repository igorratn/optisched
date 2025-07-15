import pandas as pd
import random

def schedule_sessions(tutors_df, students_df):
    schedule = []

    for _, student in students_df.iterrows():
        student_subject = student["Subject"]
        preferred = student["Preferred Slots"]

        # Filter tutors by subject match
        matching_tutors = tutors_df[tutors_df["Subject"].str.lower() == student_subject.lower()]
        
        if matching_tutors.empty:
            assigned = {"Student": student["Name"], "Subject": student_subject,
                        "Tutor": "❌ No match", "Scheduled Time": "—"}
        else:
            tutor = matching_tutors.sample(n=1).iloc[0]
            assigned = {
                "Student": student["Name"],
                "Subject": student_subject,
                "Tutor": tutor["Name"],
                "Scheduled Time": preferred
            }

        schedule.append(assigned)

    return pd.DataFrame(schedule)