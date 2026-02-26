"""
Setup script to create all necessary data files for the portfolio
Updated with complete CV data as of February 19, 2026
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
    "title": "PhD Researcher | Earth & Atmospheric Sciences | Data-Driven Weather Forecasting",
    "email": "official.animesh7@gmail.com",
    "phone": "+91 9046567045",
    "location": "Rourkela, Odisha, India",
    "bio": "PhD researcher specializing in Earth and Atmospheric Sciences with expertise in data-driven weather forecasting, machine learning applications for climate science, and remote sensing. Currently developing advanced weather prediction systems using deep learning architectures and high-resolution reanalysis data. Strong background in drought monitoring, snow cover dynamics, air quality analysis, and mesoscale meteorological modeling.",
    "tagline": "Transforming Earth Observation Data into Actionable Climate Intelligence",
    "social": {
        "linkedin": "https://www.linkedin.com/in/animeshchoudhury/",
        "github": "https://github.com/AnimeshChoudhury",
        "scholar": "https://scholar.google.com/citations?user=0p-FbaoAAAAJ&hl=en",
        "researchgate": "https://www.researchgate.net/profile/Animesh-Choudhury"
    },
    "research_interests": [
        "Data-Driven Weather Forecasting",
        "Machine Learning for Climate Science",
        "Mesoscale Meteorological Modeling",
        "Drought Monitoring & Climate Analysis",
        "Remote Sensing & Earth Observation",
        "Deep Learning for Atmospheric Sciences",
        "Urban Climate & Heat Island Effects"
    ],
    "expertise": [
        "Weather Forecasting (Pangu-Weather, Deep Learning)",
        "WRF Mesoscale Modeling",
        "Machine Learning & Deep Learning",
        "Remote Sensing (MODIS, Sentinel, Landsat)",
        "Python & R Programming",
        "Google Earth Engine",
        "Climate Data Analysis"
    ]
}

with open('data/profile.json', 'w', encoding='utf-8') as f:
    json.dump(profile_data, f, indent=2)
print("✓ Created data/profile.json")

# 2. Create animesh_cv_data.json (Complete CV data)
cv_data = {
    "personal_info": {
        "name": "Animesh Choudhury",
        "title": "PhD Researcher | Earth & Atmospheric Sciences | Data-Driven Weather Forecasting",
        "email": "official.animesh7@gmail.com",
        "phone": "+91 9046567045",
        "date_of_birth": "29/05/1992",
        "nationality": "Indian",
        "gender": "Male",
        "linkedin": "https://www.linkedin.com/in/animeshchoudhury/",
        "github": "https://github.com/AnimeshChoudhury",
        "scholar": "https://www.researchgate.net/profile/Animesh-Choudhury",
        "google_scholar": "https://scholar.google.com/citations?user=0p-FbaoAAAAJ&hl=en",
        "address": "Pahartali, Ward No 9, Raghunathpur, Purulia, 723133, West Bengal, India"
    },
    "summary": "PhD researcher specializing in Earth and Atmospheric Sciences with expertise in data-driven weather forecasting, machine learning applications for climate science, and remote sensing. Currently developing advanced weather prediction systems using deep learning architectures and high-resolution reanalysis data at National Institute of Technology, Rourkela. Strong background in drought monitoring, snow cover dynamics, air quality analysis, and mesoscale meteorological modeling with 6+ years of research experience across premier institutions.",
    "education": [
        {
            "degree": "PhD in Earth and Atmospheric Sciences",
            "institution": "National Institute of Technology",
            "location": "Rourkela, India",
            "year": "2022 - Current",
            "website": "https://www.nitrkl.ac.in/"
        },
        {
            "degree": "Post Graduate Diploma in Remote Sensing & GIS",
            "institution": "Indian Institute of Remote Sensing (IIRS)",
            "location": "Dehradun, India",
            "year": "2017-2018",
            "website": "https://www.iirs.gov.in/"
        },
        {
            "degree": "M.Sc in Environmental Science",
            "institution": "Asutosh College, Calcutta University",
            "location": "Kolkata, India",
            "year": "2015-2017",
            "website": "https://www.asutoshcollege.in/"
        },
        {
            "degree": "B.Sc in Physics",
            "institution": "Raghunathpur College, Burdwan University",
            "location": "West Bengal, India",
            "year": "2009-2013",
            "website": "https://www.raghunathpurcollege.ac.in/"
        }
    ],
    "experience": [
        {
            "position": "Junior Research Fellow (PhD Researcher)",
            "organization": "National Institute of Technology",
            "location": "Rourkela, India",
            "period": "Feb 2022 - Jun 2025",
            "project": "Land-atmosphere interaction during thunderstorms over major urban areas of India using high-resolution mesoscale modeling framework and climatological data sets",
            "responsibilities": [
                "Developing data-driven weather forecasting systems using Pangu-Weather architecture and IMDAA reanalysis data",
                "Creating BharatBench dataset for ML-based weather forecasting over India",
                "Conducting high-resolution mesoscale modeling of urban thunderstorms using WRF",
                "Analyzing land-atmosphere interactions and urban heat island effects"
            ]
        },
        {
            "position": "Junior Research Fellow",
            "organization": "Department of Remote Sensing and GIS, Vidyasagar University",
            "location": "Midnapore, India",
            "period": "Jan 2020 - Feb 2022",
            "project": "Sub seasonal to Seasonal Forecast of Agricultural Drought and Estimation of Crop Yield Reduction using Machine Learning Approaches",
            "responsibilities": [
                "Long-term monitoring of droughts using satellite-based indices (SPEI, VCI, TCI)",
                "Developed ML models for prediction of agricultural droughts",
                "Analyzed regional variation of drought parameters across India",
                "Published research in Journal of Environmental Management"
            ]
        },
        {
            "position": "Junior Research Fellow",
            "organization": "DST-Mahamana Centre of Excellence in Climate Change Research, BHU",
            "location": "Varanasi, India",
            "period": "Jun 2019 - Jan 2020",
            "project": "Air Quality Monitoring over Indo-Gangetic Plain",
            "responsibilities": [
                "Analyzed horizontal and vertical distribution of air pollutants using CALIPSO LIDAR",
                "Observed aerosol transport patterns over Indo-Gangetic plain",
                "Integrated ground-based and satellite observations for air quality assessment"
            ]
        },
        {
            "position": "Junior Research Fellow",
            "organization": "Indian Institute of Remote Sensing (IIRS)",
            "location": "Dehradun, India",
            "period": "Oct 2018 - Mar 2019",
            "project": "EOAM: Monitoring and Assessment of Mountain Eco-System and Services in NW Himalayas",
            "responsibilities": [
                "Snow cover area mapping of Northwest Himalaya using MODIS, Sentinel, Landsat",
                "Utilized Google Earth Engine for large-scale geospatial analysis",
                "Installation and supervision of automatic weather stations (AWS)",
                "Published research in Remote Sensing journal (145+ citations)"
            ]
        },
        {
            "position": "Junior Research Fellow",
            "organization": "CSIR - Institute of Himalayan Bioresource Technology",
            "location": "Palampur, India",
            "period": "Aug 2018 - Oct 2018",
            "project": "Preparation of Spectral Library of Forest tree species found in Himalayan Region",
            "responsibilities": [
                "Collected spectral signatures using ASD Fieldspec spectroradiometer",
                "Correlated spectral data with bio-physical parameters",
                "Classified tree species using satellite-based hyperspectral data"
            ]
        }
    ],
    "publications": [
        {
            "title": "Development of a Data-driven weather forecasting system over India with Pangu-Weather architecture and IMDAA reanalysis Data",
            "authors": "Choudhury, A., & Panda, J.",
            "venue": "In Preparation",
            "year": 2025,
            "citations": 0,
            "type": "journal",
            "doi": ""
        },
        {
            "title": "BharatBench: Dataset for data-driven weather forecasting over India",
            "authors": "Choudhury, A., Panda, J., & Mukherjee, A.",
            "venue": "In Preparation",
            "year": 2024,
            "citations": 0,
            "type": "journal",
            "doi": ""
        },
        {
            "title": "Analyzing urban footprints over four coastal cities of India and the association with rainfall and temperature using deep learning models",
            "authors": "Mukherjee, A., Panda, J., Choudhury, A., Singh, S., & Bhattacharyya, S.",
            "venue": "Urban Climate",
            "year": 2024,
            "citations": 0,
            "type": "journal",
            "doi": "https://doi.org/10.1016/j.uclim.2024.102123"
        },
        {
            "title": "Analysis and Forecasting of Temporal Rainfall Variability Over Hundred Indian Cities Using Deep Learning Approaches",
            "authors": "Singh, S., Mukherjee, A., Panda, J. et al.",
            "venue": "Earth Systems and Environment",
            "year": 2024,
            "citations": 0,
            "type": "journal",
            "doi": "https://doi.org/10.1007/s41748-024-00380-2"
        },
        {
            "title": "Drought trend and its association with land surface temperature (LST) over homogeneous drought regions of India (2001–2019)",
            "authors": "Choudhury, A.",
            "venue": "Discover Water",
            "year": 2024,
            "citations": 0,
            "type": "journal",
            "doi": "https://doi.org/10.1007/s43832-024-00089-4"
        },
        {
            "title": "Urban Heat: UHI and Heat Stress Threat to Megacities",
            "authors": "Panda, J., Mukherjee, A., Choudhury, A., Biswas, S.",
            "venue": "Climate Crisis: Adaptive Approaches and Sustainability. Springer",
            "year": 2023,
            "citations": 0,
            "type": "book_chapter",
            "doi": "https://doi.org/10.1007/978-3-031-28728-2"
        },
        {
            "title": "Transport of a severe dust storm from Middle East to Indian region and its impact on surrounding environment",
            "authors": "Budakoti, S., Singh, C. & Choudhury, A.",
            "venue": "International Journal of Environmental Science and Technology",
            "year": 2022,
            "citations": 89,
            "type": "journal",
            "doi": "https://doi.org/10.1007/s13762-022-04520-1"
        },
        {
            "title": "Regional variation of drought parameters and long-term trends over India using standardized precipitation evapotranspiration index",
            "authors": "Choudhury, A., Dutta, D., Bera, D., Kundu, A.",
            "venue": "Journal of Environmental Management",
            "year": 2021,
            "citations": 203,
            "type": "journal",
            "doi": "https://doi.org/10.1016/j.jenvman.2021.113056"
        },
        {
            "title": "A Response of Snow Cover to the Climate in the Northwest Himalaya (NWH) Using Satellite Products",
            "authors": "Choudhury A, Yadav AC, Bonafoni S",
            "venue": "Remote Sensing",
            "year": 2021,
            "citations": 145,
            "type": "journal",
            "doi": "https://doi.org/10.3390/rs13040655"
        }
    ],
    "conference_papers": [
        {
            "title": "A Step Towards Building Medium-Range Data-Driven Weather Forecasting System Over India",
            "venue": "IEEE Conference",
            "year": 2024,
            "url": "https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10984239"
        },
        {
            "title": "Monitoring of Surface Water of East Kolkata Wetlands (1984-2015) with Global Surface Water Dataset",
            "venue": "ACRS 2020",
            "year": 2020,
            "url": "https://a-a-r-s.org/proceeding/ACRS2020/yi3x7w.pdf"
        },
        {
            "title": "Role of Earth Observation Data and Hydrological Modeling in Supporting UN SDGs in North West Himalaya",
            "venue": "ISPRS Archives",
            "year": 2020,
            "url": "https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLIII-B3-2020/853/2020/"
        },
        {
            "title": "Simulation of an Extreme Dust Episode using WRF-CHEM",
            "venue": "IASTA 2018",
            "year": 2018,
            "url": "https://cas.iitd.ac.in/iasta2018/pdf/E-Proceedings_IASTA-2018.pdf"
        }
    ],
    "skills": {
        "Weather & Climate Modeling": ["WRF-CHEM", "Pangu-Weather", "Mesoscale Modeling", "IMDAA Reanalysis"],
        "Machine Learning & AI": ["Deep Learning", "TensorFlow", "PyTorch", "Time Series Forecasting", "Neural Networks"],
        "Remote Sensing": ["MODIS", "Sentinel", "Landsat", "SNAP", "ENVI", "Idrisi", "Hyperspectral Analysis"],
        "GIS & Geospatial": ["Google Earth Engine", "ArcGIS", "QGIS", "Spatial Analysis"],
        "Programming & Data Science": ["Python", "R", "SQL", "Data Visualization", "Big Data Processing"],
        "Climate Analysis": ["Drought Monitoring", "SPEI/VCI Indices", "Climate Trends", "Snow Cover Analysis"]
    },
    "languages": {
        "Bengali": "Native",
        "English": "Fluent (C2)",
        "Hindi": "Fluent (C2 Speaking, B2 Reading/Writing)"
    },
    "awards": [
        {
            "name": "Poster Presentation at AOGS 2025",
            "organization": "22nd Annual Meeting of Asia Oceania Geosciences Society, Singapore",
            "year": 2025,
            "description": "Regional Data-driven Weather Forecasting Over India with Pangu-weather Architecture"
        },
        {
            "name": "National Symposium Participation",
            "organization": "Tropment-2024, Indian Meteorological Society, NIT Rourkela",
            "year": 2024
        },
        {
            "name": "Organizing Member and Speaker",
            "organization": "National Workshop on Drought Monitoring, Vidyasagar University",
            "year": 2021
        },
        {
            "name": "Poster Presentation at AAPW-5",
            "organization": "Asian Air Pollution Workshop",
            "year": 2019,
            "description": "Aerosol vertical distribution over lower Gangetic plain using CALIPSO LIDAR"
        }
    ],
    "training": [
        {
            "name": "Recent Trends in Time Series Forecasting using Deep Learning Models",
            "organization": "NIT Rourkela",
            "period": "Dec 25-29, 2023"
        },
        {
            "name": "Deep Learning Application for Smart Cities",
            "organization": "NIT Rourkela",
            "period": "Sep 11-15, 2023"
        },
        {
            "name": "Machine Learning in Weather & Climate (MOOC)",
            "organization": "ECMWF in partnership with IFAB",
            "period": "Jan-Apr 2023"
        },
        {
            "name": "WRF Modeling System - Capacity Building Training",
            "organization": "C-DAC and SAMA (National Supercomputing Mission)",
            "period": "Apr 3-20, 2023"
        },
        {
            "name": "Open Classroom: Atmospheric and Climate Sciences",
            "organization": "SAMA & SRM Institute",
            "period": "Apr 7-24, 2023"
        },
        {
            "name": "Geospatial Modeling Driven Urban Hazard and Risk Analysis",
            "organization": "IIRS, Dehradun",
            "period": "Feb 13-17, 2023"
        },
        {
            "name": "Machine Learning and Deep Learning for Earth Observation",
            "organization": "DA-IITC & SAC, ISRO",
            "period": "Aug 9-13, 2021"
        }
    ]
}

with open('data/animesh_cv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cv_data, f, indent=2)
print("✓ Created data/animesh_cv_data.json")

print("=" * 60)
print("✓ All data files created successfully!")
print("\nData Summary:")
print(f"  • Publications: {len(cv_data['publications'])} journal papers")
print(f"  • Conference Papers: {len(cv_data['conference_papers'])} proceedings")
print(f"  • Experience: {len(cv_data['experience'])} positions")
print(f"  • Education: {len(cv_data['education'])} degrees")
print(f"  • Training: {len(cv_data['training'])} programs")
print(f"  • Awards: {len(cv_data['awards'])} recognitions")
print("\nYou can now run: python app.py")
print("Visit: http://localhost:5000")
