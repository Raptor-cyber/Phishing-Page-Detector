
# 🛡️ Megadriod PhishGuard

**Megadriod PhishGuard** is an intelligent phishing detection and link analysis platform developed by **Megadriod Cybersecurity Training Academy**. This web application provides an interactive, real-time tool to detect phishing attempts, analyze web links, and simulate red-team/blue-team cybersecurity training environments.

---

## 🌐 Live Demo

> [🔗 Launch Megadriod PhishGuard](https://your-host-url.com)  
> *(Replace with your hosted URL)*

---

## 🚀 Features

- ✅ **Phishing URL Detection**  
  Check if a URL is malicious using integrated phishing detection logic.

- 🔗 **Link Analysis**  
  Analyze embedded links from a web page or HTML snippet to identify threats.

- 📊 **Result History and Export**  
  Automatically saves your analysis history locally in the browser with an option to export as CSV.

- 📚 **Service Highlights**
  - Phishing Detection
  - Link Pattern Recognition
  - Threat Intelligence Integration
  - Security Consulting & Blog Updates

- 🧠 **Client Testimonials and Blog Sections**  
  Built-in trust-building testimonials and educational blog post layouts.

---

## 📁 File Structure

```
megadriod-phishguard/
├── index.html         # Main application interface
├── /api/              # Expected backend endpoints (not included in this repo)
│   ├── phishing-check
│   └── link-analysis
└── README.md
```

> 💡 This is a **frontend-only interface**. The phishing detection and link analysis logic are expected to be handled via POST requests to `/api/phishing-check` and `/api/link-analysis`.

---

## ⚙️ Installation & Hosting

1. **Download or Clone this Repository**
```bash
git clone https://github.com/megadriod/phishguard.git
cd phishguard
```

2. **Open in Browser**
   - Open `index.html` directly in your browser *(for UI demo only)*.
   - Or serve using a local server for API routing.

3. **Deploy to Hosting**
   - Upload to GitHub Pages, Netlify, Vercel, or any static file host.
   - For full functionality, deploy APIs (`/api/phishing-check`, `/api/link-analysis`) separately.

---

## 🛠️ Backend Integration (API)

> **NOTE:** This frontend calls `/api/phishing-check` and `/api/link-analysis`. You must create or connect to a backend that supports these endpoints.

### Example API Payloads:

- **POST /api/phishing-check**
```json
{ "url": "https://example.com" }
```

- **POST /api/link-analysis**
```json
{ "url": "https://example.com", "html": "<a href='...'>..." }
```

---

## 📞 Contact

- 📧 Email: [megadriodcyber@gmail.com](mailto:megadriodcyber@gmail.com)  
- 📞 Phone: +234 9019067253  
- 💬 WhatsApp: [Click to Chat](https://wa.me/2348134422262)  
- 🌍 Website: [https://megadriodcyber.wordpress.com](https://megadriodcyber.wordpress.com)

---

## 📜 License

This project is for educational use only under the **Creative Commons BY-NC 4.0 License**.  
Unauthorized phishing simulations or misuse of the code for real-world attacks are strictly prohibited.

---

## ✅ Acknowledgement

Developed by the **Megadriod Cybersecurity Training Academy** as part of its mission to educate and prepare red/blue teams across the globe.

> _"Empowering cyber defense through knowledge."_
