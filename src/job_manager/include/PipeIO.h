#ifndef __PipeIO_h__
#define __PipeIO_h__

#include <iostream>
#include <fstream>
#include <string>
#include <fcntl.h>
#include <filesystem>

class PipeIO {
private:
	std::ofstream wf;
	std::ifstream rf;
	std::string filename;

public:

	PipeIO();

	// Setters/Senders
	bool setFileName(std::string filename);
	bool connect(bool isWriting);
	void sendTransmission(std::string transmission);

	// Getters/Receivers
	bool getLine(std::string &line);
	void receiveTransmission(std::string &transmission);
	std::string getFileName();

};


#endif