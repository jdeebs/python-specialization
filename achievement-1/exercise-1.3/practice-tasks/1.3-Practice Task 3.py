num = 0
start = 0
end = 51 # end - 1

print("For loop:")
for num in range(start, end, 10):
    if num >= 50:
        print("And we're done!")
        break
    num += 10
    print(num)
    
num = 0
print("\nWhile loop:")
while num <= 50:
    num += 10
    print(num)
    if num >= 50:
        print("And we're done!")
        break