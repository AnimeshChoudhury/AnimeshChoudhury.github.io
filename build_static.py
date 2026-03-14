"""
Build static version of portfolio website for deployment
"""
from flask_frozen import Freezer
from app import app, load_json
import os
import shutil

# --- CRITICAL CONFIGURATION FOR GITHUB PAGES ---
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'CNAME']
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

freezer = Freezer(app)

@freezer.register_generator
def project_detail():
    """Tells Frozen-Flask about your dynamic project IDs"""
    projects_data = load_json('projects.json')
    for project in projects_data['projects']:
        yield {'project_id': project['id']}

@freezer.register_generator
def download_cv():
    """Exclude file download routes from freezing"""
    return
    yield

@freezer.register_generator
def view_cv():
    """Exclude file view routes from freezing"""
    return
    yield

if __name__ == '__main__':
    # Clean build directory
    if os.path.exists('build'):
        shutil.rmtree('build')
    
    print("Generating static files for GitHub Pages...")
    freezer.freeze()
    print("Done! Ready to push to GitHub.")