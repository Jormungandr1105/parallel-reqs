#!/bin/bash
# BUILDS MPI LIBRARY

mpich_version="3.4.1" # version number
pathname=$(pwd) # current path

#Download folder name
lib_name="mpich-$mpich_version"

#Install folder name
install_folder="mpich-install"

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
 --prefix=$pathname/$install_folder --with-device=ch3 --disable-fortran 2>&1 | tee c.txt
make 2>&1 | tee m.txt
make install 2>&1 | tee mi.txt
PATH=$pathname/$install_folder/bin:$PATH && export Path
which mpicc
which mpiexec
