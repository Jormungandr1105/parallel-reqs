/*
This file contains a single helper function that runs a python script to change
the color of the LED strip connected to the cluster.
*/
void send_color(int color_index) {
	std::string colors[] = {"0","1","2","3","4","5","6"};
	// Colors - White_0, Red_1, Green_2, Blue_3, Purple_4, Yellow_5, Off_6
	std::string str_com = "cd ../parallel-reqs/src; python3 color_change.py " + colors[color_index];
	const char* command = str_com.c_str();
	system(command);
}