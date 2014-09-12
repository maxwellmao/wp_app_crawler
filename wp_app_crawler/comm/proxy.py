from scrapy.contrib.downloadermiddleware.retry import RetryMiddleware
import telnetlib

class RetryChangeProxyMiddleware(RetryMiddleware):
    def _retry(self, request, reason, spider):
#        log.msg('Changing proxy')
        print '[Proxy] Changing proxy'
        tn = telnetlib.Telnet('127.0.0.1', 9051)
        tn.read_until("Escape character is '^]'.", 2)
        tn.write('AUTHENTICATE "267765"\r\n')
        tn.read_until("250 OK", 2)
        tn.write("signal NEWNYM\r\n")
        tn.read_until("250 OK", 2)
        tn.write("quit\r\n")
        tn.close()
        time.sleep(3)
#        log.msg('Proxy changed')
        print '[Proxy] Proxy changed'
        return RetryMiddleware._retry(self, request, reason, spider)
