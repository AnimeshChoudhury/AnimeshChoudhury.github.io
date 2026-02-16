"""
Setup script to create all necessary data files for the portfolio
Run this once after downloading the portfolio folder
"""

import json
import os

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

print("Creating portfolio data files...")
print("=" * 60)

# 1. Create profile.json
profile_data = {
    "name": "Animesh Choudhury",
    "title": "Junior Research Fellow | Remote Sensing & GIS Specialist",
    "email": "official.animesh7@gmail.com",
    "phone": "+91 9046567045",
    "location": "Purulia, West Bengal, India",
    "bio": "Accomplished researcher specializing in Remote Sensing, GIS, and Climate Science with extensive experience in satellite data analysis, machine learning applications for environmental monitoring, and geospatial modeling. Strong background in drought monitoring, snow cover mapping, air quality analysis, and land-atmosphere interactions. Proficient in Python, R, Google Earth Engine, and various remote sensing tools.",
    "tagline": "Transforming Earth Observation Data into Actionable Insights",
    "social": {
        "linkedin": "https://www.linkedin.com/in/animeshchoudhury/",
        "github": "https://github.com/AnimeshChoudhury",
        "scholar": "https://scholar.google.com/citations?user=0p-FbaoAAAAJ&hl=en",
        "researchgate": "https://www.researchgate.net/profile/Animesh-Choudhury"
    },
    "research_interests": [
        "Remote Sensing & Earth Observation",
        "Drought Monitoring & Climate Analysis",
        "Snow Cover Dynamics & Hydrology",
        "Machine Learning for Environmental Prediction",
        "Agricultural Remote Sensing",
        "Air Quality & Atmospheric Science",
        "Geospatial Data Analysis"
    ],
    "expertise": [
        "Satellite Data Analysis",
        "Machine Learning & AI",
        "GIS & Spatial Analysis",
        "Climate Modeling",
        "Python Programming",
        "Google Earth Engine"
    ]
}

with open('data/profile.json', 'w', encoding='utf-8') as f:
    json.dump(profile_data, f, indent=2)
print("✓ Created data/profile.json")

# 2. Create animesh_cv_data.json (CV data)
cv_data = {
    "personal_info": {
        "name": "Animesh Choudhury",
        "title": "Junior Research Fellow | Remote Sensing & GIS Specialist",
        "email": "official.animesh7@gmail.com",
        "phone": "+91 9046567045",
        "date_of_birth": "29 May 1992",
        "nationality": "Indian",
        "linkedin": "https://www.linkedin.com/in/animeshchoudhury/",
        "github": "https://github.com/AnimeshChoudhury",
        "scholar": "https://www.researchgate.net/profile/Animesh-Choudhury",
        "google_scholar": "https://scholar.google.com/citations?user=0p-FbaoAAAAJ&hl=en",
        "address": "Pahartali, Ward No 9 Raghunathpur, Purulia, 723133 West Bengal, India"
    },
    "summary": "Accomplished researcher specializing in Remote Sensing, GIS, and Climate Science with extensive experience in satellite data analysis, machine learning applications for environmental monitoring, and geospatial modeling. Strong background in drought monitoring, snow cover mapping, air quality analysis, and land-atmosphere interactions. Proficient in Python, R, Google Earth Engine, and various remote sensing tools.",
    "education": [
        {
            "degree": "PGD (Post Graduate Diploma) in Remote Sensing and GIS",
            "institution": "Indian Institute of Remote Sensing (IIRS)",
            "location": "India",
            "year": "2017-2018"
        },
        {
            "degree": "M.Sc in Environmental Science",
            "institution": "Asutosh College, Calcutta University",
            "location": "India",
            "year": "2015-2017"
        },
        {
            "degree": "B.Sc in Physics",
            "institution": "Raghunathpur College, Burdwan University",
            "location": "India",
            "year": "2009-2013"
        }
    ],
    "experience": [
        {
            "position": "Junior Research Fellow",
            "organization": "National Institute of Technology",
            "location": "Rourkela, India",
            "period": "Feb 2022 - Present",
            "responsibilities": [
                "Conducting research on land-atmosphere interaction during thunderstorms over major urban areas of India",
                "Utilizing high-resolution mesoscale modeling framework and climatological datasets"
            ]
        },
        {
            "position": "Junior Research Fellow",
            "organization": "Department of Remote Sensing and GIS, Vidyasagar University",
            "location": "Midnapore, India",
            "period": "Jan 2020 - Feb 2022",
            "responsibilities": [
                "Developed ML models for prediction of agricultural droughts",
                "Conducted long-term monitoring of droughts using satellite-based indices"
            ]
        },
        {
            "position": "Junior Research Fellow",
            "organization": "DST-Mahamana Centre of Excellence in Climate Change Research, BHU",
            "location": "Varanasi, India",
            "period": "Jun 2019 - Jan 2020",
            "responsibilities": [
                "Analyzed horizontal and vertical distribution of air pollutants over Indo-Gangetic plain"
            ]
        },
        {
            "position": "Junior Research Fellow",
            "organization": "Indian Institute of Remote Sensing (IIRS)",
            "location": "Dehradun, India",
            "period": "Oct 2018 - Mar 2019",
            "responsibilities": [
                "Mapped snow cover area of Northwest Himalaya using MODIS, Sentinel, and Landsat datasets"
            ]
        },
        {
            "position": "Junior Research Fellow",
            "organization": "CSIR - Institute of Himalayan Bioresource Technology",
            "location": "Palampur, India",
            "period": "Aug 2018 - Oct 2018",
            "responsibilities": [
                "Created spectral library of forest tree species found in Himalayan Region"
            ]
        }
    ],
    "publications": [
        {
            "title": "A Response of Snow Cover to the Climate in the Northwest Himalaya (NWH) Using Satellite Products",
            "authors": "Choudhury A, Yadav AC, Bonafoni S",
            "venue": "Remote Sensing",
            "year": 2021,
            "citations": 145,
            "type": "journal",
            "doi": "https://doi.org/10.3390/rs13040655"
        },
        {
            "title": "Regional variation of drought parameters and long-term trends over India using standardized precipitation evapotranspiration index",
            "authors": "Choudhury A, Dutta D, Bera D, Kundu A",
            "venue": "Journal of Environmental Management",
            "year": 2021,
            "citations": 203,
            "type": "journal",
            "doi": "https://doi.org/10.1016/j.jenvman.2021.113056"
        },
        {
            "title": "Transport of a severe dust storm from Middle East to Indian region and its impact on surrounding environment",
            "authors": "Budakoti S, Singh C, Choudhury A",
            "venue": "International Journal of Environmental Science and Technology",
            "year": 2022,
            "citations": 89,
            "type": "journal",
            "doi": "https://doi.org/10.1007/s13762-022-04520-1"
        }
    ],
    "conference_papers": [
        {
            "title": "Simulation of an Extreme Dust Episode using WRF-CHEM",
            "venue": "IASTA 2018",
            "year": 2018,
            "url": "https://cas.iitd.ac.in/iasta2018/pdf/E-Proceedings_IASTA-2018.pdf"
        },
        {
            "title": "Role of Earth Observation Data and Hydrological Modeling in Supporting UN SDGs in North West Himalaya",
            "venue": "ISPRS Archives",
            "year": 2020,
            "url": "https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLIII-B3-2020/853/2020/"
        }
    ],
    "skills": {
        "Remote Sensing Tools": ["ENVI", "SNAP", "Idrisi", "ERDAS Imagine"],
        "GIS Software": ["ArcGIS", "QGIS", "Google Earth Engine"],
        "Programming": ["Python", "R", "SQL", "MySQL"],
        "Data Science & ML": ["Machine Learning", "Deep Learning", "Data Analysis"],
        "Domain Expertise": ["Drought Monitoring", "Snow Cover Mapping", "Air Quality Analysis"],
        "Other Tools": ["WRF-CHEM", "MODIS", "Sentinel", "Landsat"]
    },
    "languages": {
        "Bengali": "Native",
        "English": "Fluent (C2)",
        "Hindi": "Fluent (C2 Speaking, B2 Reading/Writing)"
    },
    "awards": [
        {
            "name": "Organizing Member and Speaker",
            "organization": "National Workshop on Drought Monitoring",
            "year": 2021
        }
    ],
    "service": [
        "Poster presentation at Asian Air Pollution Workshop (AAPW-5), November 2019",
        "Attended webinar on Geospatial Techniques in Drought Characterization, September 2020"
    ]
}

with open('data/animesh_cv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cv_data, f, indent=2)
print("✓ Created data/animesh_cv_data.json")

# 3. Projects data is already created in the data folder

print("=" * 60)
print("✓ All data files created successfully!")
print("\nYou can now run: python app.py")
print("Visit: http://localhost:5000")
