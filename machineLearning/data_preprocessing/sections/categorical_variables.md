#### Categorical variables

In our data set, we can see that the columns *Country* and *Purchased* are **categorical** variables because they simply contain categories...<br>
The *Country* contains 3 categories:
  - France
  - Spain
  - Germany

While *Purchased* contains only 2 categories:
  - Yes
  - No

Since machine learning is based on mathematical functions, it would cause some problems to have these categorical variables in the data *(as they are not numeric...)* so they need encoding

The issue with encoding columns some time is that the model will interpret some values as better than others...

In our data set, if we encode the *Country* column, we may end up with numerically ascending data. For example:

| Text    | Encode |
|:-------:|:------:|
| France  |   0    |
| Germany |   1    |
|  Spain  |   2    |

It would be interpreted here that Spain is better than Germany and Germany is better than France... this might be relevant if we were encoding sizes (Small, Medium, Large) as this might infact be true. To get around this problem, we create more columns as there are categories<br>
*(You can probably get from the image below what the data is supposed to be)*

<img src="assets/split_country_columns.png" alt="Split categorised column" style="width: 400px"/><br>
