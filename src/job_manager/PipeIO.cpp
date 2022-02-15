#include "PipeIO.h"

PipeIO::PipeIO() {}

bool PipeIO::setFileName(std::string Filename) {
	filename = Filename;
	if (std::filesystem::exists(filename)) {
		return true;
	}
	return false;
}

bool PipeIO::connect(bool isWriting) {
	if (rf) {rf.close();}
	if (wf) {wf.close();}
	if(isWriting) {
		wf.open(filename);
	} else {
		rf.open(filename);
	}
	return true;
}

bool PipeIO::getLine(std::string &line) {
	if (!rf) {return false;}
	if (getline(rf,line)) {
		return true;
	}
	rf.close();
	return false;
}

void PipeIO::receiveTransmission(std::string &transmission) {
	bool connection = true;
	std::string line;
	while(true) {
		connection = getLine(line);
		if (!connection) {return;}
		transmission += line + "\n";
	}
}

void PipeIO::sendTransmission(std::string transmission) {
	wf << transmission;
	wf.close();
}