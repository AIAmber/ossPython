import oss2

auth = oss2.Auth('LTAIm180aYQIc8DZ', 'Nl851kdy1VFxUXy8gwUCu8xczz0nkQ ')
service = oss2.Service(auth, 'http://oss-cn-hangzhou.aliyuncs.com')

# print([b.name for b in oss2.BucketIterator(service)])
# for b in oss2.BucketIterator(service):
# 	print(b.name)
print(len([b.name for b in oss2.BucketIterator(service)]))
print([b.name for b in oss2.BucketIterator(service)])