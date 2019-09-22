#!/usr/bin/env python3

import zulip

# Pass the path to your zuliprc file here.
client = zulip.Client(config_file="~/.zuliprc")

# Upload a file
path_to_file ='/home/zulip/izyrtm/OUTPUT.png'
with open(path_to_file, 'rb') as fp:
    result = client.call_endpoint(
        'user_uploads',
        method='POST',
        files=[fp]
    )
print(result)
