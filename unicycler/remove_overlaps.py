from .assembly_graph import AssemblyGraph #, CannotTrimOverlaps
import sys
# from . import log
# import math
# from collections import defaultdict

#must be run in module mode with unicycler installed 
## python -m unicycler.remove_overlaps ../graph_test_graphamr.gfa

if __name__ == '__main__':
    g = sys.argv[1]
    # Load the graph
    graph = AssemblyGraph(g, 55)
    graph.load_from_gfa(g)
    ## Remove all overlaps without trimming a segment down to zero 
    print("Removing overlaps, here goes nothing")
    graph.remove_all_overlaps()
    # Save the graph
    graph.save_to_gfa(g[:-4] + "_maybe.gfa")
