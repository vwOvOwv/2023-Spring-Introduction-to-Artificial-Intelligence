#include<iostream>
#include<algorithm>
#include<iomanip>
using namespace std;

double dp[100][100000]={0};
int main(){
    int n;
    double m;
    cin>>n>>m;
    int mm=int(m*100);
    double w,p;
    for(int i=1;i<=n;i++){
        cin>>w>>p;
        int ww=int(w*100);
        for(int j=0;j<=mm;j++){
            if(j>=ww)
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-ww]+p);
            else
                dp[i][j]=dp[i-1][j];
        }
    }
    cout<<fixed<<setprecision(5)<<dp[n][mm]<<endl;
    return 0;
}