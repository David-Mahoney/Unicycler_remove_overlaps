#!/bin/bash

# Test the trimming functon 
# install unicycler with: python3 setup.py install

python -m unicycler.remove_overlaps test.gfa 55 --verbosity 3

# Check if overlaps remain, this may not do anything actually as the unicycler remove_overlap function sets the overlap to zero rather than calculating the overlap after trimming...
grep "L" test_trimmed.gfa | cut -d "	" -f 6 | uniq