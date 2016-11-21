i = input()
cost = i.split()
cost = list(map(int, cost))
cost2 = sorted(cost)
i = input()
available = i.split()
available = list(map(int, available))
cash = int(input())
available2, a, total = [], 0, 0
for i in range(0,3):
	for l in range(0,3):
		if cost2[i] == cost[l]:
			available2.append(available[l])
			break
for i in range(0, available2[0]):
	total += cost2[0]
	if total < cash:
		a += 1
	else:
		total -= cost2[0]
		break
if total < cash:
	for i in range(0, available2[1]):
		total += cost2[1]
		if total < cash:
			a += 1
		else:
			total -= cost2[1]
			break
if total < cash:
	for i in range(0, available2[2]):
		total += cost2[2]
		if total < cash:
			a += 1
		else:
			total -= cost2[2]
			break
print(a)
