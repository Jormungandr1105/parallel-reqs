#!/bin/bash
# This script prepares the user's unique system to run the scripts contained
# within this repository

echo -e "REQS_LOC=$PWD\nCOMMANDS=$PWD/commands\nHARDWARE=$PWD/src/hardware_control" > bin/env.sh
echo -e "PROGRAM PATHS CREATED"
SYSTEMBOOT="$(echo $PATH)"
EXPECTED_RESP="$PWD/bin"
if [[ "$SYSTEMBOOT" =~ "$EXPECTED_RESP" ]] 
	then
	# SEND ALREADY ON PATH MESSAGE
cat << EOT
Parallel-Reqs/bin already on PATH:
	If you have moved the folder, please remove */parallel-reqs/bin
	from your .bashrc file
EOT

else
	# ADD TO PATH
	echo -e "# Adding Parallel_Reqs/bin to the path\nexport PATH=\$PATH:$PWD/bin" >> ~/.bashrc
	# RELAY MESSAGE
cat << EOT
Added Parallel-Reqs/bin to PATH in .bashrc
	Run . ~/.bashrc or reopen the terminal to load them into your PATH
EOT

fi

if [ ! -p communication/man_in ]
	then
	mkfifo communication/man_in
	echo -e "CREATED IN_PIPE\n"
fi
