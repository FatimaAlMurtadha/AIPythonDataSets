# Second DataSet: student_performance_grade:

### Dataset count
- 8000 rows and 18 columns

### Numerical Features (['Age', 'Hours_Studied', 'Attendance', 'Sleep_Hours', 'Stress_Level','Screen_Time', 'Previous_GPA', 'Tutoring_Sessions_Per_Week','Exam_Anxiety_Score'])

- classification

### Categorical Features (['Student_ID', 'Gender', 'Part_Time_Job', 'Study_Method', 'Diet_Quality','Internet_Quality', 'Extracurricular', 'Family_Income_Level', 'Grade'])


### No missing Values
### No duplicates
### Data Types are correct


### Insight
- Hours_Studied: 
    1. mean -> 5 hours
    2. max  -> 12

- Stress_Level:
    1. mean  -> 5
    2. range ( 1 : 10)

- Exam_Anxiety_Score:
    1. mean -> 3.0
    2. range ( 1 : 10) 

- Previous_GPA: 
    1. mean -> 3.0
    2. max  -> 6.7


## Columns that would effect Grade
    1. Positive Correlation:
        - Hours_Studied
        - Attendance
        - Previous_GPA
    2. Negative Correlation
        - Stress_Level
        - Screen_Time
        - Exam_Anxiety_Score

# 1. Numerical Columns: 
['Age', 'Hours_Studied', 'Attendance', 'Sleep_Hours', 'Stress_Level',
       'Screen_Time', 'Previous_GPA', 'Tutoring_Sessions_Per_Week',
       'Exam_Anxiety_Score', 'Final_Score'] ( 8000 rows × 10 columns)

    - 1. more (Hours_Studied) => Grade -> Strong positive
    - 2. more (exam anxiety) less performance (Grade) -> Strong negative
    - 3. more (Tutoring Sessions Per Week) more (Grade) -> Correlation != causation -> we can't prove the reason directly.
    - 4. more (Stress Level) less (Grade) -> negative correlation 
    - 5. Who has a previous Good performance ability Would mostly still be good.
    - 6. (Screen Time) can cause a less grade -> Weak negative correlation
    - 7. Age -> No correlation