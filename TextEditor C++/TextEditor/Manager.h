#ifndef MANAGER_H
#define MANAGER_H

#include "Main.h"

class Manager {
private:
  TextEditor textEditor_;

public:
  Manager(TextEditor &editor);
  void cursesInit(void);
  void toManage(void);
};

#endif
