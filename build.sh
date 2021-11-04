#!/bin/bash
# This script prepares the user's unique system to run the scripts contained
# within this repository

echo -e "REQS_LOC=$PWD\nCOMMANDS=$PWD/commands\nHARDWARE=$PWD/src/hardware_control" > bin/env.sh
echo -e "PROGRAM PATHS CREATED"
SYSTEMBOOT="$(echo $PATH)"
EXPECTED_RESP="$PWD/bin"
if [[ "$SYSTEMBOOT" =~ "$EXPECTED_RESP" ]] 
	then
	echo -e "Parallel-Reqs/bin already on PATH:\n\tIf you have moved the folder, please remove */parallel-reqs/bin from your .bashrc file"
else
	echo -e "# Adding Parallel_Reqs/bin to the path\nexport PATH=\$PATH:$PWD/bin" >> ~/.bashrc
	echo -e "Added Parallel-Reqs/bin to PATH in .bashrc\nRun . ~/.bashrc or reopen the terminal to load them into your PATH"
fi
