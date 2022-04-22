import pandas
import statistics as st

alldata = pandas.read_csv('https://raw.githubusercontent.com/DishaChhabra/Project-104-Ref-/main/SOCR-HeightWeight.csv')
data = alldata['Weight(Pounds)']

# MEAN - 
sum = 0
for i in data:
    sum = sum+i
mean1 = sum/len(data)
mean2 = st.mean(data)
print(mean1, mean2)

# MODE -
mode1 = data.value_counts()
mode2 = st.mode(data)
print(mode1, mode2)

# MEDIAN -
data2 = data.tolist()
data2.sort()
n = len(data)
if n%2==0:
    n1 = float(data[n//2])
    n2 = float(data[n//2+1])
    median1 = (n1+n2)/2
else:
    median1 = float(data[n//2])
median2 = st.median(data)
print(median1,median2)