# main.py

from detector.phishing_detector import PhishingDetector
from analysis.link_analysis import LinkAnalysis

def main():
    # Initialize the phishing detector and link analysis components
    phishing_detector = PhishingDetector()
    link_analysis = LinkAnalysis()

    # Example workflow
    url = input("Enter a URL to check for phishing: ")
    is_phishing = phishing_detector.detect_phishing(url)
    print(f"Phishing detection result for {url}: {'Phishing' if is_phishing else 'Legitimate'}")

    print("\nNow, enter the HTML content of a page to analyze its links.")
    page_content = input("Paste HTML content here: ")
    links_info = link_analysis.analyze_links(page_content)
    print("\nExtracted links and analysis:")
    for info in links_info:
        print(f"URL: {info['url']}")
        print(f"Safe: {info['is_safe']}")
        print("Reasons:")
        for reason in info['reasons']:
            print(f" - {reason}")
        print("-" * 40)

if __name__ == "__main__":
    main()