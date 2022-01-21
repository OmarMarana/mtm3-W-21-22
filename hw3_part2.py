

def get_palindrom_dict_helper(s):
    
    palindromes = []
    for start in range(len(s)):
        left = start
        right = start
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.append(s[left: right + 1])
            left = left - 1
            right = right + 1
		
        left = start
        right = start+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.append(s[left: right + 1])
            left = left - 1
            right = right + 1
    
    return palindromes



def get_palindrom_dict(s):

    palindromes_dict = {}
    palindromes = get_palindrom_dict_helper(s)
    help_list = [0]*(len(s)+1)
    
    for current_len in range(len(s) + 1):
        if current_len == 0:
            continue
        for palindrome in palindromes:
            if(len(palindrome)== current_len):
                help_list[current_len]+=1
                if help_list[current_len]==1: 
                    palindromes_dict[current_len] = []
                    palindromes_dict[current_len].append(palindrome)
                else:
                    palindromes_dict[current_len].append(palindrome)

    return palindromes_dict


def letter_already_exist(dict,letter):
    for k in dict.keys():
        if k==letter:
            return True
    return False

def check_match_helper(odd, even):
    
    dict = {}
    for i in range(len(odd)):
        if(letter_already_exist(dict, odd[i])):
            continue
        dict[odd[i]] = even[i]

    return dict


def check_match(str):

    if len(str) == 0:
        return True
    
    if len(str) % 2 == 1:
        return False
    
    odd_substring = str[0::2]
    even_substring = str[1::2]

    dict = check_match_helper(odd_substring,even_substring)

    tmp_str = ""

    for i in range(len(odd_substring)):
        tmp_str += dict[odd_substring[i]]

    if tmp_str == even_substring:
        return True
    else:
        return False


