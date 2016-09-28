#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
 
int main() {
    int T,i,j,flag,mflag,num,ans[10],z=0;
    cin>>T;
    while(T--){
        cin>>num;
        flag=0;
        j=1;
        while(j){
            mflag=0;
            for(i=1;i<=num;i++){
                
                if(j%i!=0){
                    mflag=1;
                    break;
                }
                
            
            
            }
            if(mflag==0){
                ans[z]=j;
                z++;
                flag=1;
                break;
            }
            if(flag==0)
            j++;
            else
            j=0;
        }
        
    }
    for(i=0;i<z;i++){
        cout<<ans[i]<<endl;
    }
   
}
