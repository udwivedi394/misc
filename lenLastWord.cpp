int lengthOfLastWord(const string A){
    int leng = 0,  i=0, n;
    bool current=0;

    n = A.length();
    while (i<n){
        if (A[i]==' '){
            if (len>0){
                current = 0;}}
        else
        {
            if (current==0)
            {
                len = 1;
                current = 1;
            }
            else{
                len += 1;}
        }
        i += 1;
    }
    return len;
}

int main()
{
    string A;
    return 0;
}
