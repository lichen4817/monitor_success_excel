import  csv

def read_csv(path):
    data=[]
    with open(path,encoding='utf-8') as f:
        reader=csv.reader(f,dialect='excel')
        for row in reader:
            data.append(row)
    return data
data =read_csv('test.csv')
print(data)