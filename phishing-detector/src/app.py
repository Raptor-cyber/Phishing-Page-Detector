import os
from flask import Flask, request, jsonify, render_template
from detector.phishing_detector import PhishingDetector
from analysis.link_analysis import LinkAnalysis
import requests

app = Flask(__name__)
app.secret_key = os.environ.get("MEGADRIOD_PHISHGUARD_SECRET", "change_this_secret_key")
phishing_detector = PhishingDetector()
link_analysis = LinkAnalysis()

@app.route('/api/phishing-check', methods=['POST'])
def detect_phishing():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error': 'No URL provided.'}), 400
    is_phishing = phishing_detector.detect_phishing(url)
    return jsonify({'url': url, 'is_phishing': is_phishing})

@app.route('/api/link-analysis', methods=['POST'])
def analyze_links():
    data = request.json
    html = data.get('html')
    url = data.get('url')
    if url and not html:
        try:
            resp = requests.get(url, timeout=5)
            html = resp.text
        except Exception as e:
            return jsonify({'error': f'Failed to fetch URL: {str(e)}'}), 400
    if not html:
        return jsonify({'error': 'No HTML content provided.'}), 400
    results = link_analysis.analyze_links(html)
    return jsonify({'results': results})

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Do NOT use debug=True in production!
    app.run(host='0.0.0.0', port=5000)