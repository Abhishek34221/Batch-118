# import random
# emp_name = ['aman','kamal','shivam','anshu']
# res=random.choice(emp_name)
# print(res)

import random
# emp_name = ['aman','kamal','shivam','anshu']
# weight = [2,3,1,0]
# res=random.choices(emp_name,weights=weight, k=1)
# print(res)

# res = random.random()*10
# print(int(res))


# rand_int=random.randint(1,10)
# rand_range=random.randrange(1,10)

# print(rand_int)
# print(rand_range)

# user max attempt = 6
# each attempt random number generate
# randon number generate sum
# fix_value = 150



# fixed_value = 150
# total = 0
# for i in range(6):
#     num = random.randint(24,27)
#     total += num
# print("Sum =", total)
# if total == 150:
#     print("Matched")
# elif 135 <= total <= 175:
#     print("Nearest")
# else:
#     print("Too far")


# sample()

# emp_name = ['aman','kamal','shivam','anshu']
# res=random.sample(emp_name,k=2)
# print(res)

# shuffle()

# emp_name = ['aman','kamal','shivam','anshu']
# random.shuffle(emp_name)
# print(emp_name)

# coupon code
#CXYZ76989

import string


for i in range(1,11):
    letters = ''.join(random.choices(string.ascii_uppercase, k=4))
    numbers = ''.join(random.choices(string.digits, k=6))
    coupon_code = letters + numbers
    print(coupon_code)

