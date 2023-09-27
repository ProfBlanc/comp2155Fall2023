import csv
def example1():
    f = open("myfile.txt", "r+")
    f.write("here")
    f.seek(0)
    print(f.read())
def example21():
    with open("my.csv", "w") as f:
        w = csv.writer(f, lineterminator="\n")
        row = ["Ben", "Blanc", 100]
        w.writerow(row)

def example22():
    with open("my.csv", "w") as f:
        w = csv.writer(f, lineterminator="\n")
        rows = [["First Name", "Last Name", "Age"], ["John", "Smith", 105]]
        w.writerows(rows)

def example3():
    example21()

if __name__ == '__main__':
    example3()
