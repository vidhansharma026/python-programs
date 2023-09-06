# Write a query to retrieve the list of employees working in the same department.

# Select DISTINCT E.EmpID, E.EmpFname, E.Department 
# FROM EmployeeInfo E, Employee E1 
# WHERE E.Department = E1.Department AND E.EmpID != E1.EmpID;

# SELECT * FROM Emp WHERE deptno = 10; 

# SELECT employee_id, name
# FROM employees
# WHERE department = 'DepartmentName';