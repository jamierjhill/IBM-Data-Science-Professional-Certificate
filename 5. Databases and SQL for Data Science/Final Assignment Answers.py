#Need to add screenshots

#Q1. Find the total number of crimes recorded in the Crime table Take a screenshot showing the SQL query and its results.
%sql select count (*) as total_no_of_crimes from crimes
533

#Q2. Retrieve first 10 rows from the CRIME table
%sql select * from Crimes limit 10

#Q3. How many crimes involve an arrest?
%sql select count(*) from crimes where ARREST = True

#Q4. Which unique types of crimes have been recorded at a GAS STATION?
%sql SELECT distinct(primary_type) FROM crimes WHERE location_description = 'GAS STATION'

#Q5. In the CENUS_DATA table list all community areas whose names start with the letter ‘B'
%sql select community_area_name from socioeconomic where community_area_name like 'B%'

#Q6. Problem 6: List the schools in Community Areas 10 to 15 that are healthy school certified?

#Q7. What is the average school Safety Score?

#Q8. List the top 5 Community Areas by average College Enrollments (number of students)

#PQ9. Use a sub-query to determine which Community Area has the least value for Safety Score?

#Q10. Find the Per Capita Income of the Community Area which has a school Safety Score of 1.
