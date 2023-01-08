alphaBraille = ['⠁', '⠃', '⠉', '⠙', '⠑', '⠋', '⠛', '⠓', '⠊', '⠚', '⠅', '⠇','⠍', '⠝', '⠕', '⠏', '⠟', '⠗', '⠎', '⠞', '⠥', '⠧', '⠺', '⠭', '⠽', '⠵', ' ']
numBraille = ['⠼⠁', '⠼⠃', '⠼⠉', '⠼⠙', '⠼⠑', '⠼⠋', '⠼⠛', '⠼⠓', '⠼⠊', '⠼⠚']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
puntuation = [',', ';', ':', '.', '?', '!', ';', '(', ')', '/', '-']
puntuationBraille = ['⠂', '⠆', '⠒', '⠲', '⠦', '⠖', '⠐⠣', '⠐⠜', '⠸⠌', '⠤']
character = ['&', '*', '@', '©', '®', '™', '°', ]
characterBraille = ['⠈⠯', '⠐⠔', '⠈⠁', '⠘⠉', '⠘⠗', '⠘⠞', '⠘⠚', ]

# To test our cases
translateToBraille = input()
translateToEnglish = None


def main():
    Output = ' '
    if len(translateToBraille) > 0:
        for n in translateToBraille.lower():
            if n in alphabet:
                Output += alphaBraille[alphabet.index(n)]
            elif n in nums:
                Output += numBraille[nums.index(n)]
            elif n in puntuation:
                Output += puntuationBraille[puntuation.index(n)]
            elif n in character:
                Output += characterBraille[character.index(n)]
        print(Output)
        return

    if translateToEnglish:
        for n in translateToEnglish:
            if n in alphaBraille:
                Output += alphabet[alphaBraille.index(n)]
            elif n in numBraille:
                Output += nums[numBraille.index(n)]
            elif n in puntuationBraille:
                Output += puntuation[puntuationBraille.index(n)]
            elif n in characterBraille:
                Output += character[characterBraille.index(n)]

        print(Output)
        return


## calling main method
main()
