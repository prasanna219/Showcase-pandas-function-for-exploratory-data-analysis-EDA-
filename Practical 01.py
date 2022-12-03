Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> data=pd.read_csv("D:/Data Science/Housing.csv")
>>> data.head()
      price  area  bedrooms  ...  parking  prefarea furnishingstatus
0  13300000  7420         4  ...        2       yes        furnished
1  12250000  8960         4  ...        3        no        furnished
2  12250000  9960         3  ...        2       yes   semi-furnished
3  12215000  7500         4  ...        3       yes        furnished
4  11410000  7420         4  ...        2        no        furnished

[5 rows x 13 columns]
>>> data.tail()
       price  area  bedrooms  ...  parking  prefarea furnishingstatus
540  1820000  3000         2  ...        2        no      unfurnished
541  1767150  2400         3  ...        0        no   semi-furnished
542  1750000  3620         2  ...        0        no      unfurnished
543  1750000  2910         3  ...        0        no        furnished
544  1750000  3850         3  ...        0        no      unfurnished

[5 rows x 13 columns]
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 545 entries, 0 to 544
Data columns (total 13 columns):
 #   Column            Non-Null Count  Dtype 
---  ------            --------------  ----- 
 0   price             545 non-null    int64 
 1   area              545 non-null    int64 
 2   bedrooms          545 non-null    int64 
 3   bathrooms         545 non-null    int64 
 4   stories           545 non-null    int64 
 5   mainroad          545 non-null    object
 6   guestroom         545 non-null    object
 7   basement          545 non-null    object
 8   hotwaterheating   545 non-null    object
 9   airconditioning   545 non-null    object
 10  parking           545 non-null    int64 
 11  prefarea          545 non-null    object
 12  furnishingstatus  545 non-null    object
dtypes: int64(6), object(7)
memory usage: 55.5+ KB
>>> #data type of each column
>>> data.dtypes
price                int64
area                 int64
bedrooms             int64
bathrooms            int64
stories              int64
mainroad            object
guestroom           object
basement            object
hotwaterheating     object
airconditioning     object
parking              int64
prefarea            object
furnishingstatus    object
dtype: object
>>> data.shape
(545, 13)
>>> data.size
7085
>>> data.describe()
              price          area  ...     stories     parking
count  5.450000e+02    545.000000  ...  545.000000  545.000000
mean   4.766729e+06   5150.541284  ...    1.805505    0.693578
std    1.870440e+06   2170.141023  ...    0.867492    0.861586
min    1.750000e+06   1650.000000  ...    1.000000    0.000000
25%    3.430000e+06   3600.000000  ...    1.000000    0.000000
50%    4.340000e+06   4600.000000  ...    2.000000    0.000000
75%    5.740000e+06   6360.000000  ...    2.000000    1.000000
max    1.330000e+07  16200.000000  ...    4.000000    3.000000

[8 rows x 6 columns]
>>> ##Transpose Operator to switch columns to rows
>>> data.describe(include='all').T
                  count unique  ...        75%         max
price             545.0    NaN  ...  5740000.0  13300000.0
area              545.0    NaN  ...     6360.0     16200.0
bedrooms          545.0    NaN  ...        3.0         6.0
bathrooms         545.0    NaN  ...        2.0         4.0
stories           545.0    NaN  ...        2.0         4.0
mainroad            545      2  ...        NaN         NaN
guestroom           545      2  ...        NaN         NaN
basement            545      2  ...        NaN         NaN
hotwaterheating     545      2  ...        NaN         NaN
airconditioning     545      2  ...        NaN         NaN
parking           545.0    NaN  ...        1.0         3.0
prefarea            545      2  ...        NaN         NaN
furnishingstatus    545      3  ...        NaN         NaN

[13 rows x 11 columns]
>>> ##Sample Method allows you to select values randomly from a series
>>> data.sample(n=8)
       price  area  bedrooms  ...  parking  prefarea furnishingstatus
296  4200000  4600         3  ...        1        no   semi-furnished
308  4165000  4046         3  ...        1        no   semi-furnished
55   7350000  6000         3  ...        1        no      unfurnished
257  4480000  8250         3  ...        0        no        furnished
263  4410000  3968         3  ...        0        no   semi-furnished
528  2275000  3970         1  ...        0        no      unfurnished
154  5530000  3650         3  ...        2        no   semi-furnished
116  6020000  6900         3  ...        0       yes      unfurnished

[8 rows x 13 columns]
>>> ##Identifying missing values Isnull
>>> data.isnull()
     price   area  bedrooms  ...  parking  prefarea  furnishingstatus
0    False  False     False  ...    False     False             False
1    False  False     False  ...    False     False             False
2    False  False     False  ...    False     False             False
3    False  False     False  ...    False     False             False
4    False  False     False  ...    False     False             False
..     ...    ...       ...  ...      ...       ...               ...
540  False  False     False  ...    False     False             False
541  False  False     False  ...    False     False             False
542  False  False     False  ...    False     False             False
543  False  False     False  ...    False     False             False
544  False  False     False  ...    False     False             False

[545 rows x 13 columns]
>>> ##Isna function returns a dataframe filled with boolean values with true indicating missing values
>>> data.isna().any()
price               False
area                False
bedrooms            False
bathrooms           False
stories             False
mainroad            False
guestroom           False
basement            False
hotwaterheating     False
airconditioning     False
parking             False
prefarea            False
furnishingstatus    False
dtype: bool
>>> ##Identifying missing values df.isnull().sum()
>>> df.isnull().sum()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    df.isnull().sum()
NameError: name 'df' is not defined
>>> data.isnull().sum()
price               0
area                0
bedrooms            0
bathrooms           0
stories             0
mainroad            0
guestroom           0
basement            0
hotwaterheating     0
airconditioning     0
parking             0
prefarea            0
furnishingstatus    0
dtype: int64
>>> ##Nunique counts the number of unique entries over columns or rows
>>> data.nunique()
price               219
area                284
bedrooms              6
bathrooms             4
stories               4
mainroad              2
guestroom             2
basement              2
hotwaterheating       2
airconditioning       2
parking               4
prefarea              2
furnishingstatus      3
dtype: int64
>>> ##index() is an inbuilt function in python,whiles searches for a given element from the start of the list and returns the lowest index where the element appear
>>> data.index
RangeIndex(start=0, stop=545, step=1)
>>> data.column
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    data.column
  File "C:\Users\prasa\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\generic.py", line 5487, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'column'
>>> data.columns
Index(['price', 'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad',
       'guestroom', 'basement', 'hotwaterheating', 'airconditioning',
       'parking', 'prefarea', 'furnishingstatus'],
      dtype='object')
>>> ##Memory_usage() returns how much memory each column uses in bytes
>>> data.memory_usage()
Index                128
price               4360
area                4360
bedrooms            4360
bathrooms           4360
stories             4360
mainroad            4360
guestroom           4360
basement            4360
hotwaterheating     4360
airconditioning     4360
parking             4360
prefarea            4360
furnishingstatus    4360
dtype: int64
>>> data.smallest(5,'median_house_value')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    data.smallest(5,'median_house_value')
  File "C:\Users\prasa\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\generic.py", line 5487, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'smallest'
>>> data.nsmallest(5,'median_house_value')
Traceback (most recent call last):
  File "C:\Users\prasa\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'median_house_value'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    data.nsmallest(5,'median_house_value')
  File "C:\Users\prasa\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\frame.py", line 6735, in nsmallest
    self, n=n, keep=keep, columns=columns
  File "C:\Users\prasa\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\algorithms.py", line 1225, in nsmallest
    return self.compute("nsmallest")
  File "C:\Users\prasa\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\algorithms.py", line 1349, in compute
    dtype = frame[column].dtype
  File "C:\Users\prasa\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\frame.py", line 3458, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\prasa\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: 'median_house_value'
>>>  data.nsmallest(5,'hotwaterheating')
 
SyntaxError: unexpected indent
>>> data.nsmallest(5,'hotwaterheating')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    data.nsmallest(5,'hotwaterheating')
  File "C:\Users\prasa\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\frame.py", line 6735, in nsmallest
    self, n=n, keep=keep, columns=columns
  File "C:\Users\prasa\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\algorithms.py", line 1225, in nsmallest
    return self.compute("nsmallest")
  File "C:\Users\prasa\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\algorithms.py", line 1352, in compute
    f"Column {repr(column)} has dtype {dtype}, "
TypeError: Column 'hotwaterheating' has dtype object, cannot use method 'nsmallest' with this dtype
>>> data.nsmallest(5,'area')
       price  area  bedrooms  ...  parking  prefarea furnishingstatus
449  3150000  1650         3  ...        0        no      unfurnished
537  1890000  1700         3  ...        0        no      unfurnished
527  2275000  1836         2  ...        0        no   semi-furnished
271  4340000  1905         5  ...        0        no   semi-furnished
413  3430000  1950         3  ...        0       yes      unfurnished

[5 rows x 13 columns]
>>> data.nlargest(5,'area')
        price   area  bedrooms  ...  parking  prefarea furnishingstatus
7    10150000  16200         5  ...        0        no      unfurnished
125   5943000  15600         3  ...        2        no   semi-furnished
10    9800000  13200         3  ...        2       yes        furnished
66    6930000  13200         2  ...        1        no        furnished
403   3500000  12944         3  ...        0        no      unfurnished

[5 rows x 13 columns]
>>> ##loc :Select by labels and iloc :Select by positions
>>> data.loc[:5,['price','area']]
      price  area
0  13300000  7420
1  12250000  8960
2  12250000  9960
3  12215000  7500
4  11410000  7420
5  10850000  7500
>>> data.iloc[:4,:6]
      price  area  bedrooms  bathrooms  stories mainroad
0  13300000  7420         4          2        3      yes
1  12250000  8960         4          4        4      yes
2  12250000  9960         3          2        2      yes
3  12215000  7500         4          2        2      yes
>>> ##Slicing rows and columns using labels
>>> data(0:
     
SyntaxError: invalid syntax
>>> data(0:4)
SyntaxError: invalid syntax
>>> data[0:4]
      price  area  bedrooms  ...  parking  prefarea furnishingstatus
0  13300000  7420         4  ...        2       yes        furnished
1  12250000  8960         4  ...        3        no        furnished
2  12250000  9960         3  ...        2       yes   semi-furnished
3  12215000  7500         4  ...        3       yes        furnished

[4 rows x 13 columns]
>>> ##Groupby :pandas groupby function is a great tool in exploring the data
>>> data[['price','area','bedrooms']].groupby(['price','area']).mean()
               bedrooms
price    area          
1750000  2910       3.0
         3620       2.0
         3850       3.0
1767150  2400       3.0
1820000  3000       2.0
...                 ...
11410000 7420       4.0
12215000 7500       4.0
12250000 8960       4.0
         9960       3.0
13300000 7420       4.0

[532 rows x 1 columns]
>>> ##Sorting :sort_index()method by default,sorting is done on row labels in ascending order
>>> data.sort_index(axis=1,ascending=TRUE)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    data.sort_index(axis=1,ascending=TRUE)
NameError: name 'TRUE' is not defined
>>> data.sort_index(axis=1,ascending=True)
    airconditioning  area basement  ...  prefarea     price stories
0               yes  7420       no  ...       yes  13300000       3
1               yes  8960       no  ...        no  12250000       4
2                no  9960      yes  ...       yes  12250000       2
3               yes  7500      yes  ...       yes  12215000       2
4               yes  7420      yes  ...        no  11410000       2
..              ...   ...      ...  ...       ...       ...     ...
540              no  3000      yes  ...        no   1820000       1
541              no  2400       no  ...        no   1767150       1
542              no  3620       no  ...        no   1750000       1
543              no  2910       no  ...        no   1750000       1
544              no  3850       no  ...        no   1750000       2

[545 rows x 13 columns]
>>> ##Sorting by values
>>> data.sort_values(by='area')
        price   area  bedrooms  ...  parking  prefarea furnishingstatus
449   3150000   1650         3  ...        0        no      unfurnished
537   1890000   1700         3  ...        0        no      unfurnished
527   2275000   1836         2  ...        0        no   semi-furnished
271   4340000   1905         5  ...        0        no   semi-furnished
413   3430000   1950         3  ...        0       yes      unfurnished
..        ...    ...       ...  ...      ...       ...              ...
403   3500000  12944         3  ...        0        no      unfurnished
10    9800000  13200         3  ...        2       yes        furnished
66    6930000  13200         2  ...        1        no        furnished
125   5943000  15600         3  ...        2        no   semi-furnished
7    10150000  16200         5  ...        0        no      unfurnished

[545 rows x 13 columns]
>>> ##Dropna :dropna() function is used to remove a row or a column from a dataframe which has a Na
>>> ##Dropna :dropna() function is used to remove a row or a column from a dataframe which has a NaN or no values in it
>>> drop_cols =['stories']
>>> data.drop(drop_cols,axis=1,inplace=True)
>>> data
        price  area  bedrooms  ...  parking prefarea furnishingstatus
0    13300000  7420         4  ...        2      yes        furnished
1    12250000  8960         4  ...        3       no        furnished
2    12250000  9960         3  ...        2      yes   semi-furnished
3    12215000  7500         4  ...        3      yes        furnished
4    11410000  7420         4  ...        2       no        furnished
..        ...   ...       ...  ...      ...      ...              ...
540   1820000  3000         2  ...        2       no      unfurnished
541   1767150  2400         3  ...        0       no   semi-furnished
542   1750000  3620         2  ...        0       no      unfurnished
543   1750000  2910         3  ...        0       no        furnished
544   1750000  3850         3  ...        0       no      unfurnished

[545 rows x 12 columns]
>>> ##Query :dataframe based on a condition or apply a mask to get certain values
>>> data.query('1700 <area<15600')[:8]
      price  area  bedrooms  ...  parking prefarea furnishingstatus
0  13300000  7420         4  ...        2      yes        furnished
1  12250000  8960         4  ...        3       no        furnished
2  12250000  9960         3  ...        2      yes   semi-furnished
3  12215000  7500         4  ...        3      yes        furnished
4  11410000  7420         4  ...        2       no        furnished
5  10850000  7500         3  ...        2      yes   semi-furnished
6  10150000  8580         4  ...        2      yes   semi-furnished
8   9870000  8100         4  ...        2      yes        furnished

[8 rows x 12 columns]
>>> ##insert :add new column or row to the dataframe
>>> #new column
>>> new_col=np.random(545)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    new_col=np.random(545)
TypeError: 'module' object is not callable
>>> new_col=np.random.randn(545)
>>> ##Insert the new column at position 8
>>> data.insert(8,'new_col',new_col)
>>> data.head()
      price  area  bedrooms  ...  parking prefarea furnishingstatus
0  13300000  7420         4  ...        2      yes        furnished
1  12250000  8960         4  ...        3       no        furnished
2  12250000  9960         3  ...        2      yes   semi-furnished
3  12215000  7500         4  ...        3      yes        furnished
4  11410000  7420         4  ...        2       no        furnished

[5 rows x 13 columns]
>>> data.insert(3,'new_col',new_col)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    data.insert(3,'new_col',new_col)
  File "C:\Users\prasa\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\frame.py", line 4414, in insert
    raise ValueError(f"cannot insert {column}, already exists")
ValueError: cannot insert new_col, already exists
>>> new_col=np.random.randn(545)
>>> data.insert(3,'new_col',new_col)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    data.insert(3,'new_col',new_col)
  File "C:\Users\prasa\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\frame.py", line 4414, in insert
    raise ValueError(f"cannot insert {column}, already exists")
ValueError: cannot insert new_col, already exists
>>> new_col1=np.random.randn(545)
>>> data.insert(3,'new_col1',new_col)
>>> data.head()
      price  area  bedrooms  ...  parking  prefarea furnishingstatus
0  13300000  7420         4  ...        2       yes        furnished
1  12250000  8960         4  ...        3        no        furnished
2  12250000  9960         3  ...        2       yes   semi-furnished
3  12215000  7500         4  ...        3       yes        furnished
4  11410000  7420         4  ...        2        no        furnished

[5 rows x 14 columns]
>>> 