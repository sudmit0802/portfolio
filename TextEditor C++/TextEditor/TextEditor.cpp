#include "Main.h"

Adapter_ncurses adt;

TextEditor::TextEditor(void) {
  mode_ = NAVIGATION_MODE;
  status_ = "";
  clipboard_ = "";
  searchbuf_ = "";
  changed_ = false;
  upstatus = true;
  filename_ = "";
  rightestbound_ = 0;
  lowestbound_ = 0;
  x_ = 0;
  y_ = 0;
  openFile(HELLO_FILENAME);
}

bool TextEditor::openFile(MyString filename) {
  filename_ = filename;
  textbuf_.clear();

  std::ifstream input_file(filename_.c_str());

  if (input_file.is_open()) {

    while (!input_file.eof()) {
      MyString temp;
      input_file >> temp;
      if (temp.length() < COLS) {
        textbuf_.appendString(temp);
      } else {
        for (int i = 0; i < temp.length() / COLS; i++) {
          MyString ins = temp.substr(i * COLS, COLS);
          textbuf_.appendString(ins);
        }
        textbuf_.appendString(temp.substr(temp.length() - temp.length() % COLS,
                                          temp.length() % COLS));
      }
      temp.clear();
    }

    setCursor(0, 0);

    input_file.close();
    return true;
  } else {
    console_.append("\nFile does not exist. press 'Enter' to continue");
    setMode(COMMAND_MODE);
    input_file.close();
    return false;
  }
}

void TextEditor::setCursor(int x, int y) {
  x_ = x;
  y_ = y;
}

void TextEditor::setMode(char m) { mode_ = m; }

MyString TextEditor::getStatus(void) const { return status_; }

void TextEditor::updateStatus(void) {
  status_.clear();
  status_.shrink_to_fit();
  char var = getMode();

  if (var == NAVIGATION_MODE) {
    status_ = "Navigation mode\t\t";
    status_.append(CED_TITLE);
    status_.append(CED_VERSION);
    status_.append(CED_AUTHOR);
    status_.append("\t\t");
  } else if (var == INPUT_MODE) {
    status_ = "Input mode";
  } else if (var == SEARCH_MODE) {
    status_ = "Search mode";
  } else if (var == COMMAND_MODE) {
    status_ = "Command mode";
  } else if (var == EXIT_MODE) {
    status_ = "Shutting down...";
  }

  status_.append("\tCOL: ");
  status_.append(std::to_string(getX() + 1));
  status_.append("\tROW: ");
  status_.append(std::to_string(getY() + getLowestBound() + 1));
  upstatus = false;
}

char TextEditor::getMode(void) const { return mode_; }

int TextEditor::getX(void) const { return x_; }

int TextEditor::getY(void) const { return y_; }

Screen TextEditor::getScreen(void) const { return screen_; }

int TextEditor::getSymbol(void) const { return getScreen().getSymbol(); }

int TextEditor::getLowestBound(void) const { return lowestbound_; }

int TextEditor::getRightestBound(void) const { return rightestbound_; }

MyString TextEditor::getClipboard(void) const { return clipboard_; }

TextBuffer TextEditor::getTextBuffer(void) const { return textbuf_; }

void TextEditor::printScreen(void) {
  MyString st = status_;

  if (getMode() == COMMAND_MODE) {
    adt.clearA();
    getScreen().printStatusBar(status_);
    getScreen().printConsole(console_);
  } else {
    getScreen().printStatusBar(status_);
    getScreen().printBuf(getTextBuffer().getStrings(), getLowestBound(), getX(),
                         getY());
  }
}

void TextEditor::handleInput(int input) {
  adt.moveA(getY(), getX());
  upstatus = true;
  if (input == KEY_ESC) {
    console_.clear();
    searchbuf_.clear();
    setMode(NAVIGATION_MODE);
    return;
  }

  switch (getMode()) {
  case NAVIGATION_MODE: {
    switch (input) {
    case (int)'i': {
      setMode(INPUT_MODE);
      break;
    }
    case (int)'I': {
      moveStartString();
      setMode(INPUT_MODE);
      break;
    }
    case (int)'/': {
      searchbuf_.clear();
      searchbuf_.append(1, '/');
      setMode(SEARCH_MODE);
      break;
    }
    case (int)'?': {
      searchbuf_.clear();
      searchbuf_.append(1, '?');
      setMode(SEARCH_MODE);
      break;
    }
    case (int)'^': {
      moveStartString();
      break;
    }
    case (int)'$': {
      moveEndString();
      break;
    }
    case (int)'G': {
      if (console_.length() > 0) {
        setMode(COMMAND_MODE);
        processConsole();
        setMode(NAVIGATION_MODE);
        adt.clearA();
        adt.refreshA();
      } else {
        moveLastPage();
      }
      break;
    }
    case (int)'y': {
      int next = getSymbol();
      if (next == (int)'w') {
        copyString();
        isolateWord();
      } else if (next == (int)'s') {
        copyString();
      }
      break;
    }
    case (int)'p': {
      pasteClipboard();
      break;
    }
    case (int)'d': {
      if (textbuf_.getBufferSize() <= 0) {
        break;
      }

      int next = getSymbol();
      if (next == (int)'d') {
        copyString();
        if (textbuf_.getBufferSize() > 0) {
          textbuf_.removeString(getY() + getLowestBound());
          moveStartString();
        }
      } else if (next == (int)'i') {
        if (getSymbol() == (int)'w') {
          deleteWord();
        }
      }
      changed_ = true;
      adt.clearA();
      adt.refreshA();
      break;
    }
    case (int)'x': {
      setMode(INPUT_MODE);
      handleInput(KEY_DEL);
      setMode(NAVIGATION_MODE);
      break;
    }
    case KEY_PGD: {
      int cnt = getPageSize();
      if (cnt <= 0) {
        break;
      }

      int tmp = (getLowestBound() + getY()) / cnt;
      while (getLowestBound() + getY() < (tmp + 1) * cnt &&
             getLowestBound() + getY() < textbuf_.getBufferSize() - 1) {
        moveDown();
        if (getLowestBound() + getY() >= textbuf_.getBufferSize() - 1) {
          while (getLowestBound() + getY() > tmp * cnt) {
            moveUp();
          }
          break;
        }
      }
      moveStartString();
      break;
    }
    case KEY_PGU: {
      int cnt = getPageSize();
      if (cnt <= 0) {
        break;
      }

      int tmp = (getLowestBound() + getY()) / cnt;
      while (getLowestBound() + getY() > (tmp - 1) * cnt && getY() > 0) {
        moveUp();
      }
      moveStartString();
      break;
    }
    case (int)'g': {
      if (getSymbol() == (int)'g') {
        setCursor(0, 0);
        lowestbound_ = 0;
      }
      break;
    }
    case (int)'r': {
      if (getY() + getLowestBound() >= textbuf_.getBufferSize()) {
        break;
      }
      if (getX() < textbuf_[getY() + getLowestBound()].length()) {
        textbuf_.replaceSymbol(getY() + getLowestBound(), getX(),
                               (const char)getSymbol());
      } else {
        int next = getSymbol();
        setMode(INPUT_MODE);
        handleInput(KEY_DEL);
        handleInput(next);
        setMode(NAVIGATION_MODE);
      }
      changed_ = true;
      break;
    }
    case (int)'S': {
      moveEndString();
      setMode(INPUT_MODE);
      break;
    }
    case (int)'A': {
      changed_ = true;
      moveStartString();
      textbuf_.nullString(getY() + getLowestBound());
      setMode(INPUT_MODE);
      break;
    }
    case (int)'w': {
      moveEndWord();
      break;
    }
    case (int)'b': {
      moveStartWord();
      break;
    }
    case KEY_CM:
    case 65414: {
      setMode(COMMAND_MODE);
      break;
    }
    case KEY_LEFT: {
      moveLeft();
      break;
    }
    case KEY_RIGHT: {
      moveRight();
      break;
    }
    case KEY_DOWN: {
      moveDown();
      break;
    }
    case KEY_UP: {
      moveUp();
      break;
    }
    default: {
      console_.append(1, (const char)input);
      break;
    }
    }

    break;
  }

  case COMMAND_MODE: {
    switch (input) {
    case KEY_CODE_ENTER: {
      adt.clearA();
      processConsole();
      break;
    }
    default: {
      printScreen();
      console_.append(1, (const char)input);
      adt.moveA(getY(), console_.length());
      break;
    }
    }
    break;
  }

  case SEARCH_MODE: {
    searchbuf_.append(1, (const char)input);
    bool found = false;
    int X = getX();
    int Y = getY();
    int lb = getLowestBound();
    if (searchbuf_[0] == '/') {
      searchbuf_.erase(0, 1);
      do {
        if (textbuf_[getY() + getLowestBound()].find(searchbuf_.c_str(),
                                                     getX()) >= 0) {
          int found_pos = textbuf_[getY() + getLowestBound()].find(
              searchbuf_.c_str(), getX());
          found = true;
          while (getX() < found_pos) {
            moveRight();
          }
          break;
        }
        moveDown();
        moveStartString();
      } while (getY() + getLowestBound() < textbuf_.getBufferSize());
      searchbuf_.insert(0, "/");
    } else if (searchbuf_[0] == '?') {
      searchbuf_.erase(0, 1);
      setCursor(0, 0);
      lowestbound_ = 0;
      do {
        if (textbuf_[getY() + getLowestBound()].find(searchbuf_.c_str(),
                                                     getX()) >= 0) {
          int found_pos = textbuf_[getY() + getLowestBound()].find(
              searchbuf_.c_str(), getX());
          found = true;
          while (getX() < found_pos) {
            moveRight();
          }
          break;
        }
        moveDown();
        moveStartString();
      } while (getY() + getLowestBound() < Y);
      searchbuf_.insert(0, "?");
    }

    if (!found) {
      setCursor(X, Y);
      lowestbound_ = lb;
    }
    break;
  }

  case INPUT_MODE: {
    switch (input) {
    case KEY_LEFT: {
      moveLeft();
      break;
    }
    case KEY_RIGHT: {
      moveRight();
      break;
    }
    case KEY_DOWN: {
      moveDown();
      break;
    }
    case KEY_UP: {
      moveUp();
      break;
    }
    case KEY_DEL: {
      if (textbuf_.getBufferSize() <= 0) {
        break;
      }
      if ((getX() >= textbuf_[getY() + getLowestBound()].length() - 1) &&
          (getY() + getLowestBound() < textbuf_.getBufferSize() - 1)) {
        MyString tmp(textbuf_[getY() + getLowestBound() + 1]);
        if (tmp.length() > 0) {
          textbuf_.appendToString(getY() + getLowestBound(), tmp);
        }
        textbuf_.removeString(getY() + getLowestBound() + 1);
      } else if (getX() < textbuf_[getY() + getLowestBound()].length() - 1) {
        textbuf_.erase(getY() + getLowestBound(), getX() + 1, 1);
      }
      changed_ = true;
      break;
    }
    case KEY_CODE_BACKSPACE: {
      if (getX() == 0 && getY() > 0) {
        MyString tmp(textbuf_[getY() + getLowestBound()]);
        if (lowestbound_ == 0) {
          setCursor(textbuf_[getY() + getLowestBound() - 1].length(),
                    getY() - 1);
        } else {
          lowestbound_--;
          setCursor(textbuf_[getY() + getLowestBound()].length(), getY());
        }
        textbuf_.appendToString(getY() + getLowestBound(), tmp);
        textbuf_.removeString(getY() + getLowestBound() + 1);
      } else if (getX() > 0) {
        textbuf_.deleteSymbol(getX(), getY() + getLowestBound());
        moveLeft();
      }
      changed_ = true;
      break;
    }
    case KEY_CODE_ENTER: {
      if (textbuf_.getBufferSize() <= 0) {
        textbuf_.appendString("");
        textbuf_.appendString("");
        moveDown();
        break;
      }
      if (getX() < textbuf_[getY() + getLowestBound()].length()) {
        MyString tmp(textbuf_[getY() + getLowestBound()].substr(
            getX(), textbuf_[getY() + getLowestBound()].length() - getX()));
        textbuf_.insertString(tmp, getY() + getLowestBound() + 1);
        textbuf_.erase(getY() + getLowestBound(), getX(),
                       textbuf_[getY() + getLowestBound()].length() - getX());
      } else {
        textbuf_.appendString("");
      }
      moveDown();
      moveStartString();
      changed_ = true;
      break;
    }
    case KEY_TAB: {
      for (int i = 0; i < 4; i++) {
        textbuf_.insertSymbol(getX(), getY() + getLowestBound(), ' ');
        moveRight();
      }
      break;
      changed_ = true;
    }
    default: {
      changed_ = true;
      textbuf_.insertSymbol(getX(), getY() + getLowestBound(),
                            (const char)input);
      moveRight();
      break;
    }
    }
    break;
  }
  }
}

void TextEditor::processConsole(int logic) {
  if (logic != 0) {
    int wtg = logic;
    while (wtg != KEY_CODE_ENTER) {
      wtg = getSymbol();
    }
    textbuf_.clear();
    adt.clearA();
    adt.curs_setA(1);
    return;
  }

  bool f = true;

  if (getNum(console_) > 0 && getNum(console_) < textbuf_.getBufferSize() ||
      getNum(console_) == 0) {
    setCursor(0, 0);

    lowestbound_ = 0;
    while (getY() + getLowestBound() < getNum(console_) - 1 &&
           getY() + getLowestBound() + 1 < textbuf_.getBufferSize()) {
      moveDown();
    }
    moveStartString();
    setMode(NAVIGATION_MODE);
  } else if (console_[0] == 'o' && console_[1] == ' ' &&
             (f = openFile(console_.substr(2)))) {
    setMode(NAVIGATION_MODE);
  } else if (console_[0] == 'w' && !writeFile()) {
    return;
  } else if (console_ == "h") {
    adt.clearA();
    adt.printwA(HELP_INFO1);
    adt.printwA(HELP_INFO2);
    adt.printwA(HELP_INFO3);
    adt.printwA(HELP_INFO4);
    adt.printwA(HELP_INFO5);
    adt.printwA("\nPress any key to continue.");
    adt.getchA();
    console_.clear();
    return;
  } else if (console_ == "x") {
    console_ = "w";
    processConsole();
    textbuf_.clear();
    setCursor(0, 0);
  } else if (console_ == "q!") {
    setMode(EXIT_MODE);
  } else if (console_ == "q" && !changed_) {
    setMode(EXIT_MODE);
  } else {
    if (f) {
      console_.append("\nUnavailable command!");
    }
    console_.append("\nPress any key to continue.");
    adt.clearA();
    printScreen();
    adt.getchA();
    console_.clear();
    return;
  }

  console_.clear();
  if (textbuf_.getBufferSize() > 0) {
    adt.moveA(getY() + getLowestBound(),
              textbuf_[getY() + getLowestBound()].length());
  } else {
    adt.moveA(0, 0);
  }
}

void TextEditor::deleteWord(void) {

l1:
  if (textbuf_[getY() + getLowestBound()][getX()] == ' ' &&
      getY() + getLowestBound() < textbuf_.getBufferSize()) {
  l3:
    int tmp = textbuf_[getY() + getLowestBound()].find(" ", getX() + 1);
    if (tmp > 0) {
      textbuf_.erase(getY() + getLowestBound(), getX(), tmp - getX());
    } else {
      textbuf_.erase(getY() + getLowestBound(), getX(),
                     textbuf_[getY() + getLowestBound()].length() - getX());
    }
  } else if (textbuf_[getY() + getLowestBound()][getX()] == '\0' &&
             getY() + getLowestBound() < textbuf_.getBufferSize() - 1) {
    int tmp = textbuf_[getY() + getLowestBound() + 1].find(" ");
    if (tmp > 0) {
      textbuf_.appendToString(getY() + getLowestBound(), " ");
      textbuf_.appendToString(
          getY() + getLowestBound(),
          textbuf_[getY() + getLowestBound() + 1].substr(0, tmp));
      textbuf_.erase(getY() + getLowestBound() + 1, 0, tmp + 1);
    } else {
      textbuf_.removeString(getY() + getLowestBound() + 1);
    }
  } else {
    if (getY() + getLowestBound() >= textbuf_.getBufferSize() ||
        textbuf_.getBufferSize() == 0) {
      goto l2;
    } else {
      if (getX() == 0 && getY() == 0) {

        goto l3;
      } else {
        moveLeft();
        goto l1;
      }
    }
  }

l2:
  return;
}

bool TextEditor::writeFile(void) {
  bool f = true;

  std::ofstream tmp;
  if (console_.length() > 2 && console_[1] == ' ') {
    tmp.open((console_.substr(2)).c_str());
    f = tmp.is_open();
  } else if (console_.length() == 1) {
    tmp.open(filename_.c_str());
    f = tmp.is_open();
  } else {
    f = false;
  }

  if (f) {
    for (int i = 0; i < textbuf_.getBufferSize(); i++) {
      if (i == textbuf_.getBufferSize() - 1) {
        tmp << textbuf_[i];
      } else {
        tmp << textbuf_[i] << std::endl;
      }
    }
    changed_ = false;
    setMode(NAVIGATION_MODE);
  } else {
    console_.append("\nIncorrect filename");
    console_.append("\nPress any key to continue.");
    adt.clearA();
    printScreen();
    adt.getchA();
    console_.clear();
  }

  return f;
}

void TextEditor::pasteClipboard(void) {
  if (getClipboard().length() <= 0) {
    return;
  }

  if (getClipboard()[0] == '\t') {
    setMode(INPUT_MODE);
    handleInput(KEY_CODE_ENTER);
    setMode(NAVIGATION_MODE);
  }

  if (textbuf_.getBufferSize() > 0) {
    if (textbuf_[getY() + getLowestBound()][getX()] == '\0' &&
        getX() + getClipboard().length() < COLS) {
      moveDown();
      moveStartString();
      textbuf_.appendToString(getY() + getLowestBound(), getClipboard());
      setCursor(getX() + getClipboard().length(), getY());
    } else if (textbuf_[getY() + getLowestBound()].length() +
                   getClipboard().length() <=
               COLS) {
      int b = 0;
      if (getX() > 0) {
        b++;
      }
      textbuf_.insertToString(getX() + b, getY() + getLowestBound(),
                              clipboard_);
      setCursor(getX() + getClipboard().length() + b, getY());
    }
  } else {
    textbuf_.appendString(clipboard_);
    moveEndString();
  }

  adt.clearA();
  adt.refreshA();
}

void TextEditor::copyString(void) {
  clipboard_.clear();
  clipboard_.shrink_to_fit();

  if (textbuf_.getBufferSize() <= 0 ||
      textbuf_[getY() + getLowestBound()] == "") {
    clipboard_.append(1, '\t');
  } else {
    clipboard_ = textbuf_[getY() + getLowestBound()];
  }
}

int TextEditor::getNum(MyString &arr) {
  int ret = 0;
  int dec = 1;
  for (int j = arr.length() - 1; j >= 0; j--) {
    ret += dec * (int)(arr[j] - '0');
    dec *= 10;
  }

  return ret;
}

void TextEditor::moveLastPage(void) {
  int cnt = getPageSize();
  int del = textbuf_.getBufferSize() / cnt;
  setCursor(0, 0);
  lowestbound_ = 0;
  while (getY() + getLowestBound() < del * cnt) {
    moveDown();
  }
  moveStartString();
}

void TextEditor::moveLeft(void) {
  if (getX() - 1 >= 0) {
    setCursor(getX() - 1, getY());
  } else if (getY() > 0) {
    moveUp();
    moveEndString();
  }
}

void TextEditor::moveRight() {
  if (textbuf_.getBufferSize() <= 0) {
    return;
  }

  if (getX() + 1 <= textbuf_[getY() + getLowestBound()].length()) {
    if (getX() + 1 < COLS) {
      setCursor(getX() + 1, getY());
    } else {
      textbuf_.appendString("");
      moveDown();
    }
  } else if (getY() + getLowestBound() + 1 < textbuf_.getBufferSize()) {
    moveDown();
    moveStartString();
  }
}

void TextEditor::moveUp(void) {
  if (getY() > 0) {
    if (getLowestBound() > 0) {
      lowestbound_--;
    } else {
      setCursor(getX(), getY() - 1);
    }
  } else {
    return;
  }

  if (getX() >= textbuf_[getY() + getLowestBound()].length()) {
    setCursor(textbuf_[getY() + getLowestBound()].length(), getY());
  }
}

void TextEditor::moveStartWord(void) {
  if (textbuf_.getBufferSize() <= 0) {
    return;
  }

  while (textbuf_[getY() + getLowestBound()][getX()] != ' ' &&
         textbuf_[getY() + getLowestBound()][getX()] != '\0') {
    if (getY() == 0 && getX() == 0) {
      return;
    }
    moveLeft();
  }
  moveLeft();
  while (textbuf_[getY() + getLowestBound()][getX()] != ' ' &&
         textbuf_[getY() + getLowestBound()][getX()] != '\0') {
    if (getY() == 0 && getX() == 0) {
      return;
    }
    moveLeft();
  }
}

void TextEditor::moveEndWord(void) {
  if (getY() + getLowestBound() >= textbuf_.getBufferSize()) {
    return;
  }

  while (getY() + getLowestBound() < textbuf_.getBufferSize() &&
         textbuf_[getY() + getLowestBound()][getX()] != ' ' &&
         textbuf_[getY() + getLowestBound()][getX()] != '\0') {
    moveRight();
  }
  moveRight();
  while (getY() + getLowestBound() < textbuf_.getBufferSize() &&
         textbuf_[getY() + getLowestBound()][getX()] != ' ' &&
         textbuf_[getY() + getLowestBound()][getX()] != '\0') {
    moveRight();
  }
}

void TextEditor::moveDown(void) {
  if (getY() + getLowestBound() + 1 >= textbuf_.getBufferSize()) {
    return;
  }

  if (getY() + 1 < LINES - 1 && getY() + 1 < textbuf_.getBufferSize()) {
    setCursor(getX(), getY() + 1);
  } else if (getLowestBound() + getY() < textbuf_.getBufferSize()) {
    lowestbound_++;
  }
  if (getX() >= textbuf_[getY() + getLowestBound()].length()) {
    setCursor(textbuf_[getY() + getLowestBound()].length(), getY());
  }
}

void TextEditor::isolateWord(void) {
  if (getClipboard().length() <= 1) {
    return;
  } else {
    int space = getClipboard().find(" ", getX());

    while (space > getX() && space < getClipboard().length()) {
      clipboard_.erase(getX(), space);
      space = getClipboard().find(" ", getX());
    }
  }
}

int TextEditor::getPageSize(void) {
  int curx = getX();
  int cury = getY();
  int curlb = getLowestBound();
  int cnt = 0;
  setCursor(0, 0);
  lowestbound_ = 0;
  while (getLowestBound() == 0 &&
         getY() + getLowestBound() < textbuf_.getBufferSize() - 1) {
    cnt++;
    moveDown();
  }
  setCursor(curx, cury);
  lowestbound_ = curlb;
  return cnt;
}

void TextEditor::moveEndString(void) {
  setCursor(textbuf_[getY() + getLowestBound()].length(), getY());
}

void TextEditor::moveStartString(void) { setCursor(0, getY()); }