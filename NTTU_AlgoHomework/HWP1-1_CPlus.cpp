#include<iostream>
#include<vector>
using namespace std;
int main(){
	int ts;cin>>ts;
	while(ts--){
		int n,ans=0;cin>>n;
		vector<int> a(n);
		for(int k=0;k<n;k++)cin>>a[k];
		for(int k=0;k<n;k++){
			for(int h=0;h<k;h++){
				if(a[h]>a[k])ans++;
			}
		}
		cout<<"Optimal train swapping takes "<<ans<<" swaps."<<endl;
	}
} 