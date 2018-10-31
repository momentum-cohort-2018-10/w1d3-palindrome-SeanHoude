import re


pal_1 = "stunt nuts"
pal_2 = "Lisa Bonet ate no basil."
pal_3 = "A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama!"
pal_4 = "Doc, note, I dissent. A fast never prevents a fatness. I diet on cod."
pal_5 = "Madam I'm Adam"
pal_6 = "When a problem comes along, you can whip it, whip it good"


def break_down(palindrome):
    """
    Given a string, ignore case, strip punctuation and spaces, reverse the string, and determine if
    the original stripped string == reversed string.
    """
    clean_string = re.sub(r'[^A-Za-z]', "", palindrome).lower()
    # clean_string = palindrome.lower()
    reverse_string = clean_string[::-1]
    print(f"The sentence :  '{palindrome}'...")
    if clean_string == reverse_string:
        print("is a true palindrome!")
    else:
        print("is NOT a palindrome, even though it may have seemed that way.")


break_down(pal_1)
break_down(pal_2)
break_down(pal_3)
break_down(pal_4)
break_down(pal_5)
break_down(pal_6)
break_down(input("Please enter a string to test if it is a palindrome: "))