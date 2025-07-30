class Solution {
public:
    bool isValid(string s) {
    
    //stack for open parenthesis
    stack<char> stk;
    // {k,v}
    unordered_map<char, char> par = {
        {')', '('},
        {']','['},
        {'}','{'}
    };

    for(char c : s){
        // if we hit a closed parentheses
        if (par.count(c)){ // par.count(c) returns true if c is a key in par
            if (stk.empty() || stk.top() != par[c]){
                return false;
            }
            stk.pop();
        }
        else{
            stk.push(c);
        }
    }
    return stk.empty();
}
        
};