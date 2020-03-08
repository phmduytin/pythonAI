file = open('Iris.csv', 'r')

lines = file.readlines()

data = []

for i in range(1, len(lines)):
    string = lines[i].split(',')

    sepal_length = float(string[1].strip())
    sepal_width = float(string[2].strip())
    petal_length = float(string[3].strip())
    petal_width = float(string[4].strip())

    species = 0
    if string[5].strip() == 'Iris-versicolor':
        species = 1
    if string[5].strip() == 'Iris-virginica':
        species = 2

    data.append([sepal_length, sepal_width, petal_length, petal_width, species])



file.close()

print(data[0])