# ISC2 Certified in Cybersecurity (CC) Quiz

An interactive web-based MCQ quiz to prepare for the ISC2 Certified in Cybersecurity (CC) certification exam.

## Features

✨ **Interactive Quiz Experience**
- 150+ questions covering all major CC certification topics
- Real-time feedback on answers
- Progress tracking with visual progress bar
- Beautiful, responsive design

📊 **Comprehensive Question Bank**
- Questions extracted from official dump materials
- Covers: Security Principles, Access Control, Network Security, and more
- Multiple difficulty levels

🎯 **User-Friendly Interface**
- Clean, modern design with dark blue gradient theme
- Mobile-responsive layout
- Instant results with detailed scoring
- Easy navigation between questions

## How to Use Locally

1. **Clone or Download** this repository
2. **Open `index.html`** in your web browser
3. Click "Start Quiz" to begin

That's it! The quiz is fully self-contained in a single HTML file with embedded CSS, JavaScript, and JSON data.

## How to Publish on GitHub Pages

### Method 1: Using Your Own GitHub Account (Recommended)

1. **Create a GitHub Account** (if you don't have one)
   - Visit [github.com](https://github.com) and sign up

2. **Create a New Repository**
   - Click "New" button on GitHub
   - Name it: `isc2-cc-quiz` (or any name you prefer)
   - Add description: "Interactive ISC2 CC Certification Quiz"
   - Choose "Public"
   - Click "Create Repository"

3. **Upload Your Files**
   - Click "Add file" → "Upload files"
   - Drag and drop these files:
     - `index.html`
     - `questions.json`
     - `README.md`
   - Click "Commit changes"

4. **Enable GitHub Pages**
   - Go to "Settings" → "Pages"
   - Under "Build and deployment", select:
     - Source: `Deploy from a branch`
     - Branch: `main` (or `master`)
     - Folder: `/ (root)`
   - Click "Save"

5. **Access Your Quiz**
   - Wait 1-2 minutes
   - Your quiz will be live at: `https://yourusername.github.io/isc2-cc-quiz/`

### Method 2: Using Git Command Line

```bash
# Navigate to your quiz folder
cd c:\Users\samue\Documents\isc2\ CC

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: ISC2 CC Quiz"

# Add remote (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

Then follow step 4 above to enable GitHub Pages.

## File Structure

```
isc2-cc-quiz/
├── index.html          # Main quiz application
├── questions.json      # Question database
└── README.md          # This file
```

## Question Format

Questions are stored in JSON format:
```json
{
  "question": "What is the primary purpose...",
  "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
  "correctAnswerIndex": 1
}
```

## Features Explained

### Start Screen
- Shows total number of questions (150+)
- Displays difficulty level
- Click "Start Quiz" to begin

### Quiz Screen
- Question counter and progress bar
- Multiple choice options with visual feedback
- Instant feedback when you select an answer
- Navigation buttons (Previous/Next)
- Color-coded answers:
  - 🟢 Green = Correct answer
  - 🔴 Red = Your incorrect answer
  - Explanation shows the correct answer

### Results Screen
- Final score as percentage
- Breakdown of correct answers
- Performance message based on score:
  - 80%+ : Excellent
  - 70-79%: Good
  - 60-69%: Average
  - Below 60%: Needs more study
- Options to review or retake quiz

## Customization

### Adding More Questions
Edit `questions.json` and add new question objects following the same format.

### Changing Theme Colors
In `index.html`, find the CSS section and modify:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Replace the hex colors (#667eea, #764ba2) with your preferred colors.

### Changing Quiz Title
Find this line in `index.html`:
```html
<h1>🔐 ISC2 CC Certification Quiz</h1>
```

Replace with your custom title.

## Browser Compatibility

Works on:
- ✅ Chrome/Chromium
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers (iOS Safari, Chrome Android)

## Tips for Studying

1. **Take the quiz multiple times** - Retake it until you score 80%+
2. **Review wrong answers** - Look up why you got questions wrong
3. **Time yourself** - Try to complete the quiz in under 60 minutes
4. **Study weak areas** - Focus on topics where you score lower
5. **Mix with official materials** - Use this alongside official ISC2 CC study guides

## License

This quiz is provided as-is for educational purposes to help with ISC2 CC certification preparation.

## Support

If you have questions or want to add more questions:
1. Edit the `questions.json` file
2. Commit and push changes to GitHub
3. Your updated quiz will be live automatically

## Additional Resources

- [ISC2 Official CC Training](https://www.isc2.org/Training)
- [CC Certification Overview](https://www.isc2.org/Certifications/CC)
- [Official Study Guide](https://www.isc2.org/Training/Self-Study-Resources/CC)

---

**Last Updated:** 2024
**Total Questions:** 150+
**Estimated Study Time:** 2-3 hours
