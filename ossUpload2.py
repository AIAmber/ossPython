import os
import re

import oss2

endpoint = 'http://oss-cn-hangzhou.aliyuncs.com'
bucketName = 'pythontemp'
auth = oss2.Auth('LTAIm180aYQIc8DZ', 'Nl851kdy1VFxUXy8gwUCu8xczz0nkQ ')

# remoteFilePwd = 'test/'
# remoteFileName = 'remoteTest.txt'
localFilePwd = 'D:\_code\py'

# Upload Files
def ossUpload(remoteFile, localFile):
	service = oss2.Service(auth, endpoint)
	bucket = oss2.Bucket(auth, endpoint, bucketName)

	bucket.put_object_from_file(remoteFile, localFile)
	# print('Upload file successed!')

# Scan files
def scan_files(directory, prefix=None, postfix='py'):
	files_list = []

	for root, sub_dirs, files, in os.walk(directory):
		for special_file in files:
			if postfix:
				if special_file.endswith(postfix):
					files_list.append(os.path.join(root, special_file))
			elif prefix:
				if special_file.startswith(prefix):
					files_list.append(os.path.join(root, special_file))
			else:
				files_list.append(os.path.join(root, special_file))

	return files_list

n = 0
localFiles = scan_files(localFilePwd)

for localFile in localFiles:
	localFileName = localFile.split('\\')
	remoteFile = '/'.join(localFileName[1:])
	# remoteFileName = localFileName[-1]
	# ossUpload(remoteFilePwd+remoteFileName, localFile)
	ossUpload(remoteFile, localFile)
	n +=1
	rateOrg = int( 100*float(n)/float( len(localFiles) ) )
	rate = ' {0}% '.format(rateOrg)
	print( 'You have upload %s files, %s' %(n, rate) )	

print( '\rFiles totel: %s, Upload successed: %s' % (len(localFiles), n) )

################################################
# for localFile in scan_files(localFilePwd):
# 	localFileName = localFile.split('\\')
# 	# print(localFile.lstrip('oss'))
# 	# print(localFileName[-1])
# 	# print(type(localFile))
# 	# print(localFile)
# 	pwd = '/'.join(localFileName[1:])
# 	# print(localFileName[1:])
# 	print(pwd)