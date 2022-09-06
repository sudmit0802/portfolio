#include <iostream>
#include <Windows.h>
#include <stdlib.h>
#include <string.h>
#include "Fuzzer.h"

using namespace std;



int main()
{

	while (1)
	{
		while (!Manager());
		Run_exec();
	}
	
	return 0;
}