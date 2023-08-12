/*
    Compile: (g++ -o executableFileName sourceCodeFilename.cpp)          ==> generate (executableFileName) file
    Run:     (./executableFileName)
    -o means output file
*/

// 3. Write a program to check if a given year is a leap year.
// Leap Year: a year divisible by 4 but not by 100 until also divisible by 400

#include<iostream>
using namespace std;

bool is_leap(int y){
    if(y % 4 == 0){
        if(y % 100 == 0){
            if(y % 400 == 0){
                return true;
            }
            else
                return false;
        }
        else{
            return true;
        }
    }
    else{
        return false;
    }
}

int main(){
    int year;

    cout<<"Enter year to check leap: ";
    cin>>year;
    if(year <= 0){
        cout<<"Enter valid year";
    }
    else{
        if(is_leap(year)){
            cout<<year<<" is leap year";
        }
        else{
            cout<<year<<" is not leap year";
        }
    }

    cout<<endl;
    return 0;
}