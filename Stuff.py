nums = [1,2,3]
end = []
x = 0
for item in nums:
    x += item
    end.append(x)
print(end)

stist = ['apple', 'banana', 'car', 'dragon', 'ending', 'finisher', 'great','high' ]
print(sorted(stist, key = len))
