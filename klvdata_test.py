#!/usr/bin/env python3.7
import sys, klvdata;
for packet in klvdata.StreamParser(sys.stdin.buffer.read()): packet.structure()
