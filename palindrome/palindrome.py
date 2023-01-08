
def palindrome (word):
    """Returns if the word is a palidrome."""
    
    for i in range(0, int(len(word)/2)):
        if word[i] != word[len(word)-i-1]:
            return False
    return True
my_word = "kajak"
ans = palindrome (my_word) 
print(ans)