from __future__ import print_function
import os, sys
import oss2

endpoint = 'http://oss-cn-hangzhou.aliyuncs.com'
bucketName = 'pythontemp'
auth = oss2.Auth('LTAIm180aYQIc8DZ', 'Nl851kdy1VFxUXy8gwUCu8xczz0nkQ ')

bucket = oss2.Bucket(auth, endpoint, bucketName)
def percentage(consumed_bytes, total_bytes):
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        print('\r{0}% '.format(rate), end='')
        sys.stdout.flush()

bucket.put_object('test/story.txt', 'a'*1024*1024, progress_callback=percentage)