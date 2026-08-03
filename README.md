# GitHub Integration using VS Code

## 📌 Objective
To learn how to integrate GitHub with Visual Studio Code using Git and perform basic version control operations such as initializing a repository, committing changes, and pushing code to GitHub.

---

# 📋 Prerequisites

Before starting, make sure you have the following installed:

- Git
- Visual Studio Code (VS Code)
- GitHub Account
- GitHub Pull Requests and Issues Extension (Optional)

---

# 🛠 Step 1: Install Git

1. Visit:
   https://git-scm.com/downloads

2. Download Git for Windows.

3. Install using the default settings.

4. Verify installation.

Open **Command Prompt** and type:

```bash
git --version
```

Example Output:

```bash
git version 2.49.0
```

---

# 🛠 Step 2: Create GitHub Account

1. Open https://github.com

2. Click **Sign Up**

3. Verify Email

4. Login to GitHub

---

# 🛠 Step 3: Install Visual Studio Code

Download VS Code from:

https://code.visualstudio.com/

Install it normally.

---

# 🛠 Step 4: Configure Git

Open Command Prompt.

Set Username

```bash
git config --global user.name "Your Name"
```

Set Email

```bash
git config --global user.email "your@email.com"
```

Verify Configuration

```bash
git config --list
```

---

# 🛠 Step 5: Open Project in VS Code

1. Open Visual Studio Code.

2. Click

```
File
    ↓
Open Folder
```

3. Select your Project Folder.

---

# 🛠 Step 6: Initialize Git Repository

Open Terminal

```
Terminal
      ↓
New Terminal
```

Run

```bash
git init
```

Output

```text
Initialized empty Git repository
```

---

# 🛠 Step 7: Create Project File

Create a file.

Example

```
demo.txt
```

or

```
index.html
```

Save the file.

---

# 🛠 Step 8: Check Repository Status

Run

```bash
git status
```

Output

```text
Untracked files:
demo.txt
```

---

# 🛠 Step 9: Stage Files

Stage all files

```bash
git add .
```

or stage single file

```bash
git add demo.txt
```

Check status again

```bash
git status
```

---

# 🛠 Step 10: Commit Changes

Run

```bash
git commit -m "Initial commit"
```

---

# 🛠 Step 11: Create GitHub Repository

1. Login to GitHub

2. Click **New Repository**

3. Enter Repository Name

Example

```
GitHubIntegration
```

4. Click **Create Repository**

---

# 🛠 Step 12: Connect Local Repository with GitHub

Copy Repository URL.

Example

```text
https://github.com/username/GitHubIntegration.git
```

Run

```bash
git remote add origin https://github.com/username/GitHubIntegration.git
```

Verify

```bash
git remote -v
```

---

# 🛠 Step 13: Rename Branch

```bash
git branch -M main
```

---

# 🛠 Step 14: Push Project to GitHub

```bash
git push -u origin main
```

Login if prompted.

---

# 🛠 Step 15: Verify Repository

Refresh GitHub.

You should now see your project files.

---

# 🛠 Step 16: Make Changes

Edit your project.

Example

```text
Hello GitHub
```

↓

```text
Hello GitHub from VS Code
```

Save the file.

---

# 🛠 Step 17: Commit Updated Changes

```bash
git add .
```

```bash
git commit -m "Updated project"
```

---

# 🛠 Step 18: Push Updated Code

```bash
git push
```

---

# 🛠 Step 19: Clone Repository

To download repository

```bash
git clone https://github.com/username/GitHubIntegration.git
```

---

# 🛠 Step 20: Pull Latest Changes

```bash
git pull origin main
```

---

# 📚 Common Git Commands

| Command | Description |
|----------|-------------|
| git init | Initialize Repository |
| git status | Check Repository Status |
| git add . | Stage All Files |
| git commit -m "message" | Save Changes |
| git push | Upload Files |
| git pull | Download Latest Changes |
| git clone URL | Clone Repository |
| git remote -v | Show Remote Repository |
| git branch -M main | Rename Branch |

---

# 🔄 Git Workflow

```
Create Project
      │
      ▼
git init
      │
      ▼
Create Files
      │
      ▼
git add .
      │
      ▼
git commit -m "Initial commit"
      │
      ▼
Create GitHub Repository
      │
      ▼
git remote add origin URL
      │
      ▼
git branch -M main
      │
      ▼
git push -u origin main
      │
      ▼
Project Uploaded Successfully
```

---

# 🎯 Learning Outcome

After completing this practical, you will be able to:

- Install Git
- Configure Git
- Create a Local Repository
- Connect VS Code with GitHub
- Commit Changes
- Push Code to GitHub
- Pull Latest Changes
- Clone a Repository

---

# 👨‍💻 Author

**Name:** Kevin Vadoliya

**Course:** Diploma Engineering

**Subject:** GitHub Integration using VS Code
