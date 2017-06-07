# -*- coding: utf-8 -*-
# P85-P86

import pprint


message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    # count[character] = count[character] + 1
    count[character] += 1

pprint.pprint(count)  # good print