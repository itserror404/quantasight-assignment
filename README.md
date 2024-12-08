# Full Stack Intern Assignment: QuantaSight
## Subject: Search and Bookmark Web Application

### Main Structure (non imp files skipped):
<img width="476" alt="Screenshot 2024-12-08 at 5 58 29 PM" src="https://github.com/user-attachments/assets/ab23226f-c451-429c-b456-8212f5ffa31a">


### Instructions on how to Run:
#### 1. Database Setup
```psql -U postgres
CREATE DATABASE quanta;
\c quanta
\i init.sql

```

#### 2. Backend Setup
```cd backend
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
python app.py
```


#### 3. Frontend Setup
```
cd frontend
npm install
npm run serve
```

### OR

#### DOCKER SETUP:
##### Backend
```
cd backend
docker build -t backend .
docker run -p 5000:5000 backend
```

##### Frontend
```
cd frontend
docker build -t frontend .
docker run -p 8080:8080 frontend
```

### Description of application structure and functionality:
#### Languages Used: Frontend: Javascript (Vue.js) and Backend: Python (Flask) Database: PSQL

#### Features
Search through articles, reports, and profiles
Filter results by category
View detailed information for each result
Bookmark items for later reference

#### API Endpoints
POST /search: Search with optional category filter
GET /bookmarks: Retrieve all bookmarked items
POST /bookmarks: Save a new bookmark


### Challenges faced and how they were resolved:

#### 1. Search Functionality Debug
Challenge: Couldn't see if search was working or returning results
Solution: Added debug prints in Flask backend to track search requests and responses

#### 2. Bookmarks View Issue
Challenge: Bookmarks weren't showing up in the bookmarks view
Solution: Fixed the database column names (result_id → result) and corrected the SQL query joins

#### 3. Component Button Logic
Challenge: Bookmark button was showing up in both search and bookmarks view
Solution: Created separate SearchResult.vue and BookmarkResult.vue components to handle different views

#### 4. API Response Issues
Challenge: Getting 400 (BAD REQUEST) and 415 errors when fetching bookmarks
Solution: Added proper headers and fixed the API endpoint response formatting


### Screenshots
#### Main Screen
<img width="1259" alt="Screenshot 2024-12-08 at 5 32 21 PM" src="https://github.com/user-attachments/assets/398a6779-2b73-4976-9653-4e7cdf2f09aa">

#### Searching
<img width="1259" alt="Screenshot 2024-12-08 at 5 32 30 PM" src="https://github.com/user-attachments/assets/9905142f-14fb-480a-b130-f376c0054d84">

#### View Details
<img width="1259" alt="Screenshot 2024-12-08 at 5 32 35 PM" src="https://github.com/user-attachments/assets/e2ed418c-499e-4f6d-86a8-ce2f12fd00f2">

#### Bookmarks
<img width="1259" alt="Screenshot 2024-12-08 at 5 32 47 PM" src="https://github.com/user-attachments/assets/2d7bfeb5-b9ef-410e-b2b9-34e976e40daa">





