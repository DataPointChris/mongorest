employee
----------
GET     /api/employees           - get list of employees for analytics
GET     /api/employees/{id}      - get employee by id
POST    /api/employees/          - create new employee by id
PUT     /api/employees/{id}      - update employee with id
DELETE  /api/employees/{id}      - delete employee by id

role
----------
GET     /api/roles       - get list of roles
GET     /api/roles/{id}  - get role by id
POST    /api/roles/  - create new role
PUT     /api/roles/{id}  - edit role by id
DELETE  /api/roles/{id}  - delete role by id

department
----------
GET     /api/departments                 - get list of departments
GET     /api/departments/{id}            - get department by id
POST    /api/departments/                - create new department
PUT     /api/departments{id}             - update department by id
DELETE  /api/departments{id}             - delete department by id
GET     /api/departments/{id}/roles       - get all roles in department
GET     /api/departments/{id}/employees   - get  all employees in department