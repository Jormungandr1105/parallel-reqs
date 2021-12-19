#!/bin/bash
# BUILDS MPI LIBRARY

# Get env variables
source ./env.sh

################################################################################
# FUNCTIONS
################################################################################
#
# Check if folder exists, if it doesn't, make it
function Create_Folder() {
	# INPUTS: foldername
	# OUTPUTS: 
	foldername=$1
	if [ ! -d $foldername ]
	then
		return $(mkdir $foldername)
	fi
	return 0
}
# Check if file exists, if it doesn't, make it
function Create_File() {
	# INPUTS: filename
	# OUTPUTS: 
	filename=$1
	if [ ! -f $filename ]
	then
		return $(touch $filename)
	fi
	return 0
}
# Check if folder exists, if it does, delete it
function Delete_Folder() {
	# INPUTS: foldername
	# OUTPUTS: 
	foldername=$1
	if [ -d $foldername ]
	then
		return $(rm -r $foldername)
	fi
	return 0
}
################################################################################
# MAIN
################################################################################
cd ../..
# Make the folders, if they dont exist
Create_Folder $install_folder
Create_Folder temp
Create_Folder mpich-download
if [ ! -d $install_folder/bin ] # If MPICH not installed and built
then
	# Download and install MPICH Library
	cd mpich-download
	if [ ! -f $lib_name.tar.gz ]
	then
		wget http://www.mpich.org/static/downloads/$mpich_version/$lib_name.tar.gz
	fi
	if [ ! -d $lib_name ]
	then
		#tar -xpzf $lib_name.tar.gz # overwrites time accessed
		#file-roller $lib_name.tar.gz --extract-here # works only if gnome desktop
		pax -f $lib_name.tar.gz -z -r # this seems to work across systems
		#gunzip -c $lib_name.tar.gz | tar xf - # overwrites time accessed
	fi

	cd ../temp
	# Configure and Make
	$pathname/mpich-download/$lib_name/configure \
	--prefix=$pathname/$install_folder --with-device=ch3 \
	--disable-fortran 2>&1 | tee c.txt
	make 2>&1 | tee m.txt
	make install 2>&1 | tee mi.txt
fi
cd $pathname
if [ -d $install_folder/bin ]
then
	echo "MPICH INSTALLED SUCCESSFULLY"
	cur_path="$(echo $PATH)"
	should_have="$pathname/$install_folder/bin"
	if [[ "$cur_path" =~ "$should_have" ]]
	then
		echo "MPICH ON PATH"
	else
		echo -e "# Use MPICH for Parallel Programming\nexport PATH=$pathname/$install_folder/bin:\$PATH" >> $HOME/.bashrc
		echo "MPICH ADDED TO PATH"
	fi
else
	echo "MPICH INSTALLATION FAILED"
fi

# Cleanup
Delete_Folder temp
