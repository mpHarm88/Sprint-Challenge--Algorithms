
'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    count = 0
   
    if len(word) <= 1:
        return count

    # if the first 2 letters are "th" then add 1 to count
    if word[:2] == "th":
        count += 1
        # recursively add count and call function with one less letter
        return count + count_th(word[1:])
    else:
        return count_th(word[1:])