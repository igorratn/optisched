import pandas as pd
from scheduler import schedule_sessions

def test_schedule_all_students_matched():
    staff_data = pd.DataFrame({
        "Name": ["Alice", "Bob", "Carol", "David", "Eva"],
        "Subject": ["Math", "English", "Math", "Science", "English"],
        "Available Slots": [
            "Mon 10am;Tue 1pm;Thu 11am",
            "Mon 9am;Wed 3pm;Fri 10am",
            "Tue 2pm;Thu 11am;Fri 9am",
            "Mon 1pm;Wed 2pm;Fri 11am",
            "Tue 10am;Thu 1pm;Fri 2pm"
        ]
    })
    student_data = pd.DataFrame({
        "Name": ["Tom", "Jill", "Sam", "Nina", "Omar"],
        "Subject": ["Math", "English", "Math", "Science", "English"],
        "Preferred Slots": ["Mon 10am", "Wed 3pm", "Tue 2pm", "Fri 11am", "Fri 2pm"]
    })
    result = schedule_sessions(staff_data, student_data)

    # Every student matched
    assert set(result["Student"]) == set(student_data["Name"])
    assert all(result["Tutor"] != "❌ No match")

def test_schedule_unmatched_student():
    staff_data = pd.DataFrame({
        "Name": ["Alice"],
        "Subject": ["Math"],
        "Available Slots": ["Mon 10am"]
    })
    student_data = pd.DataFrame({
        "Name": ["Tom", "Unmatchable"],
        "Subject": ["Math", "Physics"],  # Physics has no matching tutor
        "Preferred Slots": ["Mon 10am", "Thu 3pm"]
    })
    result = schedule_sessions(staff_data, student_data)

    assert "Tom" in result["Student"].values
    assert "Unmatchable" in result["Student"].values

    row_tom = result[result["Student"] == "Tom"].iloc[0]
    row_unmatch = result[result["Student"] == "Unmatchable"].iloc[0]

    assert row_tom["Tutor"] != "❌ No match"
    assert row_unmatch["Tutor"] == "❌ No match"
    assert row_unmatch["Scheduled Time"] == "—"

def test_duplicate_slots_not_assigned():
    staff_data = pd.DataFrame({
        "Name": ["Alice"],
        "Subject": ["Math"],
        "Available Slots": ["Mon 10am"]
    })
    student_data = pd.DataFrame({
        "Name": ["Tom", "Jill"],
        "Subject": ["Math", "Math"],
        "Preferred Slots": ["Mon 10am", "Mon 10am"]
    })
    result = schedule_sessions(staff_data, student_data)

    # Only one student should get Alice at Mon 10am
    matched = result[result["Tutor"] != "❌ No match"]
    assert len(matched) == 1
    assert matched.iloc[0]["Tutor"] == "Alice"
    assert matched.iloc[0]["Scheduled Time"] == "Mon 10am"

def test_case_sensitivity():
    staff_data = pd.DataFrame({
        "Name": ["Alice"],
        "Subject": ["Math"],  # Uppercase
        "Available Slots": ["Mon 10am"]
    })
    student_data = pd.DataFrame({
        "Name": ["Tom"],
        "Subject": ["math"],  # Lowercase
        "Preferred Slots": ["Mon 10am"]
    })
    result = schedule_sessions(staff_data, student_data)

    matched = result[result["Student"] == "Tom"]
    assert not matched.empty
    assert matched.iloc[0]["Tutor"] == "Alice"
