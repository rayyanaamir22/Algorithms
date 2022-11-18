#include <iostream>

int binarySearch(int arr[], int target, int max, int min) {
    while(min<=max){
        int mid = (max+min)/2;
        if (arr[mid]>target){ // Access value in address of arr
            max = mid-1;
        }else if(arr[mid]<target){
            min = mid+1;
        }else{
            return mid;
        }
    }
    return -1; // Not found
}

int main(){
    int myArr[] = {1, 3, 16, 42, 45, 300, 987};
    int lengthOfArr = sizeof(myArr)/sizeof(myArr[0]);
    int target = 16;
    int index = binarySearch(myArr, target, lengthOfArr, 0);
    if(index!=-1){
        std::cout << "Target " << target << " is present at index " << index << ".\n";
    }else{
        std::cout << "Target " << target << " is not present in the array.\n";
    }
    return 0;
}