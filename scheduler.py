import pandas as pd

def schedule_sessions(tutors_df, students_df):
    schedule = []
    used_slots = set()  # Tracks (Tutor, Slot) pairs to avoid double-booking tutors

    for _, student in students_df.iterrows():
        student_subject = student["Subject"].strip().lower()
        preferred = student["Preferred Slots"].strip()

        assigned = {
            "Student": student["Name"],
            "Subject": student["Subject"],
            "Tutor": "❌ No match",
            "Scheduled Time": "—"
        }

        # Filter tutors by subject match (case-insensitive)
        matching_tutors = tutors_df[
            tutors_df["Subject"].str.strip().str.lower() == student_subject
        ]

        for _, tutor in matching_tutors.iterrows():
            available_slots = [s.strip() for s in tutor["Available Slots"].split(";")]
            if preferred in available_slots:
                slot_key = (tutor["Name"], preferred)
                if slot_key not in used_slots:
                    used_slots.add(slot_key)
                    assigned = {
                        "Student": student["Name"],
                        "Subject": student["Subject"],
                        "Tutor": tutor["Name"],
                        "Scheduled Time": preferred
                    }
                    break  # stop after assigning one slot

        schedule.append(assigned)

    return pd.DataFrame(schedule)
