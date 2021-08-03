# Anomaly Detection Project
## By Desiree McElroy and Xavier Carter

-------------

**Questions asked of us to find for the meeting on Thursday are as followed:**
- Which lesson appears to attract the most traffic consistently across cohorts (per program)?
- Which lessons are least accessed?
- Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
- What topics are grads continuing to access after graduation?
at some point in 2019 the ability for students to access both curriculums was deprecated, do you see evidence of that happening, did it happen before?
- Is there a cohort that referred to a lesson significantly more that other cohorts seemed to gloss over?

## Data Dictionary
Name | Description | Type
:---: | :---: | :---:
date | The data of the log-on | date
endpoint | The endpoint url visited | object
user_id | The id assigned to that specific user | int
cohort_id | The id assigned to the specific cohort | int
source_ip | The original ip address | object
name | The cohort name | object
start_date | The start date of the cohort | date
end_date | The end date of the cohort | date
created_at | The date the user id was created | date
updated_at | The date the data was pulled | object
program_id | The program id for the cohort | object
program_name | The name of the program for that cohort | object
-------
## Findings:
![anomaly_detection_summary](https://user-images.githubusercontent.com/69991789/128052040-9f56c667-a5bd-4bc5-9707-73208e866076.png)