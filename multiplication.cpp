#include<bits/stdc++.h>

using namespace std;
	
int main()
{
	char a=14,b=14;
	char new_overlap=0, overlap=0;
	char last = 0;

	for(int i=0; i<8; i++)
	{
		if ((a>>i)&1 >0)
		{
		new_overlap = b>>(8-i);
		last = last|(b<<i)|overlap;
		overlap = new_overlap;
		cout<<"i:"<<i<<"last:"<<unsigned(last)<<endl;
		}
	}
	cout<<"a:"<<unsigned(a)<<" b:"<<unsigned(b)<<endl;
	cout<<unsigned(last)<<endl;
	return 0;
}
