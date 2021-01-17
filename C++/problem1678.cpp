class Solution {
public:
    string interpret(string command) {
        string ans;
        for (string::iterator it = command.begin(); it < command.end(); ++it)
        {
            if (*it == 'G')
            {
                ans.append("G");
            }
            else if (*it == '(')
            {
                ++it;
                if (*it == ')')
                {
                    ans += 'o';
                }
                while (*it != ')')
                {
                    // ans.append(*it);
                    ans += *it;
                    ++it;
                }
            }
        }
        return ans;
    }
};
