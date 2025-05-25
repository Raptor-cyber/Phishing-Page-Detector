from typing import TypedDict, List

class PhishingResult(TypedDict):
    url: str
    is_phishing: bool
    confidence_score: float

class LinkInfo(TypedDict):
    url: str
    is_safe: bool
    reason: str

def get_phishing_result_structure() -> PhishingResult:
    return PhishingResult(url="", is_phishing=False, confidence_score=0.0)

def get_link_info_structure() -> LinkInfo:
    return LinkInfo(url="", is_safe=True, reason="")