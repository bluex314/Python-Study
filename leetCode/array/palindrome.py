# https://leetcode.com/problems/palindromic-substrings/


def find_sub_strings(s):
    sub_arr_pali = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            temp = s[i:j+1]
            if temp == temp[::-1]:
                sub_arr_pali.append(temp)
    return sub_arr_pali




if __name__=='__main__':
    s = "abc"
    sub = find_sub_strings(s)
    print(sub)