# O(n) - time | O(n) - space : where n is the length of the string
def reverseWordsInString(string):
	# Keeps track of all the words and white spaces in the string 
	wordsInString = []
	
	# keeps track of the start of a word in the string 
	startOfWord = 0
	
	for idx in range(len(string)):
		character = string[idx]
		
		if character == " ":
			wordsInString.append(string[startOfWord: idx])
			startOfWord = idx
		elif string[startOfWord] == " ":
			wordsInString.append(" ")
			startOfWord = idx 
			
	wordsInString.append(string[startOfWord: ])
	
	reverseList(wordsInString)
	return "".join(wordsInString)

def reverseList(list):
	start, end = 0, len(list) - 1
	while start < end:
		list[start], list[end] = list[end], list[start]
		start += 1
		end -= 1