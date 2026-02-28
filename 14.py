s = 1024**789 + 256**678 - 64**567
count = 0
while s > 0:
  if s % 5 == 4:
    count += 1
  s = s // 5
print(count)
