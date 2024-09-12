#include "Main.h"

Adapter_ncurses adm;

Manager::Manager(TextEditor &editor) { textEditor_ = editor; }

void Manager::cursesInit(void) {
  adm.noechoA();
  adm.keypadA(stdscr, true);
  textEditor_.printScreen();
  adm.curs_setA(0);
  textEditor_.processConsole(textEditor_.getSymbol());
}

void Manager::toManage(void) {
  cursesInit();
  while (textEditor_.getMode() != EXIT_MODE) {
    if (textEditor_.upstatus) {
      textEditor_.updateStatus();
    }

    textEditor_.printScreen();
    textEditor_.handleInput(textEditor_.getSymbol());
  }
  adm.endwinA();
}