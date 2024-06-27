# NextCorp MVP (MVP Complete)

### Your All-in-One Small Corporation Manager

(AUTHORS)

SOFIANE SADGALI 
CLEVELAND 
OLATUNJI OLUWADARE [tunjidare2@gmail.com] 

---

## Progress Overview

### Weekly Progress Rating
**Rating:** 7.75

**Basis:** Tasks completed (according to Trello Board) and implemented features.

### Progress Assessment
This week, we made significant strides, achieving almost all our planned tasks. The major time-consuming task was connecting the backend with the frontend for data visualization.

### Completed Project Components
- **Database Storage**: Robust and scalable storage solution.
- **Full API Integration**: Comprehensive API for seamless interactions.
- **Dashboard Integration**: Centralized control panel.
- **Dashboard CRUD Functionality**: Complete Create, Read, Update, Delete operations.
- **User Interface (UI)**: Intuitive and user-friendly interface.
- **Data Visualization on Dashboard**: Clear and actionable insights.
- **Data Visualization on Frontend**: Engaging and informative visuals.
- **Multiple Authentication Systems**: Secure access management.
- **Registration for Corporations**: Easy and efficient onboarding.
- **Password Reset Functionality**: Secure and user-friendly password management.
- **Employee Profile Manager**: Comprehensive profile management system.
- **Automatic Checker System**: Real-time user activity tracking using a timer.

### Incomplete Project Components
- **History Data Visuals**: Detailed logs of checks performed by each employee.
- **Dashboard CRUD for Employee Checkers**: Display and management of employee check-ins and check-outs from the dashboard.

---

## Challenges Faced

### Technical Challenges

**Most Difficult Technical Challenge:**

**Automated Checker System Development**

**Description:**

Creating a robust automated checker system that triggers based on user login/logout and a timer threshold was our biggest challenge. We invested substantial effort to ensure it operated seamlessly and without bugs.

**System Workflow:**

1. **Login Handling**: Upon user login, the system captures the user ID (employee_id) and stores it in a session.
2. **Check-in Verification**: The system checks for an existing check-in record within a predefined time limit.
   - If a record exists within the time limit, it is retrieved.
      - Otherwise, a new record is created with a "NULL" checkout.
      3. **Logout Handling**: The checkout process is triggered during user logout, updating the record.
      4. **Synchronization**: Maintaining synchronization between check-in and checkout was crucial. The check-in is updated only during login, and the checkout is updated during logout, ensuring accurate activity logs.

      ### Non-Technical Challenges

      **Most Difficult Non-Technical Challenge:**

      **Managing Workload and Meeting Deadlines**

      **Description:**

      We faced significant pressure from the volume of work required within a tight deadline. Prioritizing tasks effectively was essential to ensure progress and meet our goals.

      **Strategies Employed:**

      1. **Disciplined Time Management**: Breaking down the project into smaller tasks with clear milestones.
      2. **Focused Work Environment**: Minimizing distractions and setting specific work hours for high-priority tasks.
      3. **Productivity Tools**: Utilizing tools to track tasks, deadlines, and progress.
      4. **Stress Management**: Taking short breaks and maintaining a positive mindset to stay motivated.

      Our structured approach and commitment helped us navigate these challenges and achieve substantial progress toward completing the core components of the project on time.

      ---

      By following a disciplined and focused approach, we successfully managed to overcome both technical and non-technical challenges, bringing us closer to delivering a robust and comprehensive MVP for NextCorp.
