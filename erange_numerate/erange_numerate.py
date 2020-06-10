import random



class erange:

	#Has a constructor which can take 1-3 paramters
	def __init__(self, pos1, pos2 = None, pos3 = None):

		self.start = 0
		self.step = 1

		#Assigns the correct paramters to the correct variables depending on how many parameters are passed
		if pos2 == None and pos3 == None:
			self.stop = pos1
		elif pos3 == None:
			self.start = pos1
			self.stop = pos2
		else:
			self.start = pos1
			self.stop = pos2
			self.step = pos3

		self.initialStart = self.start


	#Used for when you you try to: print(erange(<values>))
	def __str__(self):
		return "erange({}, {})".format(self.initialStart,self.stop) if self.step == 1 else "erange({}, {}, {})".format(self.initialStart,self.stop,self.step)

	#overrides iterator
	def __iter__(self):
		return self

	#Cycles through the numbers at the step value until all numbers are covered
	def __next__(self):
		ret = self.start
		self.start += self.step
		pos_dir = True if self.step > 0 else False
		#Two conditions for exiting (increasing && start surpasses or equals stop) or (decreasing && start falls below of equals stop)
		if(pos_dir == True and ret >= self.stop) or (pos_dir == False and ret <= self.stop):
			raise StopIteration
		else:
			return ret


class numerate:

	pos = 0

	def __init__(self,lst,start = 0):
		self.start = start
		self.lst = lst
		if not isinstance(lst,list):
			self.lst = list(lst)

	def __iter__(self):
		return self

	def __next__(self):
		if self.pos >= len(self.lst):
			raise StopIteration
		else:
			self.pos += 1
			return (self.pos - 1 + self.start,self.lst[self.pos-1])


### -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### -------------------------------------------------------------------------------------------Delete Import!!!------------------------------------------------------------------------
### -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


	'''
x = numerate("hello",5)

for i in x:
	print(i)

print(x)'''



'''
x = erange(1,20)
print(x)

for i in erange(6,-1,-2):
	print(i)
'''

#x = erange(41)
#print(x)



'''

for c,value in numerate(erange(5)):
    print(c,value)'''

'''print(range(5,3,4) == erange(5,3,4)[1:len(erange(5,3,4))])
print(range(5,3,4))
print(str(erange(5,3,4))[1:len(str(erange(5,3,4)))])
print(str(range(5,3,4)) == str(erange(5,3,4))[1:len(str(erange(5,3,4)))])'''



works_lst = []
for i in range(10000):
	r1 = random.randint(1,3)

	rStart = 0
	rStep = 1


	#passing 1 parameter
	if(r1 == 1):
		rStop = random.randint(-5,50)
		reg = (range(rStop))
		tes = (erange(rStop))

	#passing 2 parameters
	elif(r1 == 2):
		rStart = random.randint(-50,50)
		rStop = random.randint(1,100)

		reg = (range(rStart,rStop))
		tes = (erange(rStart,rStop))

	#passing 3 parameters
	else:
		stepRange = [-3,-2,-1,1,2,3]
		rStart = random.randint(-50,50)
		rStop = random.randint(-50,50)
		rStep = random.choice(stepRange)

		reg = (range(rStart,rStop,rStep))
		tes = (erange(rStart,rStop,rStep))


	regTest = []
	for q in reg:
		regTest.append(q)
	tesTest = []
	for q in tes:
		tesTest.append(q)

	

	reg = str(reg)
	tes = str(tes)

	reg = reg.replace("\n"," , ")
	tes = tes.replace("\n"," , ")

	#print("Data:  rStart: {}\trStop: {}\trStep: {}".format(rStart,rStop,rStep))
	print("Testing:  {}  &  {}".format(reg,tes))

	print(str(regTest))
	print(str(tesTest))

	tes = tes[1:len(tes)]

	works = reg==tes and str(regTest) == str(tesTest)
	works_lst.append(works)

	print("---------- {} ----------\n".format(works))
	#print("\n")








numerate_lst = []
for q in range(10000):

	#print(q)
	wrd = ""

	length = random.randint(1,15)

	for i in range(length):
		rchar = random.randint(48,116)
		if(rchar >= 91 and rchar <= 96):
			rchar += 6
		wrd += chr(rchar)

	r1 = random.randint(1,2)

	if(r1 == 1):
		wrd = list(wrd)


	r2 = random.randint(1,4)
	r3 = None

	if(r2 == 1):
		r3 = random.randint(-50,50)
		reg = enumerate(wrd,r3)
		tes = numerate(wrd,r3)
	else:
		reg = enumerate(wrd)
		tes = numerate(wrd)

	regTest = []
	tesTest = []

	for i in reg:
		regTest.append(i)
	for i in tes:
		tesTest.append(i)

	


	if(r3):
		print("Testing:  enumerate({},{})  &  numerate({},{})".format(str(wrd),r3,str(wrd),r3))
	else:
		print("Testing:  enumerate({})  &  numerate({})".format(str(wrd),str(wrd)))

	works = str(regTest) == str(tesTest)
	numerate_lst.append(works)

	print(regTest)
	print(tesTest)

	print("---------- {} ----------\n".format(works))
	

print(works_lst)
print(numerate_lst)





print("\n\n--{} condition{} for erange() checked".format(len(works_lst),"s" if len(works_lst) > 1 else ""))
if(False in works_lst):
	print("**Failed Conditions")
else:
	print("--All Conditions passed!")


print("\n\n--{} condition{} for numerate() checked".format(len(numerate_lst),"s" if len(numerate_lst) > 1 else ""))
if(False in numerate_lst):
	print("**Failed Conditions")
else:
	print("--All Conditions passed!\n")