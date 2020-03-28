
file_names = ["AY274119", "AY278488.2", "MN908947", "MN988668", "MN988669"]
file_text = [0 for x in range(5)]

def longest_string(list):
    n = 0
    for x in list:
        if(len(x) > n):
            n = len(x)
    return n

def similitude(str_1,str_2):
    temp = 0;
    n = len(str_1) if len(str_1) < len(str_2) else len(str_2)
    for x in range(n):
        if (str_1[x] == str_2[x]):
            temp +=1
    return (round(temp/len(str_1)*100,2))


for i in range(len(file_names)):
    x = open("genomas/" + file_names[i] + ".txt", "r")
    x.readline()
    file_text[i] = x.read()
    file_text[i] = file_text[i].replace('\n', '')

print(" " * longest_string(file_names), end = "")

for i in range(len(file_names)):
    print(file_names[i], end = "\t")
print()


for i in range(len(file_names)):
    print(file_names[i] , end = " " * (longest_string(file_names) - len(file_names[i])))
    for j in range(len(file_names)):
        print(" " * (len(file_names[j])-5), end="")
        print(str(similitude(file_text[i],file_text[j])).ljust(5), end = '\t')
    print()
