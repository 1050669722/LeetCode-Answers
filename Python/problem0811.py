from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        for cpdomain in cpdomains:
            tmp = cpdomain.split()
            num, domains = int(tmp[0]), tmp[1]
            domains = domains.split('.')
            tmp = ''
            domains.reverse()
            for domain in domains:
                # tmp.append(domain+'_')
                tmp += (domain+'_')
                try:
                    d[tmp] += num
                except:
                    d[tmp] = num
        ans = []
        for key, value in d.items():
            key = key.split('_')
            key.reverse()
            key = '.'.join(key)
            key = key[1:]
            ans.append(str(value)+' '+key)
        return ans


