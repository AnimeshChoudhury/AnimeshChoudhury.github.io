# Animesh Choudhury - Portfolio Website

A creative, multi-page portfolio website for showcasing research work, publications, and projects.

## 🎨 Design Style

**Creative Portfolio** with bold colors, modern typography, and smooth animations.

**Color Scheme:**
- Deep Ocean Blue (#0a4d68) - Primary
- Teal (#088395) - Primary Light  
- Bold Orange (#e8630a) - Accent
- Dark Slate (#2d3250) - Text

**Typography:**
- Display: Playfair Display (bold headers)
- Mono: Space Mono (labels, code)
- Body: Work Sans (clean, readable)

## 📁 Project Structure

```
Portfolio/
├── venv/                     # Virtual environment
├── app.py                    # Flask application
├── requirements.txt          # Dependencies
├── setup_data.py            # Data setup script
├── README.md                # This file
├── data/                    # Data files (auto-created)
│   ├── profile.json
│   ├── animesh_cv_data.json
│   └── projects.json
├── static/                  # Static files
│   ├── css/
│   │   └── main.css
│   ├── js/
│   │   └── main.js
│   ├── images/              # Your images
│   └── files/
│       └── Animesh_Choudhury_CV.pdf
└── templates/               # HTML templates
    ├── base.html
    ├── index.html
    ├── about.html
    ├── projects.html
    ├── project_detail.html
    ├── publications.html
    ├── contact.html
    └── 404.html
```

## 🚀 Installation & Setup

### Step 1: Activate Virtual Environment

```powershell
# Navigate to Portfolio folder
cd D:\VSCODE_Works\Portfolio

# Activate virtual environment
venv\Scripts\activate
```

### Step 2: Install Dependencies

```powershell
pip install -r requirements.txt
```

### Step 3: Create Data Files (First Time Only)

```powershell
python setup_data.py
```

This creates:
- `data/profile.json` - Your profile information
- `data/animesh_cv_data.json` - Your CV data  
- `data/projects.json` - Project details

### Step 4: Add Your CV (Optional)

Copy your CV PDF to:
```
static/files/Animesh_Choudhury_CV.pdf
```

### Step 5: Run the Website

```powershell
python app.py
```

Visit: **http://localhost:5000**

## 📄 Pages

1. **Home** (`/`) - Hero section with introduction
2. **About** (`/about`) - Detailed bio, experience, education
3. **Projects** (`/projects`) - Showcase of research projects
4. **Publications** (`/publications`) - Research papers and citations
5. **Contact** (`/contact`) - Contact form and social links

## 🎯 Features

- ✅ Responsive design (mobile, tablet, desktop)
- ✅ Creative, modern layout
- ✅ 5 detailed research projects
- ✅ Publications with citation counts
- ✅ Contact form
- ✅ CV download
- ✅ Social media integration
- ✅ Smooth animations
- ✅ Fast loading

## 🛠️ Customization

### Update Your Information

Edit `data/profile.json`:
```json
{
  "name": "Your Name",
  "title": "Your Title",
  "email": "your.email@example.com",
  ...
}
```

### Add/Edit Projects

Edit `data/projects.json`:
```json
{
  "projects": [
    {
      "title": "Project Name",
      "description": "Project description",
      ...
    }
  ]
}
```

### Change Colors

Edit `templates/base.html` (CSS variables section):
```css
:root {
  --primary: #0a4d68;      /* Change primary color */
  --accent: #e8630a;       /* Change accent color */
  ...
}
```

## 📦 Deployment to Netlify

### Method 1: Drag & Drop

1. Build static site:
   ```powershell
   python build_static.py
   ```

2. Drag `build/` folder to Netlify

### Method 2: Git Deployment

1. Create `.gitignore`:
   ```
   venv/
   __pycache__/
   *.pyc
   .env
   ```

2. Push to GitHub

3. Connect GitHub repo to Netlify

4. Build settings:
   - Build command: `pip install -r requirements.txt && python build_static.py`
   - Publish directory: `build`

## 🔧 Troubleshooting

### "FileNotFoundError: data\profile.json"

**Solution:** Run `python setup_data.py`

### "No module named 'flask'"

**Solution:** 
```powershell
venv\Scripts\activate
pip install -r requirements.txt
```

### Port 5000 already in use

**Solution:** Change port in `app.py`:
```python
app.run(debug=True, port=5001)  # Change 5000 to 5001
```

### Contact form not working

The contact form currently logs to console. For production:
1. Use Netlify Forms (free)
2. Use FormSpree (free)
3. Set up Flask-Mail (requires email configuration)

## 📊 Project Stats

- **5 Research Projects** (imaginative, based on your experience)
- **3 Journal Publications** (from your CV)
- **2 Conference Papers** (from your CV)
- **6 Skill Categories** (from your CV)
- **5 Work Experiences** (from your CV)

## 🌐 Social Links

Update in `data/profile.json`:
```json
"social": {
  "linkedin": "https://www.linkedin.com/in/animeshchoudhury/",
  "github": "https://github.com/AnimeshChoudhury",
  "scholar": "https://scholar.google.com/citations?user=...",
  "researchgate": "https://www.researchgate.net/profile/..."
}
```

## 🎨 Adding Images

### Profile Photo

1. Add to: `static/images/profile.jpg`
2. Update in templates where needed

### Project Images

1. Add to: `static/images/project-name.jpg`
2. Update in `data/projects.json`:
   ```json
   "image": "project-himalsnow.jpg"
   ```

## 📝 To-Do

- [ ] Add real project images
- [ ] Add profile photo
- [ ] Set up email for contact form
- [ ] Add Google Analytics (optional)
- [ ] Deploy to Netlify
- [ ] Connect custom domain (optional)

## 🆘 Support

For issues or questions:
1. Check the troubleshooting section above
2. Make sure virtual environment is activated
3. Ensure all files are in correct folders
4. Try running `python setup_data.py` again

## 📜 License

Personal use only.

---

**Built with**: Flask, HTML5, CSS3, JavaScript
**Author**: Animesh Choudhury
**Last Updated**: February 2026
