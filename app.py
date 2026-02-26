"""
Animesh Choudhury - Personal Portfolio Website
Flask application for a creative, multi-page portfolio
"""

from flask import Flask, render_template, request, jsonify, send_from_directory
import json
import os
from datetime import datetime

app = Flask(__name__)

# --- GITHUB PAGES CONFIGURATION ---
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'build'
# This ensures that /about/ becomes about/index.html instead of about.html
app.config['FREEZER_REMOVE_EXTRA_SCHEMES'] = False 
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'

# Load data
def load_json(filename):
    """Load JSON data file"""
    filepath = os.path.join('data', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

# --- ROUTES WITH TRAILING SLASHES ---
# Adding the trailing slash / is critical for static hosting.

@app.route('/')
def index():
    """Home page"""
    profile = load_json('profile.json')
    projects = load_json('projects.json')['projects'][:3]
    return render_template('index.html', 
                         profile=profile, 
                         featured_projects=projects,
                         current_year=datetime.now().year)

@app.route('/about/')
def about():
    """About page with detailed bio"""
    profile = load_json('profile.json')
    cv_data = load_json('animesh_cv_data.json')
    return render_template('about.html', 
                         profile=profile,
                         experience=cv_data['experience'],
                         education=cv_data['education'],
                         skills=cv_data['skills'],
                         languages=cv_data.get('languages', {}),
                         current_year=datetime.now().year)

@app.route('/projects/')
def projects():
    """Projects showcase page"""
    profile = load_json('profile.json')
    all_projects = load_json('projects.json')['projects']
    
    category = request.args.get('category', 'all')
    if category != 'all':
        filtered_projects = [p for p in all_projects if p['category'] == category]
    else:
        filtered_projects = all_projects
    
    categories = list(set(p['category'] for p in all_projects))
    
    return render_template('projects.html',
                         profile=profile,
                         projects=filtered_projects,
                         categories=categories,
                         current_category=category,
                         current_year=datetime.now().year)

@app.route('/project/<project_id>/')
def project_detail(project_id):
    """Individual project detail page"""
    profile = load_json('profile.json')
    all_projects = load_json('projects.json')['projects']
    
    project = next((p for p in all_projects if p['id'] == project_id), None)
    
    if not project:
        return render_template('404.html', profile=profile), 404
    
    return render_template('project_detail.html',
                         profile=profile,
                         project=project,
                         current_year=datetime.now().year)

@app.route('/publications/')
def publications():
    """Publications page"""
    profile = load_json('profile.json')
    cv_data = load_json('animesh_cv_data.json')
    
    pubs = sorted(cv_data['publications'], 
                 key=lambda x: x.get('year', 0), 
                 reverse=True)
    
    conf_papers = cv_data.get('conference_papers', [])
    
    return render_template('publications.html',
                         profile=profile,
                         publications=pubs,
                         conference_papers=conf_papers,
                         current_year=datetime.now().year)

@app.route('/contact/')
def contact():
    """Contact page"""
    profile = load_json('profile.json')
    return render_template('contact.html',
                         profile=profile,
                         current_year=datetime.now().year)

# API routes aren't used in static builds but kept for local dev
@app.route('/api/contact', methods=['POST'])
def handle_contact():
    data = request.get_json()
    return jsonify({'success': True, 'message': 'Contact form received'})

@app.route('/download-cv/')
def download_cv():
    return send_from_directory('static/files', 
                             'Animesh_Choudhury_CV.pdf',
                             as_attachment=True)

@app.route('/view-cv/')
def view_cv():
    return send_from_directory('static/files', 
                             'Animesh_Choudhury_CV.pdf')

@app.errorhandler(404)
def page_not_found(e):
    profile = load_json('profile.json')
    return render_template('404.html', profile=profile), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)