/*
    Compile: (g++ -o executableFileName sourceCodeFilename.cpp)          ==> generate (executableFileName) file
    Run:     (./executableFileName)
    -o means output file
*/


//  1. Write a program to find the Factorial of a given number using Recursion.

#include<iostream>
using namespace std;

// recursive function for finding factorial 
int fact(int n){
    if (n == 0 || n == 1){
        return 1;
    }
    if (n >= 2){
        return (n * fact(n - 1));
    }
}

int main(){

    int num;
    cout<<"Enter number to get factorial: ";
    cin>>num;

    if(num < 0){
        cout<<"Enter positive number";
    }
    else{
        int factorial = fact(num);
        cout<<"Factorial of "<<num<<": "<<factorial;
    }

    

    cout<<endl;
    return 0;
}