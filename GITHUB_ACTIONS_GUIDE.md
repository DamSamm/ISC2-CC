# GitHub Actions Automated Deployment Guide

## What is GitHub Actions?

GitHub Actions is an **automated deployment system** that:
- ✅ Automatically deploys your site when you push code
- ✅ Builds and publishes to GitHub Pages instantly
- ✅ No manual configuration needed
- ✅ Works automatically every time you update files
- ✅ Completely free!

---

## Setup Instructions (Even Easier!)

### Step 1: Push to GitHub

Instead of manually uploading files through the web interface, you'll use Git to push your code:

```bash
# Navigate to your quiz folder
cd c:\Users\samue\Documents\isc2\ CC

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit your changes
git commit -m "Initial commit: ISC2 CC Quiz with GitHub Actions"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/isc2-cc-quiz.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 2: GitHub Actions Does Everything Else!

Once you push to GitHub:
1. GitHub automatically sees the `.github/workflows/deploy.yml` file
2. GitHub Actions runs automatically
3. Your site deploys to GitHub Pages instantly
4. You get a live URL within seconds!

**No need to manually enable GitHub Pages** - the workflow does it all!

---

## How the Workflow Works

### Automatic Triggers
The workflow automatically runs when:
- ✅ You push to `main` or `master` branch
- ✅ You create a pull request
- ✅ You manually trigger it (optional)

### What It Does
1. **Checks out** your code from GitHub
2. **Configures** GitHub Pages settings
3. **Uploads** all files as artifact
4. **Deploys** to GitHub Pages

All in **under 30 seconds!**

---

## Workflow File Explanation

Your `.github/workflows/deploy.yml` file:

```yaml
name: Deploy to GitHub Pages
# What this workflow is called

on:
  push:
    branches: ["main", "master"]
  # Runs when you push to main branch

permissions:
  pages: write
  id-token: write
  # Permissions needed to deploy

jobs:
  deploy:
    runs-on: ubuntu-latest
    # Uses Ubuntu server to run the job
    
    steps:
      - uses: actions/checkout@v3
      # Download your code
      
      - uses: actions/configure-pages@v3
      # Set up GitHub Pages
      
      - uses: actions/upload-pages-artifact@v1
      # Upload your files
      
      - uses: actions/deploy-pages@v2
      # Deploy to the internet!
```

---

## Step-by-Step Setup

### 1️⃣ Install Git

**Windows:**
- Download from [git-scm.com](https://git-scm.com)
- Run installer and accept defaults
- Restart your computer

**Mac:**
- Download from [git-scm.com](https://git-scm.com)
- Or use Homebrew: `brew install git`

### 2️⃣ Configure Git (First Time Only)

Open PowerShell or Terminal and run:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3️⃣ Create GitHub Repository

1. Log in to [github.com](https://github.com)
2. Click "+" → "New repository"
3. Name: `isc2-cc-quiz`
4. **Important:** Select "Public"
5. **Do NOT** initialize with README (we have our own)
6. Click "Create repository"

### 4️⃣ Push Your Code

In PowerShell, navigate to your quiz folder:

```bash
cd c:\Users\samue\Documents\isc2\ CC

# If you haven't initialized git yet:
git init
git add .
git commit -m "Initial commit: ISC2 CC Quiz with GitHub Actions"

# Add your GitHub repo
git remote add origin https://github.com/YOUR_USERNAME/isc2-cc-quiz.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 5️⃣ Wait for Deployment

1. Go to your repository on GitHub
2. Click the "Actions" tab
3. Watch the workflow run (it's fast!)
4. Once complete, go to "Settings" → "Pages"
5. Your live URL is displayed!

---

## Monitoring Your Deployment

### View Deployment Status

1. Go to your repository
2. Click the **"Actions"** tab
3. See all your deployments listed
4. Click one to see details

### What Success Looks Like

✅ Green checkmark next to commit
✅ "Deploy to GitHub Pages" shows "success"
✅ Your site is live at: `https://yourusername.github.io/isc2-cc-quiz/`

### If Something Fails

🔴 Red X next to commit - Click it to see error details
- Most common: Wrong permissions or typo in config
- Check error message and follow instructions
- Fix and push again

---

## Making Updates (The Best Part!)

### Update Questions

1. Edit `questions.json` locally
2. Save the file
3. Run these commands:

```bash
git add questions.json
git commit -m "Add more ISC2 CC questions"
git push
```

**That's it!** GitHub Actions automatically deploys within seconds!

### Update Quiz Design

1. Edit `index.html` locally
2. Change colors, title, or layout
3. Push to GitHub:

```bash
git add index.html
git commit -m "Update quiz styling"
git push
```

**Instant deployment!**

### Update Documentation

1. Edit `README.md` locally
2. Push to GitHub:

```bash
git add README.md
git commit -m "Update README"
git push
```

---

## GitHub Actions Benefits vs Manual Upload

### Manual Upload (Old Way)
❌ Upload files one by one
❌ Can forget files
❌ Takes 5-10 minutes
❌ Manual GitHub Pages setup
❌ Easy to mess up

### GitHub Actions (New Way)
✅ Push once, everything deploys
✅ Can't forget anything
✅ Takes 30 seconds
✅ Automatic GitHub Pages setup
✅ Impossible to mess up

---

## Useful Git Commands

### Check Status
```bash
git status
```
Shows which files changed.

### View Changes
```bash
git diff
```
Shows what changed in each file.

### View Commit History
```bash
git log
```
Shows all your commits.

### Undo Last Commit
```bash
git reset --soft HEAD~1
```
Undoes the last commit (keeps changes).

### See Your Branches
```bash
git branch
```
Shows all branches (usually just main).

---

## Troubleshooting

### "fatal: not a git repository"

```bash
# Initialize git first
git init
git add .
git commit -m "Initial commit"
git remote add origin [your-repo-url]
git push -u origin main
```

### "Permission denied (publickey)"

You need to set up SSH keys:
1. [GitHub SSH Setup Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
2. Or use HTTPS with Personal Access Token instead

### "The branch is many commits ahead of origin"

Your local repo is ahead. This is fine, just keep pushing updates.

### Workflow Not Running

1. Check `.github/workflows/deploy.yml` exists
2. Make sure it's committed and pushed
3. Go to repository → Actions tab
4. Click on the workflow and check for errors

---

## Advanced: Manual Trigger

You can manually trigger deployment without pushing code:

1. Go to your repository
2. Click **"Actions"** tab
3. Click **"Deploy to GitHub Pages"** on left
4. Click **"Run workflow"** button
5. Select branch and confirm

Useful if you change settings in GitHub.

---

## File Structure

Your repository should look like:

```
isc2-cc-quiz/
├── .github/
│   └── workflows/
│       └── deploy.yml          ← GitHub Actions config
├── index.html                  ← Quiz app
├── questions.json              ← Questions
├── README.md                   ← Docs
├── QUICK_START.md
├── SETUP_GITHUB_PAGES.md
├── QUICK_REFERENCE.txt
└── .gitignore
```

---

## Daily Workflow

### Add a New Question
```bash
# Edit questions.json
nano questions.json  # or use your editor

# Check what changed
git status

# Stage changes
git add questions.json

# Commit with message
git commit -m "Add new cryptography questions"

# Deploy
git push
```

### Update Quiz Title
```bash
# Edit index.html
# Make your changes

# Deploy
git add index.html
git commit -m "Update quiz title"
git push
```

### Fix a Bug
```bash
# Make your fix
# Test locally

# Deploy
git add .
git commit -m "Fix score calculation bug"
git push
```

---

## GitHub Pages Settings (Already Configured!)

Your workflow automatically sets these. But you can verify:

1. Go to repository
2. Settings → Pages
3. Should show:
   - **Source:** "Deploy from a branch"
   - **Branch:** "main" (configured by workflow)
   - **Folder:** "/ (root)"

If GitHub Pages isn't active, the workflow activates it automatically!

---

## Security Notes

### SSH vs HTTPS

**HTTPS (Recommended for beginners):**
```bash
git remote add origin https://github.com/YOUR_USERNAME/isc2-cc-quiz.git
```

**SSH (More secure but requires setup):**
```bash
git remote add origin git@github.com:YOUR_USERNAME/isc2-cc-quiz.git
```

### Personal Access Token (if needed)

If GitHub asks for password:
1. Create Personal Access Token: [GitHub Settings](https://github.com/settings/tokens)
2. Use token as password when pushing

---

## Monitoring Deployments

### See Deployment Status
```bash
# In your GitHub repository
Actions → Deploy to GitHub Pages → Latest run
```

### See Live Site
```
https://yourusername.github.io/isc2-cc-quiz/
```

### Monitor Performance
- GitHub provides basic analytics
- See visitors, clones in Insights tab

---

## Quick Reference Cheat Sheet

```bash
# First time setup
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOU/isc2-cc-quiz.git
git branch -M main
git push -u origin main

# Regular updates
git add .                          # Stage all changes
git commit -m "Your message"       # Commit with message
git push                           # Deploy automatically!

# Useful commands
git status                         # See what changed
git log                           # See commit history
git diff                          # See detailed changes
```

---

## It's That Simple!

✅ Push code to GitHub
✅ GitHub Actions runs automatically
✅ Your site updates instantly
✅ No manual steps needed

**Your quiz is now professionally deployed with continuous integration!** 🚀

---

## Questions?

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Git Documentation](https://git-scm.com/doc)

Enjoy your automated deployment system!
