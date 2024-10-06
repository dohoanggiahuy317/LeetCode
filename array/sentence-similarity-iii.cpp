    inline static vector<string> toStringVec(string s) {
        vector<string> ans;
        const char sep[2] = " ";
        char str[101];
        strcpy(str, s.c_str());//to C-string
        char* token;

        token = strtok(str, sep);

        while (token != NULL) {
            ans.push_back(string(token));// to C++ string
            token = strtok(NULL, sep);
        }
        return ans;
    }