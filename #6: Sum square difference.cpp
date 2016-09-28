#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
 
int main() {
    int T,i,j=0,num;
    long long *ans,S,SOP;
    cin>>T;
    ans=(long long*)malloc(T*sizeof(long long)); 
    while(T--){
        cin>>num;
        SOP=S=0;
        for(i=1;i<=num;i++){
            SOP+=i*i;
            S+=i;
        }
        S=S*S;
        ans[j]=abs(SOP-S);
        j++;
    }
    for(i=0;i<j;i++){
        cout<<ans[i]<<endl;
    }
}
