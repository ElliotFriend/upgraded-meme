#!/usr/bin/env python3

signal = None
with open('input.txt', 'r') as f:
    signal = f.read().splitlines()
signal = signal[0]

sop_marker_len = 4
som_marker_len = 14
for i in range(0, len(signal)):
    marker = signal[i:som_marker_len+i]
    if len(set(marker)) > 13:
        print(i+som_marker_len)
        break