from termcolor import colored


def KUniqueCharacters(strParam):
	# code goes here
	# print(f'strParam is of {type(strParam)}')
	# TODO: extract the inner for-loop
	
	k = int(strParam[0])
	
	print(f'k = {k}')
	
	ans = []
	curr = ''
	count = 0
	
	substr = strParam[1:]
	for i in range(substr.__len__()):
		if substr[i] in curr:
			curr += substr[i]
		else:
			if count < k:
				curr += substr[i]
				count += 1
			else:
				ans.append(curr)
				count = 0
				curr = ''
	# print(f'curr = {curr}')
	print(f'ans = {ans}')
	
	# for i in range(substr.__len__()):
	# 	temp = substr[i:]
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
	
	return ans


if __name__ == "__main__":
	# keep this function call here
	s = input()
	print(colored(s, color="green"))
	print(KUniqueCharacters(s))
