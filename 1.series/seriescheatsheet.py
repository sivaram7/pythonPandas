import pandas as pd

# <======= series ============>
#creating series
series = pd.Series([3,4,7,6,7,8,7,8,9,7])
print(series)

#shape
print(series.shape)     #shape (7,)

#RangeIndex(start=0, stop=7, step=1)
print(series.index)

#print count
print(series.count())   # 7


#selecting data
print('selecting datas')
print(series[6])

print(series[3:5])

#arithmetic
print('arithmetic')

print('sum',series.sum())
print('cumsum',series.cumsum())
print('min',series.min())
print('max',series.max())
print('idxmin',series.idxmin())
print('idxmax',series.idxmax())
print('describe',series.describe())
print('mean',series.mean())
print('median',series.median())

#sort and ranking
print('selecting rank')
print(series.rank())

#dropping data
drop = series.drop([5])   #index 5 will be deleted
print(drop)

#dropping multiple data
dropmultiple = series.drop([4,5,6])  # index 4,5,6 will be drop
print(dropmultiple)

#applying fuction
f = lambda x: x*2
modifiy_series=series.apply(f)
print(modifiy_series)

