from distutils.command import upload
import json
from mimetypes import init
import requests
class UploadFileToDrive():
    def __init__(self) -> None:
        pass
    def uploadFile(self):
        headers = {
            "Authorization":"{Drive Authorization Code}"
            }



        para = {
            "name":'compressed.json',
            "parents" : ["{Folder Key}"]
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


