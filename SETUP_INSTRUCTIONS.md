# 🚀 PORTFOLIO SETUP - STEP BY STEP

## ✅ WHAT YOU HAVE

A complete, ready-to-use portfolio website with:
- ✅ 8 Root files
- ✅ 1 Data file (projects.json)
- ✅ 2 CSS/JS files
- ✅ 8 HTML templates
- ✅ **Total: 19 files** (+ your CV = 20)

---

## 📥 STEP 1: EXTRACT FILES

### Option A: Replace Entire Folder (Easiest)

1. **Backup** your existing `D:\VSCODE_Works\Portfolio\venv\` folder
2. **Delete** everything else in `D:\VSCODE_Works\Portfolio\`
3. **Extract** `portfolio-complete` folder contents to `D:\VSCODE_Works\Portfolio\`
4. **Restore** your `venv\` folder

### Option B: Selective Copy

1. Download `portfolio-complete` folder
2. Copy each file to its location (see FILE_STRUCTURE.md)
3. Keep existing `venv\` folder

---

## 📂 STEP 2: VERIFY STRUCTURE

Your folder should look like this:

```
D:\VSCODE_Works\Portfolio\
├── venv\                    ✓ (existing)
├── app.py                   ✓
├── requirements.txt         ✓
├── setup_data.py           ✓
├── build_static.py         ✓
├── deploy_github_pages.py  ✓
├── .gitignore              ✓
├── netlify.toml            ✓
├── README.md               ✓
├── data\
│   └── projects.json       ✓
├── static\
│   ├── css\
│   │   └── main.css        ✓
│   ├── js\
│   │   └── main.js         ✓
│   ├── files\
│   │   └── (empty - add CV here)
│   └── images\
│       └── (empty - optional)
└── templates\
    ├── base.html           ✓
    ├── index.html          ✓
    ├── about.html          ✓
    ├── projects.html       ✓
    ├── project_detail.html ✓
    ├── publications.html   ✓
    ├── contact.html        ✓
    └── 404.html            ✓
```

---

## ⚙️ STEP 3: INSTALL DEPENDENCIES

```powershell
# Open PowerShell in Portfolio folder
cd D:\VSCODE_Works\Portfolio

# Activate virtual environment
venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

**Expected output:**
```
Successfully installed Flask-3.0.0 Frozen-Flask-1.0.1 ...
```

---

## 📊 STEP 4: GENERATE DATA FILES

```powershell
# Still in activated venv
python setup_data.py
```

**Expected output:**
```
Creating portfolio data files...
======================================================================
✓ Created data/profile.json
✓ Created data/animesh_cv_data.json
======================================================================
✓ All data files created successfully!

Data Summary:
  • Publications: 9 journal papers
  • Conference Papers: 4 proceedings
  • Experience: 5 positions
  • Education: 4 degrees
  • Training: 7 programs
  • Awards: 4 recognitions

You can now run: python app.py
Visit: http://localhost:5000
```

---

## 📄 STEP 5: ADD YOUR CV (Optional)

Copy your CV PDF to:
```
D:\VSCODE_Works\Portfolio\static\files\Animesh_Choudhury_CV.pdf
```

Or use any name and update in code.

---

## 🧪 STEP 6: TEST LOCALLY

```powershell
# Run the Flask app
python app.py
```

**Expected output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

**Open browser:** http://localhost:5000

**Test all pages:**
- ✅ Home: http://localhost:5000/
- ✅ About: http://localhost:5000/about
- ✅ Projects: http://localhost:5000/projects
- ✅ Publications: http://localhost:5000/publications
- ✅ Contact: http://localhost:5000/contact

---

## 🌐 STEP 7: DEPLOY TO GITHUB PAGES

```powershell
# Stop the local server (Ctrl+C)

# Run deployment script
python deploy_github_pages.py
```

**Follow the on-screen instructions!**

The script will:
1. Build static site
2. Create .nojekyll file
3. Ask for custom domain (optional)
4. Give you GitHub deployment commands

---

## ✅ VERIFICATION CHECKLIST

After setup, verify:

### Files Exist:
- [ ] All 8 root files present
- [ ] data/projects.json exists
- [ ] static/css/main.css exists
- [ ] static/js/main.js exists
- [ ] All 8 HTML templates in templates/
- [ ] venv/ folder present

### Commands Work:
- [ ] `venv\Scripts\activate` activates venv
- [ ] `pip install -r requirements.txt` installs packages
- [ ] `python setup_data.py` generates data
- [ ] `python app.py` runs server
- [ ] http://localhost:5000 loads
- [ ] All pages accessible

### Generated Files:
- [ ] data/profile.json created
- [ ] data/animesh_cv_data.json created

---

## 🐛 TROUBLESHOOTING

### Issue: "ModuleNotFoundError: No module named 'flask'"

**Solution:**
```powershell
venv\Scripts\activate
pip install -r requirements.txt
```

### Issue: "FileNotFoundError: data\profile.json"

**Solution:**
```powershell
python setup_data.py
```

### Issue: "Build folder error"

**Solution:**
```powershell
# Delete build folder
Remove-Item -Recurse -Force build
# Try again
python deploy_github_pages.py
```

### Issue: Port 5000 in use

**Solution:**
```powershell
# Kill the process or use different port
# Edit app.py, change last line to:
# app.run(debug=True, port=5001)
```

---

## 📱 WHAT'S NEXT?

After local testing works:

1. **Deploy to GitHub Pages**
   ```powershell
   python deploy_github_pages.py
   ```

2. **Get a custom domain** (optional)
   - Buy from Namecheap, Google Domains, etc.
   - Configure DNS as shown in deployment script
   - Wait 24-48 hours

3. **Share your portfolio**
   - Add to LinkedIn
   - Include in CV
   - Share on ResearchGate
   - Use for applications

---

## 🎯 QUICK COMMAND REFERENCE

```powershell
# Activate environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Generate data
python setup_data.py

# Test locally
python app.py

# Build for deployment
python deploy_github_pages.py

# Check what's in build folder
dir build
```

---

## 💡 TIPS

1. **Always activate venv** before running Python commands
2. **Keep venv folder** - it has all installed packages
3. **Don't edit build/** folder - it's auto-generated
4. **Update data/** files to change content
5. **Test locally first** before deploying

---

## 📞 NEED HELP?

Check these files:
- `FILE_STRUCTURE.md` - Complete file listing
- `README.md` - General documentation  
- `GITHUB_PAGES_CUSTOM_DOMAIN.md` - Deployment guide

---

## ✨ YOU'RE READY!

Follow these 7 steps and your portfolio will be:
- ✅ Running locally
- ✅ Ready to deploy
- ✅ Professional looking
- ✅ Fully functional

**Total setup time: 10-15 minutes**

Good luck! 🚀
