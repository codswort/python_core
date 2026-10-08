
def create_time_checker(max_time):

    def is_limited_time(real_time):
        if real_time > max_time:
            return "Лимит превышен"
        return "Лимит не превышен"

    return is_limited_time


outer_1 = create_time_checker(5)
outer_2 = create_time_checker(10)

print(outer_1(5.0))
print(outer_2(10.1))
