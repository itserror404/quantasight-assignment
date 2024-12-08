Full Stack Intern Assignment: QuantaSight
Subject: Search and Bookmark Web Application

Main Structure (non imp files skipped):

quantasight-assignment/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── SearchBar.vue      # Search input and filters
│   │   │   ├── SearchResult.vue   # Search result display with bookmark
│   │   │   └── BookmarkResult.vue # Bookmarked item display
│   │   ├── App.vue                # Main app component
│   │   └── main.js
│   ├── package.json
│   └── Dockerfile                 # Frontend Docker config
├── backend/
│   ├── app.py                     # Flask API endpoints
│   ├── data.json                  # Initial data
│   ├── requirements.txt           # Python dependencies
│   └── Dockerfile                 # Backend Docker config
├──  init.sql                   # Database schema
└──  README.md 

Instructions on how to Run:
1. Database Setup
psql -U postgres
CREATE DATABASE quanta;
\c quanta
\i init.sql

2. Backend Setup
cd backend
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
python app.py


3. Frontend Setup

cd frontend
npm install
npm run serve


OR

DOCKER SETUP:
Backend
cd backend
docker build -t backend .
docker run -p 5000:5000 backend

Frontend
cd frontend
docker build -t frontend .
docker run -p 8080:8080 frontend


Description of application structure and functionality:
Languages Used: Frontend: Javascript (Vue.js) and Backend: Python (Flask) Database: PSQL

Features
Search through articles, reports, and profiles
Filter results by category
View detailed information for each result
Bookmark items for later reference

API Endpoints
POST /search: Search with optional category filter
GET /bookmarks: Retrieve all bookmarked items
POST /bookmarks: Save a new bookmark


Challenges faced and how they were resolved:

Search Functionality Debug
Challenge: Couldn't see if search was working or returning results
Solution: Added debug prints in Flask backend to track search requests and responses

Bookmarks View Issue
Challenge: Bookmarks weren't showing up in the bookmarks view
Solution: Fixed the database column names (result_id → result) and corrected the SQL query joins

Component Button Logic
Challenge: Bookmark button was showing up in both search and bookmarks view
Solution: Created separate SearchResult.vue and BookmarkResult.vue components to handle different views

API Response Issues
Challenge: Getting 400 (BAD REQUEST) and 415 errors when fetching bookmarks
Solution: Added proper headers and fixed the API endpoint response formatting
