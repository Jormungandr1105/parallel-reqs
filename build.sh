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
$PWD/bin already on PATH:
	If you have moved the folder, please remove
	$PWD/bin
	from your .bashrc file
EOT

else
	# ADD TO PATH
	echo -e "# Adding $PWD/bin to the path\nexport PATH=\$PATH:$PWD/bin" >> ~/.bashrc
	# RELAY MESSAGE
cat << EOT
Added $PWD/bin to PATH in .bashrc
	Run . ~/.bashrc or reopen the terminal to load them into your PATH
EOT

fi

if [ ! -p communication/man_in ]
	then
	mkfifo communication/man_in
	echo -e "CREATED IN_PIPE"
fi

if [ ! -f machinefile ]
	then
	touch machinefile
	echo -e "CREATED MACHINEFILE"
fi

if [ ! -f src/discord_bot/.env ]
	then
	echo -e "DISCORD_TOKEN=\"\"" > src/discord_bot/.env
	echo -e "CREATED DISCORD ENV FILE"
fi

echo -e "DOWNLOADING JS FILES"
cd src/web-app/backend && npm install
cd src/web-app/frontend && npm install

echo -e "BUILD COMPLETE"
