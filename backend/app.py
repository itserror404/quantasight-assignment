from flask import Flask
from flask import request, jsonify
import json
from flask_cors import CORS 
import psycopg2
    
app = Flask(__name__)
CORS(app)


def get_db_connection():
    return psycopg2.connect(
        dbname="quanta",
        user="postgres",
        password="hello",
        host="localhost"
    )


def load_data():
    conn = get_db_connection()
    cur = conn.cursor()
    
    
    cur.execute("SELECT COUNT(*) FROM results")
    count = cur.fetchone()[0]
    
    if count > 0:
        print("Data already exists, skipping load")
        cur.close()
        conn.close()
        return
    
    
    with open('/Users/maimunaz/quantasight-assignment/backend/data.json', 'r') as file:
        
        data = json.load(file)
        print(data[0])
        
    for item in data:
        cur.execute("""
            INSERT INTO results (title, description, category, author, published_date, url)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            item.get('title', ''),
            item.get('description', ''),
            item.get('category', ''),
            item.get('author', ''),
            item.get('published_date', None),
            item.get('url', '')
        ))


    conn.commit()
    print("Data Loaded.")
    cur.close()
    conn.close()


@app.route('/')
def show_allresults():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM results")
    rows= cur.fetchall()
    
    results = []
    for row in rows:
            results.append({
                'id': row[0],
                'title': row[1],
                'description': row[2],
                'category': row[3],
                'author': row[4],
                'published_date': str(row[5]),  
                'url': row[6]
            })
            
    all_results = []  
    for r in results:
        all_results.append(r) 
        
    cur.close()
    conn.close()
    
    return jsonify(all_results)

    


# search from the given data
@app.route('/search', methods=['POST'])
def search():
    
    data = request.json
    
    search_term = data.get('searchTerm', '').lower()
    category = data.get('category', '')
    
    print(f"Search term: {search_term}, Category: {category}")  
    
    conn = get_db_connection()
    cur = conn.cursor() 
    
    if category:
        cur.execute("""
            SELECT * FROM results 
            WHERE category = %s
            AND (title ILIKE %s OR description ILIKE %s)
        """, (category, f'%{search_term}%', f'%{search_term}%'))
    else:
        cur.execute("""
            SELECT * FROM results 
            WHERE title ILIKE %s OR description ILIKE %s
        """, (f'%{search_term}%', f'%{search_term}%'))
    
    results = cur.fetchall()
    r = []
    for i in results:
        r.append({
            'id': i[0],
            'title': i[1],
            'description': i[2],
            'category': i[3],
            'author': i[4],
            'published_date': str(i[5]),
            'url': i[6]
        })
    
    cur.close()
    conn.close() 
    return jsonify(r)


#save to bookmarks from the given data
@app.route('/bookmarks', methods=['POST'])
def savebookmarks():
    data = request.json
    result_id = data.get('result_id')
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    
    
    cur.execute("""
        INSERT INTO bookmarked_results (result, time_bookmarked)
        VALUES (%s, CURRENT_TIMESTAMP)
        RETURNING id
    """, (result_id,))
    
    bookmark_id = cur.fetchone()[0]
    conn.commit()
    
    cur.close()
    conn.close()
    return jsonify({"message": "Bookmark added", "id": bookmark_id}), 201
        

#fetch bookmarks
@app.route('/bookmarks', methods=['GET'])
def fetchbookmarks():

    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("""
            SELECT r.* FROM results r
            JOIN bookmarked_results br ON r.id = br.result
            ORDER BY br.time_bookmarked DESC;
        """)
        
        bookmarks = cur.fetchall()
        
        book = []
        for b in bookmarks:
            book.append({
                'id': b[0],
                'title': b[1],
                'description': b[2],
                'category': b[3],
                'author': b[4],
                'published_date': str(b[5]),
                'url': b[6]
            })
        
        return jsonify(book)
    
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500
    
    finally:
        cur.close()
        conn.close()

       

if __name__ == '__main__':
    load_data()
    app.run(debug=True)
    
    