import requests
import urllib
class PagePhotoDownloader:
    
    def __init__(self, page_id, access_token):
        self.page_id = page_id 
        self.access_token = access_token

    def makeRequest(self):
        url = "https://graph.facebook.com/v2.6/%s/photos?type=uploaded&access_token=%s" %(self.page_id, self.access_token)

        r = requests.get(url)
        self.data =  r.json()

    def download(self):
        self.photos = self.data['data']
        for index, value in enumerate(self.photos):
            name = value['id']
            resource = urllib.urlopen("https://graph.facebook.com/%s/picture?type=normal" %(name))
            fileName = name + ".jpg"
            output = open(fileName,"wb")
            output.write(resource.read())
            output.close()
        
if __name__ == "__main__":
    page_id = raw_input()
    access_token = raw_input()
    obj =  PagePhotoDownloader(page_id, access_token)
    obj.makeRequest()
    obj.download()
