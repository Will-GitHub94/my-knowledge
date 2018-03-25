#### [Missing data](data_processing/missing_data.py)

How to handle situations where there is missing data?
  - Remove the records where there is missing data but could be risky if those records contain crucial information
  - (Most common) Take the **mean** of the columns. Replace the missing data with the mean value of all populated data in that column. For example, looking at the data set linked above, the 'Age' for 'Spain' will be populated with the mean value of all the other ages in that column