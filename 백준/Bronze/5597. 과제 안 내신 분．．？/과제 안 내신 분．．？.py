stu = set(range(1,31))
submit = set()

for _ in range(28):
  n = int(input())
  submit.add(n)

unsubmit = sorted(stu - submit)

for stu in unsubmit:
  print(stu)
