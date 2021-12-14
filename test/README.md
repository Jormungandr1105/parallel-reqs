# This is a VERY basic test case to see if you have setup your cluster correctly.

Modify the hosts.txt file to have the names of all of your nodes and the number of virtual nodes you would like to run on each (normally associated with the number of cores on each).
Then, run:
    mpirun -n [total_number_of_instances] -hostfile ../hosts.txt python3 roll_call.py
