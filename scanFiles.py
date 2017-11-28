import os

# Scan files
def scan_files(directory, prefix=None, postfix=None):
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

# scan_files('D:\_code\py\demo\oss')
filePwd = 'D:\_code\py\demo'

print(len(scan_files(filePwd)))
print(scan_files(filePwd))