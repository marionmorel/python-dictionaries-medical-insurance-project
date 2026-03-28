# Python Dictionaries: Medical Insurance Project

## Data Scientist: Analytics - Codecademy

You have been asked to create a program that organizes and updates medical records efficiently.

In this project, you will use your new knowledge of Python dictionaries to create a database of medical records for patients.

### Tasks

#### Storing patient names and insurance costs

1. We would like to keep a record of medical patients and their insurance costs.

First, create an empty dictionary called <code>medical_costs</code>.

2. Let’s populate our <code>medical_costs</code> dictionary by adding the following key-value pairs:

* Add <code>"Marina"</code> to <code>medical_costs</code> as a key with a value of <code>6607.0</code>.
* Add <code>"Vinay"</code> to <code>medical_costs</code> as a key with a value of <code>3225.0</code>.

3. Using one line of code, add the following three patients to the <code>medical_costs</code> dictionary:

* <code>"Connie"</code>, with an insurance cost of <code>8886.0</code>
* <code>"Isaac"</code>, with an insurance cost of <code>16444.0</code>
* <code>"Valentina"</code>, with an insurance cost of <code>6420.0M</code>

4. Print <code>medical_costs</code>. Make sure the dictionary is what you expected.

5. You notice that <code>Vinay</code>’s insurance cost was incorrectly inputted. Update the value associated with <code>Vinay</code> to <code>3325.0</code>.
Print the updated dictionary.

6. Let’s calculate the average medical cost of each patient. Create a variable called <code>total_cost</code> and set it equal to 0.

Next, iterate through the values in <codE>medical_costs</code> and add each value to the <code>total_cost</code> variable.

7. After the loop, create a variable called <code>average_cost</code> that stores the <code>total_cost</code> divided by the length of the <code>medical_costs</code> dictionary.

Print <code>average_cost</code> with the following message:

```
Average Insurance Cost: {average_cost}
```

#### List Comprehension to Dictionary

8. You have been asked to create a second dictionary that maps patient names to their ages.

First, create two lists called <code>names</code> and <code>ages</code> with the following data:

|names|ages|
|------|------|
|Marina|27|
|Vinay|24|
|Connie|43|
|Isaac|35|
|Valentina|52|

9. Next, create a variable called <code>zipped_ages</code> that is a zipped list of pairs between the <code>names</code> list and the <code>ages</code> list.

10. Create a dictionary called <code>names_to_ages</code> by using a list comprehension that iterates through <code>zipped_ages</code> and turns each pair into a key : value item.

Print <code>names_to_ages</code> to see the result.

11. Use <code>.get()</code> to get the value of Marina’s age and store it in a variable called <code>marina_age</code>. Use <code>None</code> as a default value if the key doesn’t exist.

Print <code>marina_age</code> with the following message:

```
Marina's age is {marina_age}
```

#### Using a Dictionary to create a medical database

12. Let’s create a third dictionary to represent a database of medical records that contains information such as a patient’s name, age, sex, gender, BMI, number of children, smoker status, and insurance cost.

First, create an empty dictionary called <code>medical_records</code>.

13. Next, add <code>"Marina"</code> to <code>medical_records</code> as a key with the value being a dictionary of medical data:

```
{"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
```

14. Do the same for the following individuals:

|Name|Age|Sex|BMI|Children|Smoker|Insurance Cost|
|----|---|---|---|--------|------|--------------|
|Vinay|24|Male|26.9|0|Non-smoker|3225.0|
|Connie|43|Female|25.3|3|Non-smoker|8886.0|
|Isaac|35|Male|20.6|4|Smoker|16444.0|
|Valentina|52|Female|18.7|1|Non-smoker|6420.0|

15. Print <code>medical_records</code> to see the result.

16. The <code>medical_records</code> dictionary acts like a database of medical records. Let’s access a specific piece of data in <code>medical_records</code>.

Print out <code>Connie</code>’s insurance cost with the following message:

```
Connie's insurance cost is X dollars.
```

17. Vinay has moved to a new country and we no longer want to include him in our medical records.

Remove <code>Vinay</code> from <code>medical_records</code>.

18. Let’s take a closer look at each patient’s medical record.

Use a <code>for</code> loop to iterate through the items of <code>medical_records</code>. For each key-value pair, print out a string that looks like the following:

```
{Name} is a {Age} year old {Sex} {Smoker} with a BMI of {BMI} and insurance cost of {Insurance_cost}
```

#### Extra

19. Congratulations! In this project, you used Python dictionaries to store and update medical data for individuals.

If you’d like extra practice with dictionaries, here are some suggestions to go further with this project:

* Create a function called <code>update_medical_records()</code> that takes in the name of an individual as well as their medical data, and then updates the <code>medical_records</code> dictionary accordingly.
* Create a new dictionary of your choice – feel free to get creative!

Happy coding!