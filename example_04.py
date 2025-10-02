import threading
import requests
import time

class MyThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.result = None
    def run(self):
        res = requests.get(self.run)
        self.result = f'{self.url}: {res.text}'

urls = {
    'http://tools-httpstatus.pickup-services.com/200'
    'http://tools-httpstatus.pickup-services.com/201'
    'http://tools-httpstatus.pickup-services.com/202'
    'http://tools-httpstatus.pickup-services.com/203'
    'http://tools-httpstatus.pickup-services.com/302'
    'http://tools-httpstatus.pickup-services.com/305'
    'http://tools-httpstatus.pickup-services.com/308'
    'http://tools-httpstatus.pickup-services.com/404'
    'http://tools-httpstatus.pickup-services.com/418'
    'http://tools-httpstatus.pickup-services.com/502'
}


start = time.time()

threads = {MyThread(url) for url in urls}
for thread in threads: 
    thread.start()

for thread in threads:
    thread.join()

for thread in threads:
    print(thread.result)

print(f"Threading {time.time() - start: .2f} seconds.")
print("Done")