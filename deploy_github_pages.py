"""
Deploy portfolio to GitHub Pages - FIXED VERSION
Cleans up properly and avoids file conflicts
"""

import os
import shutil

print("\n" + "="*70)
print("Preparing Portfolio for GitHub Pages")
print("="*70)

# STEP 1: Clean old build directory completely
print("\n[1/5] Cleaning old build directory...")
if os.path.exists('build'):
    try:
        shutil.rmtree('build')
        print("✓ Old build directory removed")
    except Exception as e:
        print(f"⚠️ Warning: Could not remove old build: {e}")
        print("  Please manually delete the 'build' folder and try again")
        input("\nPress Enter after deleting the build folder...")

# STEP 2: Import and build
print("\n[2/5] Building static site...")
try:
    from flask_frozen import Freezer
    from app import app
    
    # Configure freezer
    app.config['FREEZER_DESTINATION'] = 'build'
    app.config['FREEZER_RELATIVE_URLS'] = True
    app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
    
    freezer = Freezer(app)
    
    # Freeze
    freezer.freeze()
    print("✓ Static site built successfully")
    
except Exception as e:
    print(f"✗ Error building site: {e}")
    print("\nTroubleshooting:")
    print("1. Make sure Flask app runs: python app.py")
    print("2. Delete 'build' folder manually")
    print("3. Check for file/folder name conflicts")
    raise

# STEP 3: Create .nojekyll file
print("\n[3/5] Creating .nojekyll file...")
try:
    with open('build/.nojekyll', 'w') as f:
        pass
    print("✓ .nojekyll file created (prevents Jekyll processing)")
except Exception as e:
    print(f"⚠️ Warning: Could not create .nojekyll: {e}")

# STEP 4: Custom domain setup
print("\n[4/5] Custom domain configuration...")
domain = input("Enter your custom domain (e.g., animeshchoudhury.com) or press Enter to skip: ").strip()

if domain:
    try:
        with open('build/CNAME', 'w') as f:
            f.write(domain)
        print(f"✓ CNAME file created with domain: {domain}")
        print(f"  📝 Remember to configure DNS records at your domain registrar!")
    except Exception as e:
        print(f"⚠️ Warning: Could not create CNAME: {e}")
else:
    print("  Skipped - will use username.github.io")

# STEP 5: Create README
print("\n[5/5] Creating README...")
try:
    with open('build/README.md', 'w') as f:
        f.write(f"""# Animesh Choudhury - Portfolio Website

Professional portfolio showcasing research, publications, and projects.

## Live Site

- GitHub Pages: https://yourusername.github.io
{f'- Custom Domain: https://{domain}' if domain else ''}

## Features

- Research portfolio
- Publications showcase
- Interactive project gallery
- Contact form
- Responsive design

## Tech Stack

- Flask (Python)
- HTML5/CSS3
- JavaScript
- Bootstrap styling

---

*Built with Flask-Frozen for GitHub Pages deployment*
""")
        print("✓ README created")
except Exception as e:
    print(f"⚠️ Warning: Could not create README: {e}")

# Success message
print("\n" + "="*70)
print("✓ Static Site Ready for GitHub Pages!")
print("="*70)

print("\n📋 DEPLOYMENT INSTRUCTIONS:")
print("\n" + "-"*70)
print("STEP 1: Create GitHub Repository")
print("-"*70)
print("Repository name MUST be: USERNAME.github.io")
print("(Replace USERNAME with your actual GitHub username)")
print("\nExample: If username is 'AnimeshChoudhury', repo name is:")
print("         AnimeshChoudhury.github.io")
print("\n1. Go to: https://github.com/new")
print("2. Repository name: USERNAME.github.io")
print("3. Set to PUBLIC")
print("4. Don't initialize with README")
print("5. Click 'Create repository'")

print("\n" + "-"*70)
print("STEP 2: Deploy Your Site")
print("-"*70)
print("\nRun these commands in PowerShell:\n")

print("cd build")
print("git init")
print("git add .")
print('git commit -m "Deploy portfolio to GitHub Pages"')
print("git remote add origin https://github.com/USERNAME/USERNAME.github.io.git")
print("git branch -M main")
print("git push -u origin main")

print("\n(Replace USERNAME with your GitHub username)")

print("\n" + "-"*70)
print("STEP 3: Enable GitHub Pages")
print("-"*70)
print("1. Go to your repository on GitHub")
print("2. Click 'Settings'")
print("3. Scroll to 'Pages' in left sidebar")
print("4. Under 'Source':")
print("   - Branch: main")
print("   - Folder: / (root)")
print("5. Click 'Save'")
print("6. Wait 2-3 minutes")

print("\n" + "-"*70)
print("STEP 4: Your Site Will Be Live!")
print("-"*70)
print("\nYour portfolio: https://USERNAME.github.io")

if domain:
    print("\n" + "-"*70)
    print("STEP 5: Configure Custom Domain")
    print("-"*70)
    print(f"\nFor domain: {domain}")
    print("\n1. At your domain registrar, add these DNS records:")
    print("\n   A Records (add all 4):")
    print("   @ → 185.199.108.153")
    print("   @ → 185.199.109.153")
    print("   @ → 185.199.110.153")
    print("   @ → 185.199.111.153")
    print("\n   CNAME Record:")
    print("   www → USERNAME.github.io")
    print("\n2. In GitHub: Settings → Pages → Custom domain")
    print(f"   Enter: {domain}")
    print("   Click 'Save'")
    print("\n3. Enable 'Enforce HTTPS' (after DNS propagates)")
    print("\n4. Wait 24-48 hours for DNS propagation")
    print(f"\nYour site will be: https://{domain}")

print("\n" + "="*70)
print("🚀 All Files Ready in 'build/' Folder!")
print("="*70)

print("\n💡 TIP: To update your site later:")
print("1. Make changes to your portfolio")
print("2. Run: python deploy_github_pages.py")
print("3. cd build")
print("4. git add . && git commit -m 'Updated' && git push")
print("\n✨ Your site updates automatically!\n")
