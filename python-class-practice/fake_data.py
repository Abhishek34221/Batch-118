from faker import Faker
fake=Faker('hi_IN')
print(fake.name())
print(fake.email())
print(fake.emoji())
# fake(fake.address())
print(fake.address())
print(fake.phone_number())
print(fake.text())
