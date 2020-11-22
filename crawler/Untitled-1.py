class AbstractHandler(object): 
    def __init__(self, _nxt): 
        self._nxt = _nxt 
    def handle(self, url): 
        handled = self.processRequest(request) 
        if not handled:
            self._nxt.handle(url)
    def processRequest(self, request): 
        raise NotImplementedError('First implement it !') 

class StatusCodeHandler(AbstractHandler):
    def processRequest(self, request):
        r = requests.get(url)
        if r.status_code == 200:
            return True
		
class RobotscheckHandler(AbstractHandler):
    def processRequest(self, request):
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(domain + '/robots.txt')
        rp.read()
        if not rp.can_fetch('*', url):  # robots.txt mentions that the link should not be parsed
            print('robots.txt does not allow to crawl', url)
            errors.append('Robots Exclusion')
            return False
        else:
            return True

class MimeHandler(AbstractHandler):
    def processRequest(self, request):
        if 'text/html' in r.headers['Content-Type']:
            return True
        else:
            return False