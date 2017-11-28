import os

import oss2

endpoint = 'http://oss-cn-hangzhou.aliyuncs.com'
bucketName = 'pythontemp'
auth = oss2.Auth('LTAIm180aYQIc8DZ', 'Nl851kdy1VFxUXy8gwUCu8xczz0nkQ ')
service = oss2.Service(auth, endpoint)
bucket = oss2.Bucket(auth, endpoint, bucketName)

remoteFilePwd = 'test/'
remoteFileName = 'remoteTest.txt'

bucket.put_object(remoteFilePwd + remoteFileName, b'hello, remote!')
print('Upload file successed!')
