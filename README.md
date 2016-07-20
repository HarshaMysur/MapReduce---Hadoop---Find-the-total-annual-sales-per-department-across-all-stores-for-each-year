# MapReduce---Hadoop---To-find-the-total-annual-sales-per-department-across-all-stores-for-each-year
Find the total annual sales per department across all stores for each year in this dataset

Problem to solve: In this question, you will use Python to write a mapper and a reducer that will execute in Hadoop streaming. 
The program sums the sales of each department in each year, using the sales dataset. 
In the dataset, each line is a tuple <store, department, date, weekly_sales>, where weekly_sales is the sales of that department at that particular store and for the week represented by the date.
Example: <1, 1, 2010-02-05, 24924.5>
Store ID is 1, Department ID is 1, Week is ‘2010-02-05’ and the total sales of ‘2010-02-05’ week at store 1 and department 1 is 24924.5

-- Only return those department-year pairs with total sales > 25000000.
-- You can ignore the store column as you need the total sales for each department in each year across all stores.

The good way of solving this problem is to make the mapper produce key-value pairs where the keys are composite and have two fields <department, year>. 
The reducer then also uses <department, year> as the key to aggregate the sales of each department for each year.
