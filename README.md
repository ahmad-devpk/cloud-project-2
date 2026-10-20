Practice Project 2: Docker Compose + AWS EC2

Technologies

- AWS EC2 & Ubuntu Linux
- Docker & Docker Compose
- Python Flask & MySQL
- Git & GitHub

Project Overview

Built a two-container application using Docker Compose: a Flask web app and a MySQL database.

Features

- Container networking and volume persistence
- Deployed on AWS EC2
- Verified web app and MySQL connectivity in the browser


Deployment Process

1. Created the Flask application and Docker configuration files.
2. Configured the web and MySQL services using Docker Compose.
3. Deployed the application on an AWS EC2 Ubuntu instance.
4. Tested the application through a web browser.
5. Verified the connection between the web application and MySQL database.

What I Learned

- Docker containers and Docker Compose
- Container networking and volume persistence
- Flask and MySQL connectivity
- Linux command-line operations
- AWS EC2 deployment
- Git and GitHub version control


Troubleshooting

Issue: File Name Mismatch

- Problem: Docker Compose encountered an error due to a mismatch between the actual file name "requirments.txt" and the expected file name "requirements.txt".
- Investigation: Checked the file name and the configuration referencing it.
- Solution: Used the Linux "mv" command to rename the file to "requirements.txt" without changing its contents.
- Result: Docker Compose ran successfully after correcting the file name.

Learning: Learned how to troubleshoot file-name mismatches and use the Linux "mv" command to rename files.

  
Author

BSIT Cloud Computing Learner

## Deployment Proofs

1. **Git Commit & Push:**
   ![Upload Part 1](screenshots/upload%20part%201.png)

2. **AWS EC2 Instance Running:**
   ![Upload Part 2](screenshots/upload%20part%202.png)

3. **Docker Compose Deployment:**
   ![Upload Part 3](screenshots/upload%20part%203.png)

4. **Live Web Application Result:**
   ![Upload Part 4](screenshots/upload%20part%204.png)
   
