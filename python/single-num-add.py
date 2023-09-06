# l1 = [2,4,3]
# l2 = [5,6,4]

# for i in range(len(l1)):
#     s = l1[i] + l2[i]
#     if len(str(s)) > 1:
#         b = s%10
#         c = s//10
#         print(b, c)
#         s = b
#     print(s)


l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]

# Step 1: Pad the shorter list with zeros
while len(l1) < len(l2):
    l1.append(0)
while len(l2) < len(l1):
    l2.append(0)

print(l1)
print(l2)

# Step 2: Initialize the result list and carry
result = []
carry = 0

# Step 3: Perform the addition
for i in range(len(l1)):
    sum_digits = l1[i] + l2[i] + carry
    carry = sum_digits // 10
    result.append(sum_digits % 10)

# Step 4: Add any remaining carry to the result
if carry:
    result.append(carry)

# Step 5: Reverse the result list to get the correct order
# result = result[::-1]

print(result)  # Output: [8, 9, 9, 9, 0, 0, 0, 1]


