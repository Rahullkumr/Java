/*
6 6 6 6 6 6
4 4 4 4
2 2
*/

#include <iostream>
using namespace std;

int main() 
{
    int value = 6;
    int arr[3] = {6,4,2};
    for(int i=0; i < 3; i++){
      for(int j = 0; j < arr[i]; j++){
        cout<<value<<" ";
      }
      value = value - 2;
      cout<<endl;
    }
    return 0;
}