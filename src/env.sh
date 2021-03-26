#!/bin/bash

# version number
export mpich_version="3.4.1" 

# current path to project
export pathname=$(cd .. && pwd) 

#Download folder name
export lib_name="mpich-$mpich_version"

#Install folder name
export install_folder="mpich-install"

export PATH=$pathname/$install_folder/bin:$PATH