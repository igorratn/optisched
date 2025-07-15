# 📅 OptiSched — Smart Weekly Scheduling Assistant

**OptiSched** is a lightweight web app for generating optimized weekly schedules between staff (like tutors or service providers) and clients (like students or appointments).

Built with Python, Streamlit, and basic matching logic — ideal for small businesses that manually manage bookings and want quick automation.

---

## 🔧 Features

- 📤 Upload staff availability (CSV)
- 📤 Upload client requests (CSV)
- 🔁 Auto-match based on subject
- 🧠 Expandable to smart scheduling (with PuLP)
- 📥 Download final schedule as CSV

---

## 🚀 Live Demo

👉 [Click here to try it now](https://igorratn-optisched.streamlit.app)  
_(Live app hosted via Streamlit Cloud)_

---

## 📁 Sample CSV Templates

### 🧑‍🏫 Tutors — `staff.csv`
```csv
Name,Subject,Available Slots
Alice,Math,Mon 10am;Tue 1pm;Thu 11am
Bob,English,Mon 9am;Wed 3pm;Fri 10am
Carol,Math,Tue 2pm;Thu 11am;Fri 9am
David,Science,Mon 1pm;Wed 2pm;Fri 11am
Eva,English,Tue 10am;Thu 1pm;Fri 2pm
```

### 👩‍🎓 Clients — `client.csv`
```csv
Name,Subject,Preferred Slots
Tom,Math,Mon 10am
Jill,English,Wed 3pm
Sam,Math,Tue 2pm
Nina,Science,Fri 11am
Omar,English,Fri 2pm
Lily,Math,Fri 9am
Zoe,Science,Wed 2pm
Eric,English,Mon 9am
Ben,Math,Tue 1pm
Kate,English,Tue 10am
```

---

## 🛠 Tech Stack

- Python 3
- Streamlit
- Pandas
- PuLP (optional, for optimization)

---

## 📦 Installation (for developers)

```bash
git clone https://github.com/igorratn/optisched.git
cd optisched
pip install -r requirements.txt
streamlit run app.py
```

---

## 📄 License

MIT — see `LICENSE` file.

---

## 👋 About the Author

Built by **Igor Ratnere**  
📧 [igorratn@yahoo.com](mailto:igorratn@yahoo.com)