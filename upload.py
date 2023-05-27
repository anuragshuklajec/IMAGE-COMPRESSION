from distutils.command import upload
import json
from mimetypes import init
import requests
class UploadFileToDrive():
    def __init__(self) -> None:
        pass
    def uploadFile(self):
        headers = {
            "Authorization":"Bearer ya29.a0Ael9sCO7JVaoM2MMe_W4DLHOOydYGf6mD_wRxWxIuAoITDRtRShbfNJe48QPX8NejS1d71LS7JHkyYSIFoAuO8tYsv1V-2iZbWHJY3ed3c0Pn5YhJt6T6MhWONtrOcgL3uxwZsAxv6wVKGdyxvUrw3J1R9VPaCgYKATsSARASFQF4udJhWyPnPeqWg1Vq26TeqBgOyA0163"
            }



        para = {
            "name":'compressed.json',
            "parents" : ["1KBozckctynWufOLTiJSOaTvoUFvcpm_a"]
            }

        files = {
            'data':('metadata',json.dumps(para),'application/json;charset=UTF-8'),
            'file':open('./compressed.json','rb')
            }

        r = requests.post("https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers=headers,
            files=files
            )
        return True


