num = 55
start_num = 1
end_num = 100
count = 0

while True:
    count += 1
    avg_num = (start_num + end_num) // 2
    if num == avg_num:
        break
    elif avg_num > num:
        end_num = avg_num
    else:
        start_num = avg_num

print(count)