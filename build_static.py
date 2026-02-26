"""
Build static version of portfolio website for deployment
Converts Flask app to static HTML files
"""

from flask_frozen import Freezer
from app import app
import os
import shutil

print("\n" + "="*70)
print("Building Static Portfolio Website")
print("="*70)

# Configure freezer
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

freezer = Freezer(app)

# Clean build directory if exists
if os.path.exists('build'):
    print("\nCleaning old build directory...")
    shutil.rmtree('build')
    print("✓ Old build removed")

print("\nGenerating static files...")
print("This may take a minute...")

try:
    # Freeze the app (generate static files)
    freezer.freeze()
    
    print("\n" + "="*70)
    print("✓ Static Site Successfully Built!")
    print("="*70)
    print(f"\nOutput directory: build/")
    print("\nGenerated files:")
    
    # List generated files
    for root, dirs, files in os.walk('build'):
        level = root.replace('build', '').count(os.sep)
        indent = ' ' * 2 * level
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 2 * (level + 1)
        for file in files[:10]:  # Show first 10 files per directory
            print(f'{subindent}{file}')
        if len(files) > 10:
            print(f'{subindent}... and {len(files) - 10} more files')
    
    print("\n" + "="*70)
    print("Ready for Deployment!")
    print("="*70)
    print("\nNext steps:")
    print("1. Upload 'build/' folder to Netlify/Vercel")
    print("2. Or push to GitHub and connect to Netlify")
    print("\n")

except Exception as e:
    print(f"\n✗ Error building static site: {e}")
    print("Check your Flask app for errors.")
    raise

