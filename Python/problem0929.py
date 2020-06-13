# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 09:07:39 2019

@author: ASUS
"""

class Solution:
    def numUniqueEmails(self, emails: list) -> int:
        for k in range(len(emails)):
            ind = emails[k].index('@')
            stack = []
            p = 0
            while p < len(emails[k]):
                if emails[k][p] == '.':
                    p += 1
                elif p == ind:#emails[k][p] == '@':
                    break
                elif emails[k][p] == '+':
                    while p != ind:#emails[k][p] != '@':
                        p += 1
                else:
                    stack.append(emails[k][p])
                    p += 1
            stack += emails[k][p:]
            emails[k] = ''.join(stack)
        return len(set(emails))
            
class Solution:
    def numUniqueEmails (self, emails) -> int:
        def get_real_email (email: str):
            parts = email.split('@')
            real = parts[0].split('+')
            return real[0].replace('.', '') + "@" + parts[1]
        return len(set(map(get_real_email, emails)))  
    
solu = Solution()
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(solu.numUniqueEmails(emails))