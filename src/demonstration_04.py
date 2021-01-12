"""
Challenge #4:
​
Create a function that changes specific words into emoticons. Given a sentence
as a string, replace the words `smile`, `grin`, `sad`, and `mad` with their
corresponding emoticons.
​
word -> emoticon
---
smile -> :D
grin -> :)
sad -> :(
mad	-> :P
​
Examples:
- emotify("Make me smile") ➞ "Make me :D"
- emotify("Make me grin") ➞ "Make me :)"
- emotify("Make me sad") ➞ "Make me :("
​
Notes:
- The sentence always starts with "Make me".
- Try to solve this without using conditional statements like if/else.
"""
​
​
def emotify(txt):
	# Make dictionary that maps words to emojis
	emoji_map = {
		"smile": ":D",
		"grin": ":)",
		"sad": ":(",
		"mad": ":P"
	}
​
	# Pull the last word off the text
	word = txt[8:]  # 8 is length of "Make me "
​
	return "Make me " + emoji_map[word]
​
print(emotify("Make me smile")) # ➞ "Make me :D"
print(emotify("Make me grin")) # ➞ "Make me :)"
print(emotify("Make me sad")) # ➞ "Make me :("
print(emotify("Make me mad")) # ➞ "Make me :P"
