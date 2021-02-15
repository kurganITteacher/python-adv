# import random

def validate_str(func):
    def inner(str_to_check):
        # print('checking str...')
        if not str_to_check:
            print(f'wrong str to parse: "{str_to_check}"')  # logging
            return
        return func(str_to_check)  # parse_str(src_str)

    return inner


# def user_start_lesson(func):
#     pass  # send to Big Data (ClickHouse)
pass


# @user_start_lesson
@validate_str
def parse_str(src_str):
    # if not src_str:
    #     print('wrong str to parse!')  # logging
    #     return
    return src_str.strip().split()


sample_1 = 'идет февраль месяц, скоро весна'
sample_1_p = parse_str(sample_1)
print(sample_1_p)

sample_2 = ''
sample_2_p = parse_str(sample_2)
print(sample_2_p)

sample_3 = None
sample_3_p = parse_str(sample_3)
print(sample_3_p)

# a = 0
# b = None
# print(random.randint(a, b))
pass
# if not user.is_superuser:
#     return HttpResponeRedirect('/')
pass
