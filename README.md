# Unicycler remove overlaps
This is a modification of the Unicycler assembler that removes overlaps between segments/nodes/unitigs in a graph. The remove_all_overlaps function has been implemented as a function that can be called from the command line. Functionality to trim segments with equal overlap length added. Removing overlaps in a graph can be useful for graph alignment and extracting paths through the graph. 

## Installation:
```
git clone https://github.com/David-Mahoney/Unicycler_remove_overlaps.git
cd Unicycler_remove_overlaps
python3 setup.py install
```

## Usage:
```
python -m unicycler.remove_overlaps <input_graph.gfa> <overlap_length>
```
### Arguments:
- input_graph.gfa: The input graph in GFA format
- overlap_length: The overlap lenth to remove between segments/nodes/unitigs, variable length overlaps not supported
    - If you do want to disallow trimming to zero, set overlap_length to one more than the graph overlap length

### Output:
- a log including how many nucleotides were removed from each segment will be written to stdout
- a new GFA file with the overlaps removed will be written to the same directory as the input graph with the suffix "_trimmed.gfa"

## To do:
- [ ] Separate the remove_all_overlaps function from the Unicycler codebase
- [ ] Set up a command line interface with help documentation 
- [ ] Add an option to allow trimming segments to zero
- [ ] Improve testing