python_students = {"pranav", "jean", "anjana"}
data_science_students = {"aiswarya", "amal", "eby"}

python_students.add("seyda")

data_science_students.remove("eby")

both_courses = python_students & data_science_students
print("Students in both courses:", both_courses)

only_python = python_students - data_science_students
print("Only Python students:", only_python)

all_students = python_students | data_science_students
print("All students:", all_students)

course_counts = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}

for course, count in course_counts.items():
    print(f"Course: {course}, Students: {count}")

expected_growth = {course: count * 2 for course, count in course_counts.items()}

print("Expected growth:", expected_growth)
