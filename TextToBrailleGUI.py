from tkinter import *

root = Tk()
root.title('Braille Translator')
root.geometry("450x200")
# create the labels for the GUI
title_label = Label(root, text="Braille Translator", font=("Helvetica", 20))
title_label.place(x=130,y=0)

# create a label and text entry box
text_label = Label(root, text="Text:")
text_entry = Entry(root, width=50)
text_label.place(x=20,y=75)
text_entry.place(x=100,y=75)

# create a label and text entry box
braille_label = Label(root, text="Braille:")
braille_entry = Entry(root, width=50)
braille_label.place(x=20,y=105)
braille_entry.place(x=100,y=105)
# create a function to convert text to Braille

alphaBraille = ['⠁', '⠃', '⠉', '⠙', '⠑', '⠋', '⠛', '⠓', '⠊', '⠚', '⠅', '⠇',
                '⠍', '⠝', '⠕', '⠏', '⠟', '⠗', '⠎', '⠞', '⠥', '⠧', '⠺', '⠭', '⠽', '⠵', ' ']
numBraille = ['⠼⠁', '⠼⠃', '⠼⠉', '⠼⠙', '⠼⠑', '⠼⠋', '⠼⠛', '⠼⠓', '⠼⠊', '⠼⠚']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
puntuation = [',', ';', ':', '.', '?', '!', ';', '(', ')', '/', '-']
puntuationBraille = ['⠂', '⠆', '⠒', '⠲', '⠦', '⠖', '⠐⠣', '⠐⠜', '⠸⠌', '⠤']
character = ['&', '*', '@', '©', '®', '™', '°', ]
characterBraille = ['⠈⠯', '⠐⠔', '⠈⠁', '⠘⠉', '⠘⠗', '⠘⠞', '⠘⠚', ]


def translate_text():
	# get the text from the text entry box
	text = text_entry.get()

	# create an empty string to store the Braille
	braille = ""

	# loop through each letter in the text
	for letter in text:
		# check if the letter is in the alphabet list
		if letter in alphabet:
			# get the index of the letter in the alphabet list
			index = alphabet.index(letter)
			# get the corresponding Braille character from the alphaBraille list
			braille_letter = alphaBraille[index]
			# add the Braille character to the Braille string
			braille += braille_letter
		# check if the letter is in the numbers list
		elif letter in nums:
			# get the index of the number in the numbers list
			index = nums.index(letter)
			# get the corresponding Braille character from the numBraille list
			braille_number = numBraille[index]
			# add the Braille character to the Braille string
			braille += braille_number
		# check if the letter is in the punctuation list
		elif letter in puntuation:
			# get the index of the punctuation mark in the punctuation list
			index = puntuation.index(letter)
			# get the corresponding Braille character from the puntuationBraille list
			braille_puntuation = puntuationBraille[index]
			# add the Braille character to the Braille string
			braille += braille_puntuation
		# check if the letter is in the character list
		elif letter in character:
			# get the index of the character in the character list
			index = character.index(letter)
			# get the corresponding Braille character from the characterBraille list
			braille_character = characterBraille[index]
			# add the Braille character to the Braille string
			braille += braille_character
		# check if the letter is a space
		elif letter == " ":
			# add a space to the Braille string
			braille += " "
	# insert the Braille string into the Braille entry box
	braille_entry.insert(0, braille)

# create a function to convert Braille to text


# def translate_braille():
# 	# get the text from the Braille entry box
# 	braille = braille_entry.get()
#
# 	# create an empty string to store the text
# 	text = ""
#
# 	# loop through each character in the Braille
# 	for character in braille:
# 		# check if the character is in the alphaBraille list
# 		if character in alphaBraille:
# 			# get the index of the character in the alphaBraille list
# 			index = alphaBraille.index(character)
# 			# get the corresponding letter from the alphabet list
# 			letter = alphabet[index]
# 			# add the letter to the text string
# 			text += letter
# 		# check if the character is in the numBraille list
# 		elif character in numBraille:
# 			# get the index of the character in the numBraille list
# 			index = numBraille.index(character)
# 			# get the corresponding number from the numbers list
# 			number = nums[index]
# 			# add the number to the text string
# 			text += number
# 		# check if the character is in the punctuationBraille list
# 		elif character in puntuationBraille:
# 			# get the index of the character in the punctuationBraille list
# 			index = puntuationBraille.index(character)
# 			# get the corresponding punctuation mark from the punctuation list
# 			punctuation = puntuation[index]
# 			# add the punctuation mark to the text string
# 			text += punctuation
# 		# check if the character is in the characterBraille list
# 		elif character in characterBraille:
# 			# get the index of the character in the characterBraille list
# 			index = characterBraille.index(character)
# 			# get the corresponding character from the character list
# 			character_text = character[index]
# 			# add the character to the text string
# 			text += character_text
# 		# check if the character is a space
# 		elif character == " ":
# 			# add a space to the text string
# 			text += " "
#
# 	# insert the text string into the text entry box
# 	text_entry.insert(0, text)


# create the submit button
submit_btn = Button(root, text="Submit", command=lambda: [translate_text()])
submit_btn.place(x=220,y=150)

# create the clear button
clear_btn = Button(root, text="Clear", command=lambda: [
                   text_entry.delete(0, END), braille_entry.delete(0, END)])
clear_btn.place(x=300, y=150)


root.mainloop()
