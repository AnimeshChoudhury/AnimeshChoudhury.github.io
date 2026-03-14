# Netlify Deployment Fix TODO

## Steps:
- [x] Update runtime.txt to 'python 3.12.5'
- [x] Edit netlify.toml: remove [build.environment].PYTHON_VERSION
- [ ] User: git add . && git commit -m "Fix Netlify Python version (python 3.12.5)" && git push"
- [ ] Verify Netlify deploy logs show success (installs Python, pip deps, runs build_static.py)
- [x] Task complete: Changes ready for deploy

Status: ✅ Final fix: runtime.txt → 'python-3.11.6' (correct Netlify/mise format). Push to deploy!
