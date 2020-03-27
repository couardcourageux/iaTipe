import pickle
import matplotlib.pyplot as plt

def import_data(num):

    fichier = open("data/essai{}".format(str(num)), "rb")
    data = pickle.load(fichier)
    fichier.close()
    return data


# for c, v in data.items():
#     print(c, v, "\n")

mth_to_view = [207, 217, 227, 206, 216, 226]
# mth_to_view = [140, 141, 142, 143, 144]
data_sheet = []
names = []
for i in mth_to_view:
    data_sheet.append(import_data(i))
    names.append("mth_{}".format(i))

nbGen = len(data_sheet[0]["points"])

gen = [i for i in range(nbGen)]

for c, v in data_sheet[0].items():
    print(c)

def displate( donnee):

    for i in range(len(names)):
        plt.plot(gen, data_sheet[i][donnee], label=names[i])
    plt.title(c)
    plt.legend()
    plt.show()


# compare("nbMvt")

def show():
    for i in range(len(names)):
        for c, v in data_sheet[i].items():
            print(c, v)


def compare(data1, data2):
    for i in range(len(names)):
        plt.plot(data_sheet[i][data2], data_sheet[i][data1], label=names[i])
        plt.title(data1 + "/" + data2)
    plt.legend()
    plt.show()


for c, v in data_sheet[0].items():
    displate( c)

# compare("points", "distance")




