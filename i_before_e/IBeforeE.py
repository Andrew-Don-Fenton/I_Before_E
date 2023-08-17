import re
WordsIBeforeE = [word for word in [line.strip() for line in open('C:\\Users\\afenton\\Desktop\\EnglishWords.txt')] if re.match('.*ie.*', word)]
WordsEBeforeI = [word for word in [line.strip() for line in open('C:\\Users\\afenton\\Desktop\\EnglishWords.txt')] if re.match('.*ei.*', word)]
#matches = [i for i in lines if re.match('.*i.*e.*', i)]
print('number of words that have i before e is ' + str(WordsIBeforeE.__len__()))
print('number of words that have e before i is '+ str(WordsEBeforeI.__len__()))
WordsThatBreakAfterCRule = [word for word in WordsIBeforeE if re.match('.*c.*ie.*', word)]
WordsThatFollowTheAfterCRule = [word for word in WordsEBeforeI if re.match('.*c.*ei.*', word)]
WordsThatHaveEBeforeIWithNoC = [word for word in WordsEBeforeI if word not in WordsThatFollowTheAfterCRule]
print('number of words that break the after c with an i before e is ' + str(WordsThatBreakAfterCRule.__len__()))
print('number of words that follow the after c rule with an e before i is ' + str(WordsThatFollowTheAfterCRule.__len__()))
print('number of words that have an e before i where there is no c before it ' + str(WordsThatHaveEBeforeIWithNoC.__len__()))
