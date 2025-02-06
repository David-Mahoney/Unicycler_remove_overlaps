from .assembly_graph import AssemblyGraph 
import sys

# This script removes all overlaps from a GFA file, without trimming any segment down to zero. Some graph alignment tools cannot accept segment of length zero. 
# If you do want the functionality to trim segments to zero, set overlap length to be one less than your graph's overlap length.
# Cannot trim variable length overlaps found in some graph types (e.g. OLC assembly graphs).

#must be run in module mode with unicycler installed 

if __name__ == '__main__':
    """
    Main function to remove overlaps from a GFA file. 
    Call from command line with: python -m unicycler.remove_overlaps <graph.gfa> <overlap_length>
    
    Arguments:
    input_graph: GFA file to remove overlaps from
    overlap: length of overlaps to remove (typically the largest k-mer size used to build the graph, available in the GFA file)

    Returns:
    stdout log of segments and how many nucleotides were trimmed from each end
    GFA file with overlaps removed
    """

    input_graph = sys.argv[1]
    overlap = int(sys.argv[2])
    # Load the graph
    graph = AssemblyGraph(input_graph, overlap)
    graph.load_from_gfa(input_graph)
    # trim segments 
    graph.remove_all_overlaps()
    # Save the trimmed graph
    graph.save_to_gfa(input_graph[:-4] + "_trimmed.gfa")
