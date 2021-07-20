# Input
name, ssn = input().split(' ') # 이름(name), 주민번호(Social Security Number)

# Process
TABLE = [
    # 년도    출생지         성별
    ('18', 'korea',     'female'),
    ('19', 'korea',     'male'  ),
    ('19', 'korea',     'female'),
    ('20', 'korea',     'male'  ),
    ('20', 'korea',     'female'),
    ('19', 'foreign',   'male'  ),
    ('19', 'foreign',   'female'),
    ('20', 'foreign',   'male'  ),
    ('20', 'foreign',   'female'),
    ('18', 'korea',     'male'  )
]

g = ssn[7] # 주민번호 G 숫자

century, born, gender = TABLE[int(g)]

yyyymmdd = century + ssn[:6] # 생년월일 8자리

# Output
print('{0:15s}{1:15s}{2:15s}{3:15s}'.format(name, yyyymmdd, born, gender))
