#include "pch.h"
#include "framework.h"
#include <iostream>
#include <cstring>
#include <cassert>
#include "MyString.h"



/*--------------------------------------------------------------------------Information methods--------------------------------------------------------------------------*/
int MyString::length() const
{
    return size_;
}

int MyString::size() const
{
    return size_;
}

int MyString::capacity() const
{
    return capacity_;
}

char* MyString::data() const
{
    return str_;
}

int MyString::slen(const char* str) const
{
    int j = 0;
    while (str[j] != '\0')
    {
        j++;
    }
    return j;
}

bool MyString::empty() const
{
    if (size_ == 0 && str_[0] == '\0')
    {
        return true;
    }
    else
    {
        return false;
    }
}
/*--------------------------------------------------------------------------Information methods--------------------------------------------------------------------------*/






/*--------------------------------------------------------------------------Constructors--------------------------------------------------------------------------*/
MyString::MyString(void)
{
    size_ = 0;
    capacity_ = 1;
    str_ = new char[capacity_];
    str_[0] = '\0';
}

MyString::MyString(int count, char c)
{
    capacity_ = count + 1;
    size_ = count;
    str_ = new char[capacity_];
    for (int i = 0; i < capacity_ - 1; i++)
    {
        str_[i] = c;
    }
    str_[capacity_ - 1] = '\0';
}

MyString::MyString(const std::initializer_list<char> &list)
{
    int cnt = 0;

    for(auto &element : list)
    {
	    cnt++;
    }

    size_= cnt ;
    capacity_ = cnt + 1;
    str_ = new char[capacity_];

    cnt = 0;

    for(auto &element : list)
    {
        if (cnt < size_)
        {
            str_[cnt] = element;
        }
         ++cnt;
    }

    str_[size_]='\0';
}

MyString::MyString(const char* str, int lim)
{
    size_ = lim;
    capacity_ = size_ + 1;
    str_ = new char[capacity_];
    scpy(str, str_, lim);
    str_[size_]= '\0';
}

MyString::MyString(const char* str) : MyString(str, slen(str)) {}

MyString::MyString(const std::string& str) : MyString(str.data()) {}

MyString::MyString(const MyString &str) : MyString(str.data()) {}
/*--------------------------------------------------------------------------Constructors--------------------------------------------------------------------------*/






/*--------------------------------------------------------------------------Functional methods--------------------------------------------------------------------------*/
char* MyString::scpy(const char* from, char* to, const int n)
{
    for (int i = 0; i < n; i++)
    {
        to[i] = from[i];
    }
    to[n] = '\0';
    return to;
}

char* MyString::c_str()
{
    str_[size_]='\0';
    return str_;
}

void MyString::shrink_to_fit()
{
    MyString tmpstr(str_);
    str_ = new char[tmpstr.capacity_];
    capacity_ = tmpstr.capacity_;
    scpy(tmpstr.data(), str_, tmpstr.size());
}

void MyString::erase(const int index, const int count)
{
    int tmp = index + count;
    MyString tmpstr;
    tmpstr.clear();
    tmpstr.append(str_, 0, index);
    tmpstr.append(str_, tmp, size_- tmp);
    clear();
    append(tmpstr.data());
}

MyString MyString::substr(const int index) const
{
    MyString ret(str_);
    ret.erase(0,index);
    return ret;
}

MyString MyString::substr(const int index, const int count) const
{
    MyString ret;
    ret.clear();
    ret.append(str_, index, count);
    return ret;
}

int MyString::find(const char* str, const int index) const
{
    int cnt = 0;

    for (int i = index; i < size_; i++)
    {
        if (str_[i] == str[cnt])
        {
            cnt++;
        }
        else
        {
            cnt = 0;
        }
        if (cnt == slen(str))
        {
            return i - cnt + 1;
        }
    }
    return -1;
}

int MyString::find(const char* str) const
{
   return find(str, 0);
}
int MyString::find(const std::string &str) const
{
   return find(str, 0);
}

int MyString::find(const std::string &str, const int index) const
{
    return find(str.data(), index);
}

void MyString::insert(const int index, const char* str, const int count)
{
    assert(index <= size_);
    assert(count <= slen(str));
    size_ += count;
    if (size_ + 1 > capacity_)
    {
        capacity_ = size_ + 1;
        char* tmpstr1 = new char[index + 1];
        char* tmpstr2 = new char[count + 1];
        char* tmpstr3 = new char[size_ - (index + count) + 1];
        scpy(str_, tmpstr1, index);
        scpy(str, tmpstr2, count);
        for (int i = index; i < size_ - count; i++)
        {
            tmpstr3[i - index] = str_[i];
        }
        str_ = new char[capacity_];
        scpy(tmpstr1, str_, index);
        for (int i = index; i < index + count; i++)
        {
            assert(index + count < capacity_);
            if(index + count < capacity_)
                str_[i] = tmpstr2[i - index];
        }
        for (int i = index + count; i < size_; i++)
        {
            str_[i] = tmpstr3[i - (index + count)];
        }
    }
    else
    {
        char* tmpstr = new char[size_ - index + 1];
        scpy(str, tmpstr, count);
        for (int i = count; i < size_ - index; i++)
        {
            tmpstr[i] = str_[i - count + index];
        }
        for (int i = index; i < size_; i++)
        {
            str_[i] = tmpstr[i - index];
        }
    }
    str_[size_] = '\0';
}

void MyString::insert(const int index, const int count, const char c)
{
    MyString tmp(count, c);
    insert(index, tmp.data());
}

void MyString::insert(const int index, const std::string& str)
{
    insert(index, str.data(), str.length());
}

void MyString::insert(const int index, const char* str)
{
    insert(index, str, slen(str));
}

void MyString::insert(const int index, const std::string &str, const int count)
{
    insert(index, str.data(), count);
}

    
void MyString::append(const char* str, const int index, const int count)
{
    char* tmpstr;
    tmpstr = new char[count + 1];

    for (int i = index; i < count + index; i++)
    {
        tmpstr[i - index] = str[i];
    }
    tmpstr[count] = '\0';

    insert(size_, tmpstr);
}

void MyString::append(const std::string& str, const int index, const int count)
{
    append(str.data(), index, count);
}

void MyString::append(const int count, const char c)
{
    insert(size_, count, c);
}

void MyString::append(const std::string& str)
{
    insert(size_, str);
}

void MyString::append(const char* str) 
{
    insert(size_, str);
}

void MyString::replace(const int index, const int count, const char* str)
{
    erase(index, count);
    insert(index, str);
}

void MyString::replace(const int index, const int count, const std::string &str)
{
    replace(index, count, str.data());
}

void MyString::clear()
{
    for(int i = 0; i<size_; i++)
    {
        str_[i] = '\0';
    }
    size_ = 0;
}

void MyString::Destructor()
{
    delete str_;
    str_ = nullptr;
    size_ = 0;
    capacity_ = 0;
}
/*--------------------------------------------------------------------------Functional methods--------------------------------------------------------------------------*/




/*--------------------------------------------------------------------------Overloaded operators--------------------------------------------------------------------------*/
MyString operator+(const MyString& str1, const MyString& str2)
{
    MyString tmp(str1);
    tmp.append(str2.data());
    return tmp;
}

MyString operator+(const MyString& str1, const char* str2)
{
    MyString tmp(str2);
    return operator+(str1, tmp);
}

MyString operator+(const MyString& str1, const std::string &str2)
{
    MyString tmp(str2);
    return operator+(str1, tmp);
}

void MyString::operator+=(const MyString& str)
{
    append(str.data());
}

void MyString::operator+=(const std::string &str)
{
    MyString tmp(str);
    operator+=(tmp);
}

void MyString::operator=(const std::string &str)
{
    operator=(str.data());
}

void MyString::operator=(const char* str)
{
    clear();
    append(str);
}

void MyString::operator=(const char c)
{
    clear();
    append(1, c);
}

const char & MyString::operator[](int i) const
{
    return str_[i];
}

bool MyString::operator>(const MyString& str) const
{
    for(int i = 0; i<=size_; i++)
    {
        if(str_[i]>str.str_[i])
        {
            return 1;
        }
        if(str_[i]<str.str_[i])
        {
            return 0;
        }
    }
    return 0;
    
}

bool MyString::operator<(const MyString& str) const
{
        for(int i = 0; i<=size_; i++)
    {
        if(str_[i]<str.str_[i])
        {
            return 1;
        }
        if(str_[i]>str.str_[i])
        {
            return 0;
        }
    }
    return 0;
}

bool MyString::operator==(const MyString& str) const
{
    if(str.size_!=size_)
    {
        return 0;
    }
    else
    {
        int i = 0;
        while(str.str_[i]==str_[i])
        {
            i++;
            if(i>size_)
            {
                return 1;
            }
        }
        return 0;
    }
}

bool MyString::operator >=(const MyString& str) const
{
    return !operator<(str);
}

bool MyString::operator <=(const MyString& str) const
{
    return !operator>(str);
}

    
bool MyString::operator !=(const MyString& str) const
{
    if(operator==(str))
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
/*--------------------------------------------------------------------------Overloaded operators--------------------------------------------------------------------------*/




/*--------------------------------------------------------------------------Free functions--------------------------------------------------------------------------*/
std::ostream& operator<<(std::ostream &os, const MyString& str)
{
   return os << str.data();
}

std::istream& operator>>(std::istream &is, MyString& str)
{
    str.clear();
    char c;
    is.get(c);
    if(c == '\n')
    {
        is.get(c);
    }
    while(is && c != '\n')
    {
        str.append(1, c);
        is.get(c);
    }
    return is;
}
/*--------------------------------------------------------------------------Free functions--------------------------------------------------------------------------*/