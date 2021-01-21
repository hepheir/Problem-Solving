import sys
i = sys.stdin.readline

database = []

N = int(i())
for n in range(N):
    person_str = i().rstrip()
    age = int(person_str.split()[0])
    database.append((age, person_str))

database.sort(key=lambda x:x[0])

for age, person_str in database:
    print(person_str)