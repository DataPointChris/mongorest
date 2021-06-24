employee
----------
GET     /employees           - get list of employees for analytics
GET     /employees/{id}      - get employee by id
POST    /employees/          - create new employee by id
PUT     /employees/{id}      - update employee with id
DELETE  /employees/{id}      - delete employee by id

role
----------
GET     /roles       - get list of roles
GET     /roles/{id}  - get role by id
POST    /roles/  - create new role
PUT     /roles/{id}  - edit role by id
DELETE  /roles/{id}  - delete role by id

department
----------
GET     /departments                 - get list of departments
GET     /departments/{id}            - get department by id
POST    /departments/                - create new department
PUT     /departments{id}             - update department by id
DELETE  /departments{id}             - delete department by id
GET     /departments/{id}/roles       - get all roles in department
GET     /departments/{id}/employees   - get list of all employees in department


Bamboo Color:
#69b426