#include "Fuzzer.h"

int Manager()
{
	char* mode = (char*)calloc(32, sizeof(char));
	cout << "Choose a mode of fuzzing" << endl << endl;
	cout << "1 - Change one byte manually" << endl << "2 - Change multiple bytes manually" << endl << "3 - Add bytes to the end of config file" << endl << "4 - Delete bytes" << endl << "5 - Find separators" << endl << "6 - Auto-fuzzing" << endl << "7 - Run programm" << endl << ">>";

	cin >> mode;
	if (strlen(mode) > 1)
	{
		system("cls");
		cout << "Incorrect input! Try again" << endl << endl;
		free(mode);
		return 0;
	}

	switch (mode[0])
	{
		case '1':
		{
			int offset = 0;
			int val;
			cout << "Enter an index:" << endl << ">>";
			cin >> offset;
			cout << "Enter a value from 0x00 to 0xFF:" << endl << ">>";
			scanf("%x", &val);

			if (val < 0 || val>255)
			{
				cout << "Incorrect input! Try again" << endl << endl;
				return 0;
			}
			
			if (!Change_Config(offset, val, 1))
			{
				cout << "Incorrect input! Try again" << endl << endl;
				return 0;
			}

			cout << endl;


			break;
		}
		case '2':
		{
			int offset = 0;
			int num_of_values = 0;
			int val;
			cout << "Enter an index:" << endl << ">>";
			cin >> offset;
			cout << "Enter an amount of values:" << endl << ">>";
			cin >> num_of_values;
			cout << "Enter a value from 0x00 to 0xFF:" << endl << ">>";
	
			scanf("%x", &val);

			if (val < 0 || val>255)
			{
				cout << "Incorrect input! Try again" << endl << endl;
				return 0;
			}

			if (!Change_Config(offset, val, num_of_values))
			{
				cout << "Incorrect input! Try again" << endl << endl;
				return 0;
			}

			cout << endl;

			break;
		}
		case '3':
		{
			int num_of_values = 0;
			int val;
			cout << "Enter an amount of values:" << endl << ">>";
			cin >> num_of_values;
			cout << "Enter a value from 0x00 to 0xFF:" << endl << ">>";
			scanf("%x", &val);

			if (val < 0 || val>255)
			{
				cout << "Incorrect input! Try again" << endl << endl;
				return 0;
			}

			cout << endl;

			Add_Bytes(val, num_of_values);

			break;
		}
		case '4':
		{
			int start = 0;
			int end = 0;
			
			cout << "Enter a start index:" << endl << ">>";
			cin >> start;
			cout << "Enter an end index:" << endl << ">>";
			cin >> end;

			if (!Delete_Bytes(start, end))
			{
				cout << "Incorrect input! Try again" << endl;
				return 0;
			}

			break;
		}
		case '5':
		{
			cout << endl << "Searching for separators..." << endl;
			if (!Find_Separators())
			{
				cout << "There is no any separator here!"<<endl;
			}
			cout << endl << endl;
			return 0;
		}
		case '6':
		{
			// 8-9: 0xFF, 0x7F
			int val = 0xFF;
			cout << "Current offset: 0x";
			printf("%x\n", 8);
			cout << "New value for this position: 0x";
			printf("%x\n", val);
			Change_Config(8, val, 1);
			Run_exec();
			val = 0x7F;
			cout << "Current offset: 0x";
			printf("%x\n", 9);
			cout << "New value for this position: 0x";
			printf("%x\n", val);
			Change_Config(9, val, 1);
			Run_exec();
			
			// 16-17: 0xFF, 0x7F
			val = 0xFF;
			cout << "Current offset: 0x";
			printf("%x\n", 16);
			cout << "New value for this position: 0x";
			printf("%x\n", val);
			Change_Config(16, val, 1);
			Run_exec();
			val = 0x7F;
			cout << "Current offset: 0x";
			printf("%x\n", 17);
			cout << "New value for this position: 0x";
			printf("%x\n", val);
			Change_Config(17, val, 1);
			Run_exec();
			
			// 54 - oo: 0xFF
			int i = 54;
			int j = 0;
			val = 0xFF;
			while (1)
			{
				cout << "Current offset: 0x";
				printf("%x\n", 54 + j * 64);
				cout << "New value for this position: 0x";
				printf("%x\n", val);
				Change_Config(i, val, 64);
				Run_exec();
				i += 64;
				j++;
			}

			break;
		}
		case '7':
		{
			return 1;
		}
		default:
		{
			system("cls");
			cout << "Incorrect input! Try again" << endl;
			return 0;
		}
	}
	cout << endl;
	free(mode);
	cout << "Config file has been modified successfully!"<<endl<<endl;
	return 1;
}

int Change_Config(int offset, int value, int num_of_values)
{
	ifstream config_file("./Python27/config_12", ios::binary);
	stringstream ss;
	ss << config_file.rdbuf();
	string sbuf = ss.str();
	config_file.close();

	if (offset<0)
	{
		return 0;
	}

	if (offset + num_of_values > sbuf.length())
	{
		sbuf.replace(offset, sbuf.length() - offset, num_of_values, (char)value);
	}
	else
	{
		sbuf.replace(offset, num_of_values, num_of_values, (char)value);
	}

	ofstream conf_file("./Python27/config_12", ios::binary);
	conf_file.write(sbuf.c_str(), sbuf.length());
	conf_file.close();
	return 1;
}

void Add_Bytes(int value, int num_of_values)
{
	ifstream config_file("./Python27/config_12", ios::binary);
	stringstream ss;
	ss << config_file.rdbuf();
	string sbuf = ss.str();
	config_file.close();

	sbuf.insert(sbuf.length()-1, num_of_values, (char)value);
	
	ofstream conf_file("./Python27/config_12", ios::binary);
	conf_file.write(sbuf.c_str(), sbuf.length());
	conf_file.close();
}

int Find_Separators(void)
{
	int cnt = 0;
	ifstream config_file("./Python27/config_12", ios::binary);
	stringstream ss;
	ss << config_file.rdbuf();
	string sbuf = ss.str();
	config_file.close();
	
	for (int i = 0; i < sbuf.length(); i++)
	{
		switch ((int)sbuf[i])
		{
			case 0x3B:
			{
				cout << " Separator: ';' " << "Offset: 0x";
				printf("%x\n", i);
				break;
			}
			case 0x20:
			{
				cout << " Separator: ' ' " << "Offset: 0x";
				printf("%x\n", i);
				break;
			}
			case 0x2E:
			{
				cout << " Separator: '.' " << "Offset: 0x";
				printf("%x\n", i);
				break;
			}
			case 0x2C:
			{
				cout << " Separator: ',' " << "Offset: 0x";
				printf("%x\n", i);
				break;
			}
			case 0x21:
			{
				cout << " Separator: '!' " << "Offset: 0x";
				printf("%x\n", i);
				break;
			}
			case 0x3F:
			{
				cout << " Separator: '?' " << "Offset: 0x";
				printf("%x\n", i);
				break;
			}
			case 0x3A:
			{
				cout << " Separator: ':' " << "Offset: 0x";
				printf("%x\n", i);
				break;
			}
			case 0x2F:
			{
				cout << " Separator: '/' " << "Offset: 0x";
				printf("%x\n", i);
				break;
			}
			default:
			{
				cnt++;
				break;
			}
		}
	}

	if (cnt == sbuf.length())
	{
		return 0;
	}
	else
	{
		return 1;
	}

}

int Delete_Bytes(int start_offset, int end_offset)
{
	ifstream config_file("./Python27/config_12", ios::binary);
	stringstream ss;
	ss << config_file.rdbuf();
	string sbuf = ss.str();
	config_file.close();
	string tmp;

	if (start_offset < 0 || end_offset<start_offset || end_offset<0 || start_offset>sbuf.length() || end_offset>sbuf.length())
	{
		return 0;
	}

	tmp.append(sbuf.c_str(), start_offset);
	for (int i = end_offset+1; i < sbuf.length(); i++)
	{
		tmp.append(1, sbuf[i]);
	}

	ofstream conf_file("./Python27/config_12", ios::binary);
	conf_file.write(tmp.c_str(), tmp.length());
	conf_file.close();
	return 1;
}


void Run_exec()
{
	system("python2.exe.lnk Debugger.py");
}