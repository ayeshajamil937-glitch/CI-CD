# 🐳 Dockerized Three-Tier Application & CI/CD Pipeline

## 👩‍💻 Project Overview

This project focuses on learning Docker containerization, three-tier application architecture, Git/GitHub version control, and CI/CD automation using GitHub Actions.

The goal is to build, run, test, and eventually deploy a containerized application through an automated DevOps workflow.

## 🎯 Project Objectives

- Understand Docker images and containers.
- Run an Nginx web server inside a Docker container.
- Learn Docker port mapping and container management.
- Manage source code using Git and GitHub.
- Create a CI pipeline using GitHub Actions.
- Automate Docker image builds and application testing.
- Prepare for deployment on an Ubuntu server or AWS EC2.

## 🛠️ Technology Stack

- **Operating System:** Ubuntu Linux / Windows
- **Containerization:** Docker
- **Web Server:** Nginx
- **Version Control:** Git
- **Code Hosting:** GitHub
- **CI/CD:** GitHub Actions
- **Container Orchestration:** Docker Compose (project development)
- **Future Cloud Deployment:** AWS EC2

## 🏗️ Application Architecture

```text
Developer
   |
   v
Git Repository
   |
   v
GitHub Repository
   |
   v
GitHub Actions
   |
   v
Build Docker Image
   |
   v
Run Container & Test HTTP
   |
   v
Successful CI Pipeline
```

## ✅ Completed Work

### 1. Docker Container

- Docker container created using the Nginx Alpine image.
- Container name: `my-docker-app`
- Host port: `3000`
- Container port: `80`
- Application URL: http://localhost:3000
- Container status: Running (when verified locally).

### 2. Docker Commands Practiced

- `docker ps`
- `docker images`
- `docker pull`
- `docker run`
- `docker logs`
- `docker exec`
- `docker build`

### 3. Git and GitHub

- Created and managed a Git repository.
- Practiced adding, committing, pulling, and pushing changes.
- Worked on synchronizing local and remote branches.
- Practiced resolving a README merge conflict.

### 4. CI/CD Learning

- Created a GitHub Actions workflow.
- Automated Docker image building.
- Added an HTTP health/smoke test for the web application.
- Configured automatic workflow execution on pushes to the `main` branch.

**Note:** CI pipeline success should be confirmed in the GitHub Actions tab.

## 🚧 Work in Progress / Future Enhancements

- [ ] Configure a complete frontend using Nginx.
- [ ] Develop a backend API using Node.js or Flask.
- [ ] Integrate a MySQL or PostgreSQL database.
- [ ] Complete the three-tier application.
- [ ] Publish Docker images to Docker Hub or GitHub Container Registry.
- [ ] Configure automated deployment to an Ubuntu VM or AWS EC2.
- [ ] Add HTTPS/SSL.
- [ ] Implement application monitoring and logging.

## 📂 Project Structure

```text
docker-3-tier-app/
├── frontend/
├── backend/
├── database/
├── .github/
│   └── workflows/
│       └── docker-ci.yml
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
└── README.md
```

*The folder structure may vary depending on which components have been created and committed.*

## 🚀 Run the Application

Start the Docker Compose application:

```bash
docker compose up -d
```

Check running containers:

```bash
docker ps
```

View logs:

```bash
docker compose logs
```

Open the application in a browser:

http://localhost:3000

## 🔄 CI/CD Workflow

1. Developer modifies the application code.
2. Changes are committed and pushed to GitHub.
3. GitHub Actions starts automatically.
4. The workflow builds the Docker image.
5. The container starts in the CI environment.
6. An HTTP request tests the application.
7. The workflow reports success or failure.

**Current scope:** Automated build and test. Image publishing and deployment are planned enhancements.

## 🔐 Security Practices

- Do not commit `.env` files containing credentials.
- Do not upload private SSH keys (`.pem`) to GitHub.
- Use `.gitignore` to exclude secrets and unnecessary files.
- Store deployment credentials in GitHub Actions Secrets.
- Use least-privilege permissions for cloud resources.

## 📚 Learning Outcomes

Through this project, I am developing practical skills in:

- Docker containerization
- Linux and Ubuntu administration
- Git and GitHub
- CI/CD automation
- Nginx web server configuration
- Application deployment fundamentals
- DevOps workflow and troubleshooting

## 👩‍💻 Author

**Ayesha Jamil**

Emerging DevOps Engineer | AWS | Git & GitHub | Cloud Infrastructure

---

This is a hands-on learning project created to build practical DevOps skills through containerization, version control, and CI/CD automation.
