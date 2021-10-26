from termcolor import colored


def KUniqueCharacters(strParam):
	# code goes here
	k = int(strParam[0])
	
	# print(f'k = {k}')
	
	ans = []
	curr = ''
	count = 0
	
	s1 = strParam[1:]
	for i in range(s1.__len__()):
		s2 = s1[i:]
		for j in range(s2.__len__()):
			if s2[j] in curr:
				curr += s2[j]
			else:
				if count < k:
					curr += s2[j]
					count += 1
				else:
					ans.append(curr)
					count = 0
					curr = ''
					break
	
	# for i in range(s1.__len__()):
	# 	if s1[i] in curr:
	# 		curr += s1[i]
	# 	else:
	# 		if count < k:
	# 			curr += s1[i]
	# 			count += 1
	# 		else:
	# 			ans.append(curr)
	# 			count = 0
	# 			curr = ''
	
	# print(f'curr = {curr}')
	# print(f'ans = {ans}')
	
	# for i in range(s1.__len__()):
	# 	temp = s1[i:]
	# 	count = 0
	# 	curr = ''
	# 	for j in range(temp.__len__()):
	# 		if temp[j] in curr:
	# 			curr += temp[j]
	# 		elif (temp[j] not in curr) and count < k:
	# 			curr += temp[j]
	# 			count += 1
	#
	# 	# print(f'curr = {curr}')
	# 	if curr.__len__() > ans.__len__():
	# 		ans = curr
	
	return sorted(ans, key=len, reverse=True)[0]


if __name__ == "__main__":
	# keep this function call here
	s = input()
	print(colored(s, color="green"))
	print(KUniqueCharacters(s))
