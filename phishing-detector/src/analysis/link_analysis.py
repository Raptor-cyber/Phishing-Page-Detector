from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

class LinkAnalysis:
    def analyze_links(self, page_content):
        """
        Extracts all links from the HTML content and analyzes each for phishing indicators.
        Returns a list of dictionaries with analysis results for each link.
        """
        links = self.extract_links(page_content)
        analysis_results = []
        for link in links:
            result = self.analyze_link_safety(link)
            analysis_results.append(result)
        return analysis_results

    def extract_links(self, page_content):
        """
        Uses BeautifulSoup to extract all href links from the HTML content.
        Returns a list of URLs.
        """
        soup = BeautifulSoup(page_content, "html.parser")
        links = []
        for tag in soup.find_all("a", href=True):
            links.append(tag["href"])
        return links

    def analyze_link_safety(self, link):
        """
        Analyzes a single link for common phishing indicators.
        Returns a dictionary with the link, its safety status, and reasons.
        """
        reasons = []
        is_safe = True

        if self.has_ip_address(link):
            is_safe = False
            reasons.append("URL uses an IP address instead of a domain.")

        if len(link) > 75:
            is_safe = False
            reasons.append("URL is unusually long.")

        if '@' in link:
            is_safe = False
            reasons.append("URL contains '@' symbol.")

        if self.has_multiple_subdomains(link):
            is_safe = False
            reasons.append("URL has multiple subdomains.")

        if self.has_suspicious_keywords(link):
            is_safe = False
            reasons.append("URL contains suspicious keywords (e.g., 'login', 'secure', 'update').")

        if not link.startswith("https://"):
            is_safe = False
            reasons.append("URL does not use HTTPS.")

        if self.has_punycode(link):
            is_safe = False
            reasons.append("URL uses punycode encoding (possible IDN homograph attack).")

        if self.has_suspicious_tld(link):
            is_safe = False
            reasons.append("URL uses a suspicious top-level domain (TLD).")

        if self.has_suspicious_extension(link):
            is_safe = False
            reasons.append("URL ends with a suspicious file extension (e.g., .exe, .scr, .zip).")

        if self.uses_url_shortener(link):
            is_safe = False
            reasons.append("URL uses a known URL shortener service.")

        return {
            "url": link,
            "is_safe": is_safe,
            "reasons": reasons if reasons else ["No obvious phishing indicators detected."]
        }

    def has_ip_address(self, url):
        """
        Returns True if the URL uses an IP address instead of a domain name.
        """
        try:
            hostname = urlparse(url).hostname
            if hostname:
                # IPv4 pattern
                if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", hostname):
                    return True
                # IPv6 pattern
                if re.match(r"^\[?[A-F0-9]*:[A-F0-9:]+\]?$", hostname, re.I):
                    return True
        except Exception:
            pass
        return False

    def has_multiple_subdomains(self, url):
        """
        Returns True if the URL has more than two subdomains.
        """
        try:
            hostname = urlparse(url).hostname
            if hostname:
                parts = hostname.split('.')
                # e.g., sub.sub.domain.com -> 4 parts
                return len(parts) > 3
        except Exception:
            pass
        return False

    def has_suspicious_keywords(self, url):
        """
        Returns True if the URL contains common phishing keywords.
        """
        keywords = ['login', 'secure', 'update', 'verify', 'account', 'banking', 'confirm']
        url_lower = url.lower()
        return any(keyword in url_lower for keyword in keywords)

    def has_punycode(self, url):
        """
        Returns True if the URL uses punycode encoding (xn--).
        """
        hostname = urlparse(url).hostname or ""
        return "xn--" in hostname

    def has_suspicious_tld(self, url):
        """
        Returns True if the URL uses a suspicious TLD.
        """
        tlds = ['.tk', '.ml', '.ga', '.cf', '.gq']
        hostname = urlparse(url).hostname or ""
        return any(hostname.endswith(tld) for tld in tlds)

    def has_suspicious_extension(self, url):
        """
        Returns True if the URL ends with a suspicious file extension.
        """
        suspicious_exts = ['.exe', '.scr', '.zip', '.rar', '.js', '.php']
        path = urlparse(url).path.lower()
        return any(path.endswith(ext) for ext in suspicious_exts)

    def uses_url_shortener(self, url):
        """
        Returns True if the URL uses a known URL shortener.
        """
        shorteners = ['bit.ly', 'tinyurl.com', 'goo.gl', 't.co', 'ow.ly', 'is.gd', 'buff.ly']
        hostname = urlparse(url).hostname or ""
        return any(shortener in hostname for shortener in shorteners)