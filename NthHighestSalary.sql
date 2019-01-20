CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select if (count(distinct(Salary)) < N, null, min(Salary)) from
      (select distinct Salary from Employee order by Salary desc limit N) topN
  );
END
