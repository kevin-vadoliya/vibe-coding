<img width="1600" height="865" alt="image" src="https://github.com/user-attachments/assets/ba01ed2b-8213-4c73-8150-242be326ff2b" />

# GitHub Integration using VS Code

## 📌 Objective
To implement and understand GitHub integration using Visual Studio Code.

---

## 📋 Prerequisites

Before starting, ensure the following software is installed:

- Git
- Visual Studio Code (VS Code)
- GitHub Account
- GitHub Pull Requests and Issues Extension (Optional but Recommended)

---

# Step 1: Install Git

1. Download Git from:
   https://git-scm.com/downloads

2. Install Git using the default settings.

3. Verify the installation by opening **Command Prompt** and running:

```bash
git --version
```

### Example Output

```bash
git version 2.49.0
```

---

# Step 2: Create a GitHub Account

1. Visit https://github.com
2. Click **Sign Up**.
3. Verify your email address.
4. Log in to your GitHub account.

---

# Step 3: Install Visual Studio Code

1. Download VS Code from:

   https://code.visualstudio.com/

2. Install it using the default settings.

---

# Step 4: Configure Git

Open **Command Prompt**.

### Set Git Username

```bash
git config --global user.name "Your Name"
```

### Set Git Email

```bash
git config --global user.email "your@email.com"
```

### Verify Configuration

```bash
git config --list
```

---

# Step 5: Open VS Code

1. Open **Visual Studio Code**.
2. Click **File → Open Folder**.
3. Select your project folder.

---

# Step 6: Initialize Git Repository

Open the terminal in VS Code.

```
Terminal
   ↓
New Terminal
```

Run the following command:

```bash
git init
```

### Example Output

```text
Initialized empty Git repository in C:/Project/.git/
```

---
