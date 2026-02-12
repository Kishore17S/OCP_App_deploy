from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

# In-memory vote storage (in production, use Redis or a database)
votes = {
    'python': 0,
    'javascript': 0
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/vote', methods=['POST'])
def vote():
    data = request.get_json()
    choice = data.get('choice')
    
    if choice in votes:
        votes[choice] += 1
        return jsonify({
            'success': True,
            'votes': votes
        })
    
    return jsonify({
        'success': False,
        'error': 'Invalid choice'
    }), 400

@app.route('/api/results')
def results():
    total = sum(votes.values())
    return jsonify({
        'votes': votes,
        'total': total,
        'percentages': {
            'python': round((votes['python'] / total * 100) if total > 0 else 0, 1),
            'javascript': round((votes['javascript'] / total * 100) if total > 0 else 0, 1)
        }
    })

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
