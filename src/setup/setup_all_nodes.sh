#!/bin/bash
################################################################################
##   Sets Up All Nodes For Parallel Processing   ###############################
################################################################################
command="cd Code/parallel-reqs/src/setup && chmod +x build_mpi.sh && ./build_mpi.sh"

"$(./execnodes.sh "$command" "$1")"
