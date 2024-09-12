#ifndef MYSTRING_H
#define MYSTRING_H

#include "Main.h"

class MyString {
private:
  int capacity_;
  int size_;
  char *str_;

public:
  MyString(void);
  MyString(const char *str);
  MyString(const std::initializer_list<char> &list);
  MyString(const std::string &str);
  MyString(const char *str, int lim);
  MyString(int count, char c);
  MyString(const MyString &str);
  int slen(const char *str) const;
  char *scpy(const char *from, char *to, const int n);
  int length(void) const;
  int size(void) const;
  int capacity(void) const;
  char *data(void) const;
  char *c_str(void);
  void shrink_to_fit(void);
  void erase(const int index, const int count);
  MyString substr(const int index) const;
  MyString substr(const int index, const int count) const;
  int find(const char *str) const;
  int find(const char *str, const int index) const;
  int find(const std::string &str, const int index) const;
  int find(const std::string &str) const;
  void insert(const int index, const int count, const char c);
  void append(const int count, const char c);
  void insert(const int index, const std::string &str);
  void append(const std::string &str);
  void insert(const int index, const char *str);
  void append(const char *str);
  void insert(const int index, const char *str, const int count);
  void append(const char *str, const int index, const int count);
  void insert(const int index, const std::string &str, const int count);
  void append(const std::string &str, const int index, const int count);
  void replace(const int index, const int count, const char *str);
  void replace(const int index, const int count, const std::string &str);
  void clear(void);
  bool empty(void) const;
  void Destructor(void);
  friend MyString operator+(const MyString &str1, const MyString &str2);
  friend MyString operator+(const MyString &str1, const char *str2);
  friend MyString operator+(const MyString &str1, const std::string &str2);
  void operator+=(const MyString &str);
  void operator+=(const std::string &str);
  void operator=(const std::string &str);
  void operator=(const char *str);
  void operator=(const char c);
  const char &operator[](int i) const;
  bool operator>(const MyString &str) const;
  bool operator<(const MyString &str) const;
  bool operator==(const MyString &str) const;
  bool operator>=(const MyString &str) const;
  bool operator<=(const MyString &str) const;
  bool operator!=(const MyString &str) const;
};

std::ostream &operator<<(std::ostream &os, const MyString &str);
std::istream &operator>>(std::istream &is, MyString &str);

#endif