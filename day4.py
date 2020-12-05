import re


def parse_input(input_lines):
    passports = []
    current = {}
    for line in input_lines:
        line = line.strip()
        if not line:
            if current:
              passports.append(current)
            current = {}
        for chunk in line.split():
            k, v = chunk.split(':')
            if k in current:
                raise ValueError('BORKED: %r' % line)
            current[k] = v
    if current:
        passports.append(current)
    return passports


def is_valid(passport):
    required_keys = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    }
    if not all(k in passport for k in required_keys):
        return False
    if not 1920 <= int(passport['byr']) <= 2002:
        return False
    if not 2010 <= int(passport['iyr']) <= 2020:
        return False
    if not 2020 <= int(passport['eyr']) <= 2030:
        return False
    h = passport['hgt']
    if h.endswith('cm'):
        if not 150 <= int(h[:-2]) <= 193:
            return False
    elif h.endswith('in'):
        if not 59 <= int(h[:-2]) <= 76:
            return False
    else:
        return False
    if not re.match(r'^#[0-9a-f]{6}$', passport['hcl']):
        return False
    if passport['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        return False
    if not re.match('^[0-9]{9}$', passport['pid']):
        return False
    return True

bad_pps = parse_input('''
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
'''.splitlines())
for pp in bad_pps:
    if is_valid((pp)):
        is_valid(pp)


good_pps = parse_input('''
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
'''.splitlines())
for pp in good_pps:
    if not is_valid((pp)):
        is_valid(pp)


with open('day4_input.txt') as f:
    passports = parse_input(f.readlines())
print(len(passports))
total = 0
for p in passports:
    if is_valid(p):
        total += 1

print(total)
