# player_wins = [random.randint(0, 1000) for _ in range(20)]
player_wins = [
    540, 167, 930, 874, 894, 310,
    229, 2, 298, 349, 331, 768, 160,
    902, 491, 39, 725, 7, 784, 998
]
print(player_wins)

att_example = [(930, 874, 894), (874, 894, 310), (349, 331, 768)]
# 3 times > 300

att = []
for i in range(len(player_wins) - 3 + 1):
    nums = player_wins[i:i + 3]
    if min(nums) >= 300:
        # print(nums)
        att.append(tuple(nums))
# print(att)
assert att == att_example, 'wrong result'
