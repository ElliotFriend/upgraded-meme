#!/usr/bin/env python3

signal = None
with open('input.txt', 'r') as f:
    signal = f.read().splitlines()
signal = signal[0]

sop_marker_len = 4
for i in range(0, len(signal)):
    marker = signal[i:sop_marker_len+i]
    if len(set(marker)) > 3:
        print(i+sop_marker_len)
        break