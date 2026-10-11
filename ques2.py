s = input()
seen = set()
left = 0
max_length = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    length = right - left + 1
    if length > max_length:
        max_length = length

print("length of longest substring :", max_length)