#include "main.h"

struct Message {
	std::string hash;
	std::string command;
	std::string data;
	std::string extra;
};

struct Job {
	std::string hash;
	std::string path;
	std::string name;
	std::string filename;
	int max_time;
	std::string machinefile;
	int num_procs;
	bool running;
	pid_t pid;
	int start_time;
	std::string exec;
};

//FUNCTIONALITY
void time_manager();
void pipe_manager();
void parse_message(std::string transmission, Message *message);
void process_job(Message message);
void add_job(Message message);
void show_queue(Message message);
void send_response(std::string hash, std::string data);
// UTILITIES
void sleep(int milliseconds);
int convert_to_seconds(std::string time);
void print_job_info(Job job);


// Global Vars
bool keep_alive = true;
std::vector<Job> current_queue;
std::vector<Job> past_queue;
std::mutex current_queue_mutex;


int main() {
	pipe_manager();
	return 0;
}

void pipe_manager() {
	std::string transmission;
	std::vector<std::thread> threads;
	while (keep_alive) {
		transmission = "";
		Message curr_message;
		PipeIO* pipe_controller = new PipeIO();
		pipe_controller->setFileName("communication/man_in");
		pipe_controller->connect(false);
		pipe_controller->receiveTransmission(transmission);
		parse_message(transmission, &curr_message);
		std::thread new_t(process_job,curr_message);
		new_t.detach();
	}
}

void parse_message(std::string transmission, Message *message) {
	std::string section_delim = "\n################################################################################\n";
	std::string term_delim = "\n";
	int start = 0;
	int end;
	// Get Hash
	message->hash = transmission.substr(0,8);
	transmission = transmission.substr(9);
	// Start to get sections
	// Get Command
	end = transmission.find(section_delim);
	message->command = transmission.substr(start,end);
	transmission = transmission.substr(end+section_delim.length());
	// Get Data
	end = transmission.find(section_delim);
	message->data = transmission.substr(start,end);
	transmission = transmission.substr(end+section_delim.length());
	// Get Extra
	end = transmission.find(section_delim);
	message->extra = transmission.substr(start,end);

	// SANITY CHECK
	std::cout << "HASH: " << message->hash << std::endl;
	std::cout << "COMMAND: " << message->command << std::endl;
	std::cout << "DATA:\n" << message->data << std::endl;
	std::cout << "EXTRA:\n" << message->extra << std::endl;
}

void process_job(Message message) {
	if(message.command == "add_job") {
		add_job(message);
	} else if (message.command == "show_queue") {
		show_queue(message);
	} else {
		std::cout << "INVALID COMMAND: " << message.command << std::endl;
	}
}

void add_job(Message message) {
	Job curr_job;
	int start,end;
	std::string delim = "\n";
	std::string data = message.data;
	curr_job.hash = message.hash;
	// Get path
	end = data.find(delim);
	curr_job.path = data.substr(0,end);
	start = end + delim.length();
	// Get name
	end = data.find(delim,start);
	curr_job.name = data.substr(start,end-start);
	start = end + delim.length();
	// Get filename
	end = data.find(delim,start);
	curr_job.filename = data.substr(start,end-start);
	start = end + delim.length();
	// Get max duration
	end = data.find(delim,start);
	curr_job.max_time = convert_to_seconds(data.substr(start,end-start));
	start = end + delim.length();
	// Get machinefile
	end = data.find(delim,start);
	curr_job.machinefile = data.substr(start,end-start);
	start = end + delim.length();
	// Get number of processes
	curr_job.num_procs = std::stoi(data.substr(start));
	// Figure out bash exec
	curr_job.exec = "mpiexec -n " + std::to_string(curr_job.num_procs);
	curr_job.exec += " --hostfile " + curr_job.path + curr_job.machinefile;
	if (curr_job.filename.find(".py")!=std::string::npos) {
		curr_job.exec += " python3 -m mpi4py " + curr_job.path + curr_job.filename;
	} else {
		curr_job.exec += " " + curr_job.path + curr_job.filename;
	}
	print_job_info(curr_job);
	//FILE* stdout = popen("");
	current_queue_mutex.lock();
	current_queue.emplace_back(curr_job);
	current_queue_mutex.unlock();
}

void show_queue(Message message) {
	std::string response = "";
	if (message.data.substr(0,5) == "basic") {
		response += "_________________\n";
		response += "|_CURRENT_QUEUE_|________________________________________\n";
		response += "|__JOB_NAME__|_ELAPSED_TIME_|_%_|________________________\n";
	} else {
		response += "Unidentified Keyword: " + message.data + "\n";
	}
	send_response(message.hash,response);
}

void send_response(std::string hash, std::string data) {
	// (LOSING MY) SANITY CHECKS
	//std::cout << "SENDING TO: " << hash << std::endl;
	//std::cout << "SENDING: " << data <<std::endl;
	bool valid_pipe;
	PipeIO* return_pipe = new PipeIO();
	valid_pipe = return_pipe->setFileName("communication/"+hash);
	if(valid_pipe) {
		return_pipe->connect(true);
		return_pipe->sendTransmission(data);
	} else {
		std::cout << "ERROR: INVALID PIPE" << std::endl;
	}
}

// UTILITIES
void sleep(int milliseconds) {
	std::this_thread::sleep_for(std::chrono::milliseconds(milliseconds));
}

int convert_to_seconds(std::string time) {
	int seconds = 0;
	seconds += std::stoi(time.substr(0,3))*86400;
	seconds += std::stoi(time.substr(4,2))*3600;
	seconds += std::stoi(time.substr(7,2))*60;
	seconds += std::stoi(time.substr(10,2));
	return seconds;
}

void print_job_info(Job job) {
	std::cout << "PATH: " << job.path << std::endl;
	std::cout << "NAME: " << job.name << std::endl;
	std::cout << "FILENAME: " << job.filename << std::endl;
	std::cout << "MAX_TIME: " << job.max_time << std::endl;
	std::cout << "MACHINEFILE: " << job.machinefile << std::endl;
	std::cout << "NUM_PROCS: " << job.num_procs << std::endl;
	std::cout << "EXEC: " << job.exec << std::endl;
	std::cout << "RUNNING: " << job.running << std::endl;
	std::cout << "PID: " << job.pid << std::endl;
}
