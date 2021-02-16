from requests import Session
from urllib.parse import urljoin

class HTTPSession(Session):
    def __init__(self, prefix_url=None, *args, **kwargs):
        super(HTTPSession, self).__init__(*args, **kwargs)
        self.prefix_url = prefix_url

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.prefix_url, url)
        return super(HTTPSession, self).request(method, url, *args, **kwargs)

