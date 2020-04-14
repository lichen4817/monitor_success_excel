import csv

def csv_write(path,data):
    with open(path,'w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f,dialect='excel')
        for row in data:
            writer.writerow(row)
    return True

data = [
    ['Name','Height'],
    ['Keys','176cm'],
    ['HongPing','160cm'],
    ['WenChao','176cm']
]

csv_write('test.csv',data)