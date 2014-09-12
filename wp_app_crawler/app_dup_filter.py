from scrapy.dupefilter import RFPDupeFilter

class AppURLFilter(RFPDupeFilter):
    '''
        dup filter for url of app in window phone app
    '''
    def __getid__(self, url):
        return url
    
    def request_seen(self, request):
        id=self.__getid__(request.url)
        if id in self.fingerprints:
            return True
        self.fingerprints.add(id)
#        if request.url.find('details?id=')>-1:
        print '[Filter]: have not seen', request.url
        if self.file:
            self.file.write(request.url)
            self.file.write('\n')