

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
    
    for current_len in range(len(s)):
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

    print(palindromes_dict)


def check_match_helper(odd, even):


def check_match(str):

    if len(str) == 0:
        return True
    
    

    # str = "door"
    odd_substring = str[0::2]
    even_substring = str[1::2]


    print(odd_substring)
    print(even_substring)



if __name__ == '__main__':

	# s = 'AbbAcaBBa'
	# get_palindrom_dict(s)

    s= "door"
    check_match(s)





