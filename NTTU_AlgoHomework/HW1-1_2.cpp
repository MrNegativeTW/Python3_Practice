// HWP1-1
// KevinLee
// 20180924
#include <cstdio>
#include <vector>
#include <map>
#include <cstring>
#include <algorithm>
using namespace std;

//採用合併排序法 (Merge sort) 進行排序
long long merge(int* arr, int* temp, int left, int mid, int right){
    int q, w, e; 
    long long inv_count = 0; 

    q = left; w = mid; e = left; 

    while ((q <= mid - 1) && (w <= right))  
    { 
        if (arr[q] <= arr[w]){ 
            temp[e++] = arr[q++]; 
        } else{
            temp[e++] = arr[w++]; 
            inv_count = inv_count + (mid - q);
        }
    }

    while (q <= mid - 1) temp[e++] = arr[q++]; 
    while (w <= right) temp[e++] = arr[w++]; 
    for (q=left; q <= right; q++) arr[q] = temp[q]; 
 
    return inv_count; 
}

//採用合併排序法 (Merge sort) 進行排序
long long merge_sort(int* arr, int* temp, int left, int right){
    int m; 
    long long inv_count = 0; 
    if (right > left){ 
        m = (right + left)/2; 
        inv_count = merge_sort(arr, temp, left, m); 
        inv_count += merge_sort(arr, temp, m+1, right); 
        inv_count += merge(arr, temp, left, m+1, right); 
    }
    return inv_count; 
}
 
int main(){
    // 執行次數
    int p;
    scanf("%d", &p);

    // 執行次數迴圈
    for(int a = 0; a<p; a++){
        // 待排序資料總量
        int n; scanf("%d", &n);
        // 待排序資料陣列
        int A[n];

        // 待排序資料寫入陣列
        for(int z = 0; z<n; z++){ 
            scanf("%d", &A[z]); 
        }

        // 下載更多記憶體
        int* B = (int *)malloc(n*sizeof(int));
       
        printf("Optimal train swapping takes %lld swaps.\n", merge_sort(A, B, 0, n-1)); 
    }
    return 0; 
}