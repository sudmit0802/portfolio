#include "Main.h"

std::vector<MyString> TextBuffer::getStrings(void) const { return strings_; }

MyString TextBuffer::convertTabs(MyString &str) {
  int pos = str.find("\t");
  if (pos < 0) {
    return str;
  } else {
    str.replace(pos, 1, "    ");
    return convertTabs(str);
  }
}

void TextBuffer::insertString(MyString &str, int pos) {
  str = convertTabs(str);
  strings_.insert(strings_.begin() + pos, str);
}

void TextBuffer::clear(void) { strings_.clear(); }

void TextBuffer::nullString(int numstr) { strings_[numstr].clear(); }

void TextBuffer::replaceSymbol(int posy, int posx, const char c) {
  MyString tmp(1, c);
  strings_[posy].replace(posx, 1, tmp.c_str());
}

void TextBuffer::appendString(MyString str) {
  str = convertTabs(str);
  strings_.push_back(str);
}

void TextBuffer::removeString(int i) { strings_.erase(strings_.begin() + i); }

void TextBuffer::insertSymbol(int posx, int posy, const char c) {
  if (posy < strings_.size()) {
    strings_[posy].insert(posx, 1, c);
  } else {
    MyString tmp(1, c);
    appendString(tmp);
  }
}

void TextBuffer::appendToString(int numstr, MyString str) {
  strings_[numstr].append(str.data());
}

void TextBuffer::insertToString(int posx, int posy, MyString &str) {
  strings_[posy].insert(posx, str.c_str());
}

void TextBuffer::erase(int numstr, int pos, int count) {
  strings_[numstr].erase(pos, count);
}

void TextBuffer::deleteSymbol(int posx, int posy) {
  strings_[posy].erase(posx - 1, 1);
}

int TextBuffer::getBufferSize(void) const { return strings_.size(); }

MyString TextBuffer::operator[](int i) const { return strings_[i]; }
