# Question 1
This function uses pandas library to read a CSV file 'NISPUF17.csv' and compute the proportion of individuals in the dataset who have each level of education.

The proportion is calculated using the value_counts method with normalize=True to get the proportion of each education level in the dataset.

The results are stored in a dictionary EDUC1_dict where each key represents a level of education, and the corresponding value is the proportion of individuals in the dataset who have that level of education.

The function returns this dictionary EDUC1_dict.

# Question 2
This function uses pandas library to read a CSV file 'NISPUF17.csv' and compute the average number of influenza vaccines (P_NUMFLU) for children whose mother reported that they received breastfeeding (CBF_01 equals 1) and for children whose mother reported that they did not receive breastfeeding (CBF_01 equals 2).

The function creates two dataframes, df1 for children who received breastfeeding and df2 for children who did not receive breastfeeding, using boolean indexing.

The function then calculates the mean of the P_NUMFLU column for each of the two dataframes and returns a tuple with the results.

# Question 3
This function uses pandas library to read a CSV file 'NISPUF17.csv' and compute the ratio of the number of children who had chickenpox (HAD_CPOX equals 1) to the number of children who did not have chickenpox (HAD_CPOX equals 2), separately for males and females who received at least one dose of the chickenpox vaccine (P_NUMVRC is greater than or equal to 1).

The function first selects the columns of interest (SEX, HAD_CPOX, and P_NUMVRC) and drops the rows with missing values using the dropna() method.

The function then selects the rows where P_NUMVRC is greater than or equal to 1 using boolean indexing.

The function creates two dataframes, male_df for males and female_df for females, using boolean indexing.

The function then selects the rows where HAD_CPOX equals 1 and P_NUMVRC is greater than or equal to 1 (female_chickenpox) and the rows where HAD_CPOX equals 2 and P_NUMVRC is greater than or equal to 1 (female_non_chickenpox) for the female_df.

The function calculates the ratio of the number of children who had chickenpox to the number of children who did not have chickenpox, separately for males and females, and stores the results in the male_ratio and female_ratio variables.

The function returns a dictionary with the results, where the keys are "male" and "female" and the corresponding values are the ratios.

It looks like the function is complete and should work as intended.

# Question 4
This function uses the scipy.stats library to compute the Pearson correlation coefficient between the number of chickenpox (HAD_CPOX) and the number of chickenpox vaccines (P_NUMVRC) received by children who either had chickenpox (HAD_CPOX equals 1) or did not have chickenpox (HAD_CPOX equals 2).

The function first reads the CSV file 'NISPUF17.csv' into a pandas DataFrame and selects only the rows where HAD_CPOX is less than or equal to 2 using boolean indexing.

The function then selects only the rows where P_NUMVRC and HAD_CPOX are not NaN values using the isna() method and the negation operator ~.

The function uses the pearsonr() function from the scipy.stats library to compute the Pearson correlation coefficient and the corresponding p-value for the two variables.

The function returns the correlation coefficient.

It looks like the function is complete and should work as intended.





