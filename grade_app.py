import streamlit as st


# Grade calculation
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


# Store students in session state
if "students" not in st.session_state:
    st.session_state.students = []


# Page title
st.title("Student Grade Manager")


# Add student form
with st.form("add"):
    name = st.text_input("Name")
    mark = st.number_input(
        "Mark",
        min_value=0,
        max_value=100,
        step=1
    )

    submitted = st.form_submit_button("Add")


# Add student
if submitted:
    if name.strip():
        grade = get_grade(mark)

        st.session_state.students.append({
            "Name": name,
            "Mark": mark,
            "Grade": grade
        })

        st.success(f"{name} added successfully!")
    else:
        st.warning("Please enter a student name.")


# Display students and class statistics
if st.session_state.students:

    # Student table
    st.subheader("Students")
    st.table(st.session_state.students)

    # Get marks
    marks = [student["Mark"] for student in st.session_state.students]

    # Class statistics
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Display metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("Class Average", f"{average:.1f}")
    col2.metric("Highest", highest)
    col3.metric("Lowest", lowest)