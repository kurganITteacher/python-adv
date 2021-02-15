# @str_len
def parse_str(src_str):
    return src_str.strip().split()


sample_1 = 'идет февраль месяц, скоро весна'
sample_1_p = parse_str(sample_1)
# print(f'str len: {len(sample_1)}')
print(sample_1_p)

sample_2 = 'идет февраль'
sample_2_p = parse_str(sample_2)
# print(f'str len: {len(sample_2)}')
print(sample_2_p)
