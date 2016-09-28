#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int T;
    cin>>T;
    while(T--){
        int N,K,prod=0;
        cin>>N>>K;
        char t[N];
        int A[N];
        cin>>t;
        
        for(int i=0;i<N;i++){
            A[i]=t[i]-48;
            
        }
       /* for(int i=0;i<N;i++){
            cout<<A[i];
            
        }*/
        
        for(int i=0;i<N-K;i++){
            int p=1;
            for(int j=0;j<K;j++){
                p*=A[i+j];
            }
            if(p>prod) prod=p;
        }
        cout<<prod<<endl;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
