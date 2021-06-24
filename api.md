employee
----------
GET     /api/employees/           - get list of employees for analytics
POST    /api/employees/          - create new employee by id
GET     /api/employees/{id}      - get employee by id
PUT     /api/employees/{id}      - update employee with id
DELETE  /api/employees/{id}      - delete employee by id

role
----------
GET     /api/roles/       - get list of roles
PUT     /api/roles/{name}  - edit role by name
GET     /api/roles/{name}/employees/  - get employees in this role
GET     /api/roles/{name}/departments/ - get departments with this role 

department
----------
GET     /api/departments/                 - get list of departments
PUT     /api/departments/{name}             - edit department by name
GET     /api/departments/{name}/employees   - get  all employees in department
GET     /api/departments/{name}/roles       - get all roles in department