employee
----------
GET     /employee       - get list of employees
GET     /employee/{id}  - get employee by id
POST    /employee/{id}  - create new employee by id

role
----------
GET     /role       - get list of roles
GET     /role/{id}  - get role by id
POST    /role/{id}  - create new role by id

department
----------
GET     /department                 - get list of departments
GET     /department/{id}            - get department by id
POST    /department/{id}            - create new department by id
GET     /department/{id}/role       - get all roles in department
GET     /department/{id}/employee   - get list of all employees in department