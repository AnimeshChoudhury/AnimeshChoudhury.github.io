"""
Build static version for Netlify deployment
"""
from flask_frozen import Freezer
from app import app, load_json
import os
import shutil

# Configuration
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'build'

freezer = Freezer(app)

# Register dynamic routes
@freezer.register_generator
def project_detail():
    projects_data = load_json('projects.json')
    for project in projects_data['projects']:
        yield {'project_id': project['id']}

if __name__ == '__main__':
    # Clean and build
    if os.path.exists('build'):
        shutil.rmtree('build')
    
    print("Building static site...")
    freezer.freeze()
    
    # Create .nojekyll
    with open('build/.nojekyll', 'w') as f:
        pass
    
    print("Build complete!")