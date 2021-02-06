class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        if (k == cardPoints.size())
        {
            return accumulate(cardPoints.begin(), cardPoints.end(), 0);
        }
        
        int m = cardPoints.size() - k;
        int sum_0 = accumulate(cardPoints.begin(), cardPoints.end(), 0), sum_ = sum_0;
        int tmp = 0, cache = 0;
        for (int i = 0; i < cardPoints.size() - m + 1; ++i)
        {

            // for (vector<int>::iterator it = cardPoints.begin() + i; it < cardPoints.begin() + i + m; ++it)
            // {
            //     cout << *it << ' ';
            // }
            // cout << endl;
            // for (int p = i; p < i + m; ++p)
            // {
            //     cout << cardPoints[p] << ' ';
            // }
            // cout << endl;

            if (i == 0)
            {
                // for (int j = i; j < i + m; ++j) //这样的写法，数组的长度就是 后索引 - 前索引
                // {
                //     tmp += cardPoints.at(j);
                // }
                tmp = accumulate(cardPoints.begin() + i, cardPoints.begin() + i + m, 0);
            }
            else
            {
                tmp -= cache;
                tmp += cardPoints[i + m - 1];
            }
            // cout << tmp << endl;
            sum_ = min(sum_, tmp);
            cache = cardPoints[i]; //这里不能重新定义cache，这是要保留上一轮的头元素；在python中，因为可以不显式定义，所以定义和重载是混淆的 //编译型语言，定义必须在前面声明
        }
        return sum_0 - sum_;

    }
};
