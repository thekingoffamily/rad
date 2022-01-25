import asyncio, time, random, hashlib, pytest

# name, vacancy, salary = sys.argv[1], sys.argv[2], sys.argv[3]

data = {"name" : "Vitaliy", "vacancy" : "Python Developer Trainee", "salary" : 110000}

def testData():
	assert type(data["name"]) == str
	assert type(data["vacancy"]) == str
	assert type(data["salary"]) == int

async def getRandomTime():
	return time.sleep(random.randint(0, 5))

async def aboutMe():
	await getRandomTime()
	print("Hello, i am {0}!".format(data["name"]))
	await getRandomTime()
	print("Want job on vacancy -> {0}.".format(data["vacancy"]))
	await getRandomTime()
	print("Salary after 1 year work -> {0} rub.".format(data["salary"]))

def sha256(*args):
	allData = []
	for var in args:
		if var != str:
			var = str(var)
			allData.append(hashlib.sha256(var.encode('utf-8')).hexdigest())
	print(allData)
if __name__ == '__main__':
	asyncio.run(aboutMe())
	print(r'Hash all data in sha256:\n')
	sha256(data["name"], data["vacancy"], data["salary"])
