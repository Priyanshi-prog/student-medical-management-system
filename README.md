"# student-medical-management-system"  

**INTRODUCTION**
THIS PROJECT IS MADE IN ORDER TO EASE THE WORK OF
DOCTOR, NURSE AND TEACHERS TO KEEP A RECORD OF
THE STUDENT MEDICAL DETAILS AND MEDICINE STOCK.

**DOCTOR:**
DOCTOR CAN ENTER STUDENT DETAILS, MEDICINE
STOCK DETAILS, STUDENT ASSESSMENT, UPDATE AND
VIEW THESE DETAILS.

**NURSE:**
NURSE CAN ENTER STUDENT DETAILS, MEDICINE STOCK
DETAILS, STUDENT ASSESSMENT, UPDATE AND VIEW
THESE DETAILS.

**TEACHER:**
TEACHER CAN ENTER STUDENT DETAILS, MEDICINE
STOCK DETAILS, STUDENT ASSESSMENT, UPDATE AND
VIEW THESE DETAILS.

**DATABASE DESIGN:**

### Tables
| Table Name              | Description                                               |
|------------------------|-----------------------------------------------------------|
| **user_info**          | Stores usernames, passwords, and roles (Doctor/Nurse/Teacher) |
| **student_registration** | Contains student personal and health data              |
| **studassess**         | Tracks assessments, treatments, issued medicines          |
| **stock**              | Manages medicine inventory (batch no, total, issued, remaining) |


## Installation & Setup
1. Clone the repo  
2. Run `medical_management_schema.sql` to create tables  
3. Configure your database connection  
4. Launch the application…

## Usage
- Log in as a doctor, nurse, or teacher  
- Perform CRUD actions on students, assessments, and stock

## 🔧 Contributing
Feel free to submit issues or pull requests!

## License
[MIT](LICENSE)



