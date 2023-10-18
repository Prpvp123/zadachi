# 1
# def find_majority_element(nums):
#     for num in nums:
#         if nums.count(num) > len(nums) / 2:
#             return num
#     return 0
#
#
# nums = [1, 4, 4, 4, 9, 9, 9, 9]
# result = find_majority_element(nums)
# print(result)
# Если элемент встр меньше чем n / 2  то выводет 0
# 2
# binary_Str = ('100110101101')
# decimal_num = 0
# for digit in binary_Str:
#    decimal_num = decimal_num * 2 + int(digit)
#   print(decimal_num)
# выводит из двоичной в дисятичную сис
# 3
# def string_to_int(s):
#     s = s.strip()
#     sign = 1
#
#     if s and s[0] == '-':
#         sign = -1
#         s = s[1:]
#
#     result = 0
#     for char in s:
#         if '0' <= char <= '9':
#             result = result * 10 + (ord(char) - ord('0'))
#         else:
#             break
#
#     return result * sign
#
#
# print(string_to_int('69'))
# print(string_to_int('-69'))
# print(string_to_int('6969 words'))
# фун преаб строку в 32 битное целое число со знаком
# 4
# def transform_and_remove_duplicates(nums):
#     unique_nums = list(set(nums))
#
#     if len(nums) % 2 != 0:
#         unique_nums.append(nums[-1])
#
#     for i in range(0, len(unique_nums) - 1, 2):
#         unique_nums[i], unique_nums[i + 1] = unique_nums[i + 1], unique_nums[i]
#
#     return unique_nums
#
#
# nums = [2, 3, 1, 6, 8, 9, 66, 66]
# result = transform_and_remove_duplicates(nums)
# print(result)
# удаляет все дубликаты из массива и попарно меняет местами его элементы, если кол-в эл не чёт - последний эл не трогать!!!!
# 5
#n, m, q = map(int, input().split())
#watched_episodes = set()

#for _ in range(q):
    #season, episode = map(int, input().split())
   # watched_episodes.add((season, episode))

#missing_episodes = []

#for season in range(1, n + 1):
    #for episode in range(1, m + 1):
        #if (season, episode) not in watched_episodes:
            #missing_episodes.append((season, episode))

#print(len(missing_episodes))
#for episode in missing_episodes:
    #print(episode[1], episode[0])
# составляет список всех недостующих серий
