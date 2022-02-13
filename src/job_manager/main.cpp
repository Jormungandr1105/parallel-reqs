#include "main.h"

int main() {

	// First test
	
	//int fifo = mkfifo("pipe",0666);
	PipeIO* pipe_controller = new PipeIO();
	pipe_controller->setFileName("communication/man_in");
	pipe_controller->connect(false);
	std::string line;
	pipe_controller->receiveTransmission(line);
	std::cout << line << std::endl;
	std::string hash = line.substr(0,8);
	std::cout << "HASH:" << hash << std::endl;
	pipe_controller->setFileName("communication/"+hash);
	pipe_controller->connect(true);
	pipe_controller->sendTransmission("RECEIVED");

	return 0;
}