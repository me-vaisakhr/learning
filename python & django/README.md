# Full-Stack Development Learning 🚀

> **My journey from React Developer to Full-Stack AI Developer**  
> 12 weeks | Python + Django + AI Integration

---

## 📁 Folder Structure

```
python & django/
├── README.md                   # This file - Quick reference guide
├── .claude_instructions.md     # Claude CLI context (DON'T DELETE!)
├── ROADMAP.md                  # Master progress tracker
├── week1/                      # Week 1: Python Basics
├── week2/                      # Week 2: Django Setup
├── week3/                      # Week 3: Models & ORM
├── week4/                      # Week 4: Database Fundamentals
├── week5/                      # Week 5: Django ORM Deep Dive
├── week6/                      # Week 6: REST Fundamentals
├── week7/                      # Week 7: Django REST Framework
├── week8/                      # Week 8: LLM Basics
├── week9/                      # Week 9: LLM APIs
├── week10/                     # Week 10: LangChain
├── week11/                     # Week 11: RAG Implementation
├── week12/                     # Week 12: Full-Stack AI Integration
├── notes/                      # Learning notes & insights
└── projects/                   # Practice projects
```

---

## 🎯 Quick Start

### Daily Learning Workflow

1. **Open ROADMAP.md** - Check today's goals
2. **Study for 1-2 hours** - Follow the week's checklist
3. **Write code** - Practice exercises
4. **Update ROADMAP.md** - Fill in daily notes and check off completed items
5. **Ask Claude for help** - Use Claude CLI when stuck

---

## 🤖 Using Claude CLI

### Setup (One-time)

Make sure `.claude_instructions.md` exists in this folder. This file tells Claude:
- Your background (React dev, learning Python from scratch)
- Your learning goals and roadmap
- How to help you effectively

**Important:** Claude CLI automatically reads `.claude_instructions.md` when you run it from this folder!

### Common Commands

```bash
# Get help on current topic (Socratic guidance)
claude "Explain [topic]"

# When stuck - Claude will ask YOU guiding questions
claude "I'm stuck on this problem: [describe problem]"
claude "Help me debug this error"

# Compare to JavaScript
claude "How is this different from JavaScript?"

# Review your code (you'll get questions, not just answers)
claude "Review my code in week1/calculator.py"

# Only when you want direct answers
claude "Just tell me the answer to [problem]"
claude "Show me the solution"

# Check progress and get suggestions
claude "Check my ROADMAP.md and suggest what to focus on next"

# Ask for exercises
claude "Give me practice exercises for [topic]"

# Update instructions when you progress
claude "Update my current focus in .claude_instructions.md to Week 2"
```

### Examples

**Instead of repeating context:**
```bash
# ❌ Don't do this every time
claude "I'm a React dev learning Django, no Python experience, 
explain views and compare to Express routes"

# ✅ Just ask directly
claude "Explain Django views"
# Claude already knows your background from .claude_instructions.md!
```

**Quick help:**
```bash
# Ask about today's work
claude "I'm on Week 1 Day 3, help me with list comprehensions"

# Get unstuck
claude "I'm stuck on today's exercise"

# Review code
claude "Review calculator.py and give feedback"
```

---

## 📊 Tracking Progress

### Update ROADMAP.md Daily

After each learning session, update `ROADMAP.md`:

1. **Check off completed items:**
   ```markdown
   - [x] Python installation & setup  ← Change [ ] to [x]
   ```

2. **Fill in daily notes:**
   ```markdown
   #### Day 1 - Oct 4, 2025
   - **Time:** 1.5h
   - **Completed:** Learned variables, data types, loops
   - **Struggles:** List comprehensions syntax
   - **Tomorrow's Goal:** Practice more comprehensions, start functions
   ```

3. **Update "Current Focus" section** in `.claude_instructions.md` weekly:
   ```markdown
   **Current Phase:** Phase 1  
   **Current Week:** Week 2  
   **Current Day:** Day 8  
   ```

---

## 📚 Learning Resources

### Phase 1-3: Backend Fundamentals
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [Django Official Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Django REST Framework](https://www.django-rest-framework.org/)

### Phase 4-5: AI Integration
- [Generative AI with LLMs - Coursera](https://www.coursera.org/learn/generative-ai-with-llms)
- [LangChain for LLM App Development](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/)
- [Krish Naik YouTube](https://www.youtube.com/@krishnaik06)

### Documentation
- [Python Docs](https://docs.python.org/3/)
- [Django Docs](https://docs.djangoproject.com/)
- [OpenAI API](https://platform.openai.com/docs/)
- [Anthropic API](https://docs.anthropic.com/)

---

## 🗓️ Timeline

| Week | Phase | Focus Area | Status |
|------|-------|------------|--------|
| 1 | Phase 1 | Python Basics | ⬜ |
| 2 | Phase 1 | Django Setup & Structure | ⬜ |
| 3 | Phase 1 | Models & ORM Basics | ⬜ |
| 4 | Phase 2 | Database Fundamentals | ⬜ |
| 5 | Phase 2 | Django ORM Deep Dive | ⬜ |
| 6 | Phase 3 | REST Fundamentals | ⬜ |
| 7 | Phase 3 | Django REST Framework | ⬜ |
| 8 | Phase 4 | LLM Basics & Prompting | ⬜ |
| 9 | Phase 4 | LLM APIs & Integration | ⬜ |
| 10 | Phase 5 | LangChain Framework | ⬜ |
| 11 | Phase 5 | RAG Implementation | ⬜ |
| 12 | Phase 5 | Full-Stack AI Integration | ⬜ |

**Update status:** ⬜ Not Started | 🔄 In Progress | ✅ Complete

---

## 💡 Important Reminders

### DO's ✅
- **Practice daily** (1-2 hours minimum)
- **Write code, don't just read** - hands-on learning is key
- **Update ROADMAP.md** after each session
- **Ask Claude for help** when stuck - that's what it's for!
- **Compare to JavaScript** - leverage your existing knowledge
- **Build the practice projects** - they're crucial for learning
- **Commit code to Git** regularly
- **Take breaks** when frustrated

### DON'T's ❌
- **Don't delete** `.claude_instructions.md` - Claude needs this!
- **Don't skip fundamentals** - build strong basics first
- **Don't just copy code** - understand what it does
- **Don't compare your progress** to others - go at your own pace
- **Don't skip the exercises** - they reinforce learning
- **Don't move ahead** if you don't understand current concepts

---

## 🐍 Python Environment Setup

### First Time Setup

```bash
# Check Python version (need 3.10+)
python3 --version

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install Django (when you reach Week 2)
pip install django

# Install DRF (when you reach Week 7)
pip install djangorestframework
```

### Daily Usage

```bash
# Always activate venv before working
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Deactivate when done
deactivate
```

---

## 🛠️ Useful Commands

### Python
```bash
# Run Python file
python filename.py

# Interactive Python shell
python

# Check installed packages
pip list

# Install package
pip install package-name
```

### Django (Week 2+)
```bash
# Create new project
django-admin startproject projectname

# Create new app
python manage.py startapp appname

# Run development server
python manage.py runserver

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Django shell
python manage.py shell
```

### Git
```bash
# Initialize repo (first time)
git init

# Check status
git status

# Add files
git add .

# Commit changes
git commit -m "Completed Week 1 Day 3"

# Push to GitHub
git push origin main
```

---

## 🎯 Weekly Review Process

At the end of each week:

1. **Complete weekly reflection** in ROADMAP.md
2. **Update timeline table** above (change ⬜ to ✅)
3. **Update `.claude_instructions.md`** with new week/phase
4. **Commit progress to Git**
5. **Plan next week's focus areas**

---

## 🚨 Troubleshooting

### Claude CLI Not Understanding Context
- ✅ Ensure `.claude_instructions.md` exists in this folder
- ✅ Run Claude CLI from this directory
- ✅ Check if file content is up-to-date

### Python Import Errors
- ✅ Make sure virtual environment is activated
- ✅ Check if package is installed: `pip list`
- ✅ Reinstall package: `pip install package-name`

### Django Errors
- ✅ Check migrations: `python manage.py migrate`
- ✅ Verify settings.py configuration
- ✅ Check server is running: `python manage.py runserver`

---

## 📈 Progress Tracking

**Start Date:** [Add your start date]  
**Target Completion:** [12 weeks from start]  
**Current Week:** Week 1  
**Total Hours Logged:** 0h  

**Completed Phases:** 0/5  
**Completed Weeks:** 0/12  
**Completed Projects:** 0

---

## 🏆 Milestones

- [ ] **Week 3** - Built first Django app
- [ ] **Week 5** - Designed complex database schema
- [ ] **Week 7** - Built REST API with authentication
- [ ] **Week 9** - Integrated LLM into Django app
- [ ] **Week 12** - Built full-stack AI application

---

## 🎓 Next Steps After Completion

1. Build capstone project (see ROADMAP.md for ideas)
2. Create portfolio website showcasing projects
3. Contribute to open-source Django projects
4. Apply for full-stack positions
5. Continue learning: Docker, Celery, Advanced AI

---

## 📞 Getting Help

### When Stuck
1. **Read error messages carefully** - they usually tell you what's wrong
2. **Use Claude CLI** - ask for help understanding the error
3. **Check documentation** - Django docs are excellent
4. **Search Stack Overflow** - someone likely had the same issue
5. **Review ROADMAP.md** - see if you missed a prerequisite topic

### Best Practices for Asking Claude
```bash
# ✅ Good - Specific with context
claude "I'm getting ImportError when running my Django view. 
Here's the error: [paste error]. Here's my code: [paste code]"

# ❌ Bad - Too vague
claude "My code doesn't work"
```

---

## 🎉 Motivation

**Remember why you started:**
- Build AI-powered applications
- Become a T-shaped full-stack developer
- Increase career opportunities
- Contribute to Entri's educational technology

**You've got this!** 💪

Every expert was once a beginner. Stay consistent, stay curious, and you'll be building full-stack AI apps in 12 weeks!

---

**Last Updated:** [Add date]  
**Next Review:** [End of Week 1]
