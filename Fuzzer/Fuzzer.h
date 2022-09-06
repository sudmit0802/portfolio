#ifndef FUZZER_H
#define FUZZER_H

#define _CRT_SECURE_NO_WARNINGS
#include <fstream>
#include <sstream>
#include <iostream>
#include <Windows.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int Manager(void);

int Change_Config(int offset, int value, int num_of_values);

void Add_Bytes(int value, int num_of_values);

void Run_exec(void);

int Find_Separators(void);

int Delete_Bytes(int start_offet, int end_offset);




#endif
