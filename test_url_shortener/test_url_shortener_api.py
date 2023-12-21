# test_url_shortener_api.py

import requests

class RateLimitError(Exception):
    """Raised when the ratelimit is exceeded"""
    pass

class InvalidRequestError(Exception):
    """Raised when an invalid url is passed"""
    pass

def test_shorten_url(url: str = "https://example.com/"):
    """
    Shortens a URL
    --------------

    Args:
    -----

    `url`:
        Type: `str`
        Required: `True`


    Raises:
    -------

    `RateLimitError`:
        Reasons: `Raised when the ratelimit is exceeded`
    
    `InvalidRequestError`:
        Reasons: `Raised when an invalid url is passed`
    """
    headers = {
        "URL": url,
        "Content-Type": "application/json"
    }
    request = requests.get(
        "https://cocfire.xyz/api/shortener", 
        headers = headers
    )
    if request.status_code == 200:
        return request.text
    elif request.status_code == 429:
        raise RateLimitError
    elif request.status_code == 400:
        raise InvalidRequestError

__all__ = ['RateLimitError', 'InvalidRequestError', 'test_shorten_url']
