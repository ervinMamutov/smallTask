textMobiDic = []
with open('moby_01_clean.txt') as infile:
    for line in infile:
        textMobiDic.append(line)
# Привести к одному регистру
textList = repr(textMobiDic)
textList = textList.lower()

print(textList)

# Удалить знаки препинания
withDot = textList.maketrans('\.,-n', '     ')
textList = textList.translate(withDot)
print(textList)

# Разбить на слова
textList = textList.split()
print(textList)

# Записать все слова по одному на строку файла
with open('moby_complite_clean.txt', 'a') as file:
    for word in textList:
        print(word)
        file.write(word + '\n')
