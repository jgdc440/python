def count_letters(word_list):
    """ See question description """
    
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for letter in ALPHABET:
        letter_count[letter] = 0
        
    for word in word_list:
      for char in word:
        letter_count[char] += 1
    
    max_value = 0
    max_char = 'a'
    
    for k in letter_count.keys():
      if (letter_count[k] > max_value):
        max_value = letter_count[k]
        max_char = k
        
    return max_char, max_value
    
monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"

monty_words = monty_quote.split(" ")

print (count_letters(monty_words))