#ifndef TEXTEDITOR_H
#define TEXTEDITOR_H

#include "Main.h"

class TextEditor {
private:
  char mode_;
  int x_, y_;
  int lowestbound_;
  int rightestbound_;
  bool changed_;
  TextBuffer textbuf_;
  Screen screen_;
  MyString searchbuf_;
  MyString clipboard_;
  MyString status_;
  MyString filename_;
  MyString console_;

public:
  bool upstatus;
  TextEditor(void);
  char getMode(void) const;
  int getLowestBound(void) const;
  int getRightestBound(void) const;
  MyString getStatus(void) const;
  Screen getScreen(void) const;
  TextBuffer getTextBuffer(void) const;
  MyString getClipboard(void) const;
  int getNum(MyString &arr);
  int getPageSize(void);
  void processConsole(int logic = 0);
  void pasteClipboard(void);
  bool openFile(MyString filename);
  void printScreen(void);
  bool writeFile(void);
  void handleInput(int input);
  int getSymbol(void) const;
  int getX(void) const;
  int getY(void) const;
  void deleteWord(void);
  void isolateWord(void);
  void copyString(void);
  void setMode(char m);
  void setCursor(int x, int y);
  void updateStatus(void);
  void moveEndString(void);
  void moveStartString(void);
  void moveStartWord(void);
  void moveLastPage(void);
  void moveEndWord(void);
  void moveLeft(void);
  void moveUp(void);
  void moveRight(void);
  void moveDown(void);
};

#endif