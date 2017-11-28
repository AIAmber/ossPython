import os
import re

import oss2

# Resumable Upload
oss2.resumable_upload(bucket, 'remote.txt', 'local.txt')

# Resumble Upload
oss2.resumable_upload(bucket, 'remote.txt', 'local.txt',
    store=oss2.ResumableStore(root='/tmp'),
    multipart_threshold=100*1024,
    part_size=100*1024,
    num_threads=4)