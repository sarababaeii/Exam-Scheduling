# Exam Scheduling

This project designs and develops an Integer Programming (IP) model for scheduling midterm exams across departmental courses.
The goal is to assign an exam date to each course while minimizing schedule compression for students, that is, avoiding multiple exams on the same day and reducing cases where students have exams on consecutive days.

The model uses real enrollment data to determine which students are registered in which courses, ensuring that exams are scheduled to minimize conflicts and clustering.
It automatically structures the model’s input by crawling and processing real data from 57 courses and 580 students in the department for a given semester and produces feasible exam timetables that minimize student exam load compression.

The project also compares results obtained under different computation time limits and objective function parameters to analyze the trade-off between optimality and computation time.
