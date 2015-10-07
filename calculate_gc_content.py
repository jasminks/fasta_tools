#!/usr/bin/env python

# Command line script to calculate base frequency from a .fasta file

import sys
import argparse

a_count = 0
c_count = 0
g_count = 0
t_count = 0

varb = ["fasta_file"]
parser = argparse.ArgumentParser()
parser.add_argument("file_name")
args = parser.parse_args()
file_name = args.file_name

with open(args.file_name, 'r') as fasta:
    for line in fasta:
        if line.startswith(">"):
            # Header line, skip it
            continue
        a_count += line.count("A")
        t_count += line.count("T")
        c_count += line.count("C")
        g_count += line.count("G")
        
    print("A: %d" % a_count)
    print("C: %d" % c_count)
    print("G: %d" % g_count)
    print("T: %d" % t_count)
    
        
total=float(a_count+t_count+c_count+g_count)

a_percent=float((a_count/total)*100.)
c_percent=float((c_count/total)*100.)
t_percent=float((t_count/total)*100.)
g_percent=float((g_count/total)*100.)

print("The percent of A: %f" % a_percent)
print("The percent of C: %f" % c_percent)
print("The percent of T: %f" % t_percent)
print("The percent of G: %f" % g_percent)


