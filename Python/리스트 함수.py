# append(a) a를 삽입한다.
booksan = ["강백호",  "송태섭", "채치수", "서태웅"]
booksan.append("정대만")
print(booksan)

# sort()
nums = [1, 4, 5, 3 , 2]
nums.sort();
print(nums);

# reverse()
nums2 = [5, 4, 3, 2, 1]
nums2.reverse()
print(nums2)

# index(a), a가 있는 인덱스를 반환
print(booksan.index("강백호")) # 0

# insert(a, b) a번째 index에 b를 삽입
nums.insert(0, 0)
print(nums)

# pop(), stack의 pop
# nums.pop()

# count(a) a가 몇개있냐
nums3 = [1, 1, 1, 2, 3]
print(nums3.count(1))

# b.extend(a) b 리스트에 a라는 리스트를 붙인다