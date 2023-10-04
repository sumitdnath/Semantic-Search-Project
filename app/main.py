from flask import Flask, request, jsonify
from search import semantic_search

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400

    # Perform semantic search
    results = semantic_search(query)

    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
