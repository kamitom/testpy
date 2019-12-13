

from faker import Faker

testf = Faker()

urname = testf.name()

# print(testf.name())

print(f"hello, {urname}")

x = -2.9


print(abs(x))

has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
  print("pass!!")

# unpacking
nba_teams = ("LA", "MI", "LO")

a, b, c = nba_teams

# print(c)

for nba in nba_teams:
  print(nba)

nba_all = {
  "LA": "LOS",
  "NY": "NICKS",
  "NY": "BROOKLYN"
}

print(nba_all["LA"])
print(nba_all.get("tw"))

nba_all["US"] = "WHITE HOUSE"

print(nba_all["US"])
