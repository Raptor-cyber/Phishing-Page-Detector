import os
from flask import Flask, request, jsonify, render_template
# from detector.phishing_detector import PhishingDetector
import sys
import importlib

PhishingDetector = None
try:
    phishing_detector_module = importlib.import_module("detector.phishing_detector")
    PhishingDetector = phishing_detector_module.PhishingDetector
except ModuleNotFoundError:
    try:
        phishing_detector_module = importlib.import_module("phishing_detector")
        PhishingDetector = phishing_detector_module.PhishingDetector
    except ModuleNotFoundError:
        raise ImportError(
            "Could not import 'PhishingDetector' from either 'detector.phishing_detector' or 'phishing_detector'. "
            "Please ensure the file exists and is in the correct location."
        )
LinkAnalysis = None
try:
    link_analysis_module = importlib.import_module("analysis.link_analysis")
    LinkAnalysis = link_analysis_module.LinkAnalysis
except ModuleNotFoundError:
    try:
        link_analysis_module = importlib.import_module("link_analysis")
        LinkAnalysis = link_analysis_module.LinkAnalysis
    except ModuleNotFoundError:
        raise ImportError(
            "Could not import 'LinkAnalysis' from either 'analysis.link_analysis' or 'link_analysis'. "
            "Please ensure the file exists and is in the correct location."
        )
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