class Solution {
public:
    bool isCircularSentence(string s) {
        vector<string> v;
        int i=0;
        s+=' ';
        for(int i=0;i<s.size();i++){
            string str="";
            while(s[i]!=' '){
                str+=s[i];
                i++;
            }
            v.push_back(str);
        }
        // for(auto s:v)cout<<s<<" ";
        int n=v.size();
        for(int i=0;i<n-1;i++){
            string s1=v[i];
            string s2=v[i+1];
            if(s1[s1.size()-1]!=s2[0])
                return false;
        }
        if(v[n-1][v[n-1].size()-1]== v[0][0])return true;
        
        return false;
    }
};