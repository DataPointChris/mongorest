from faker import Faker
import random
import datetime

fake = Faker()


def create_fake_employees(num_employees):

    departments = {1: 'engineering', 2: 'hr', 3: 'accounting', 4: 'development'}
    roles = {1: 'junior', 2: 'dev', 3: 'senior', 4: 'lead', 5: 'technician', 6: 'custodian', 7: 'CTO', 8: 'CEO'}
    status = ['current', 'sabbatical', 'terminated', 'furlough']
    fake_list = []

    for i in range(num_employees):
        dept_no = random.randint(1, len(departments))
        department = departments[dept_no]
        salary = random.randint(100_000, 125_000)
        age = random.randint(23, 70)
        hire_date = (
            datetime.date(2020, 1, 1) + datetime.timedelta(days=random.randint(1, 500))
        ).strftime("%Y-%m-%d")
        role_id = random.randint(1, len(roles))
        role = roles[role_id]
        previous_roles = list(
            set(random.choice(list(roles.values())) for r in range(random.randint(0, 3)))
        )
        status = random.choice(status)

        fake_employee = {
            "id": i,
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "personal_info": {
                "address": fake.street_address(),
                "city": fake.city(),
                "state": fake.state(),
                "country": fake.country(),
                "phone": {"work": fake.phone_number(), "cell": fake.phone_number()},
            },
            "role_id": role_id,
            "role": role,
            "previous_roles": previous_roles,
            "department_id": dept_no,
            "department": department,
            "salary": salary,
            "hiredate": hire_date,
            "age": age,
            "status": status,
        }

        fake_list.append(fake_employee)

    return fake_list
