#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int isvalid(long num){
    for(int i=999;i>101;i--)
        if((num%i==0)&&(num/i<1000))return 1;
    return 0;
}
        
 
int main() {
   long A[900];
   int T,i,j,k,z=0,num,ans[100];
   cin>>T;
    for(i=1;i<10;i++){
       for(j=0;j<10;j++){
           for(k=0;k<10;k++){
               num=(((((((((10*i)+j)*10)+k)*10)+k)*10)+j)*10)+i;
               if(isvalid(num)){
                   A[z]=num;
                   z++;
               }
           }
           
       }
   }
   j=0;
   while(T--){
       cin>>num;
       for(i=z-1;i>=0;i--){
           if(A[i]<num){
               ans[j]=A[i];
               j++;
               break;
           }          
        } 
    }
    for(i=0;i<j;i++){
        cout<<ans[i]<<endl;
    }
}
