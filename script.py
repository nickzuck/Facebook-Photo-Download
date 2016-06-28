import requests
class PagePhotoDownloader:
    
    def __init__(self, page_id, access_token):
        self.page_id = page_id 
        self.access_token = access_token

    def makeRequest(self):
        url = "https://graph.facebook.com/v2.6/%s/photos?type=uploaded&access_token=%s" %(self.page_id, self.access_token)

        r = requests.get(url)
        print r.json()


    def download(self):
        pass

if __name__ == "__main__":
    page_id = raw_input()
    access_token = raw_input()
    obj =  PagePhotoDownloader(page_id, access_token)
    obj.makeRequest()
