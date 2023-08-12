/*
    Compile: (g++ -o executableFileName sourceCodeFilename.cpp)          ==> generate (executableFileName) file
    Run:     (./executableFileName)
    -o means output file
*/

// 2. Write a program to sort the elements of an array in descending order without using built-in functions.

#include<iostream>
using namespace std;

int main(){
    int arr[] = {6, 2, 9, 12, 3};

    for(int i = 0; i < 5; i++){
        for(int j = i+1; j < 5; j++){
            if(arr[i] < arr[j]){
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    cout<<"After sorting in descending order\n ";
    for(int element = 0; element < 5; element++){
        cout<<arr[element]<<" ";
    }

    cout<<endl;
    return 0;
}