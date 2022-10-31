fnames = ["file7.txt", "file1.png", "file3.txt", "file2.txt",
          "file7.txt", "file1.txt", "file3.txt", "file4.png",
          "file4.png", "file5.txt", "file0.txt", "file7.dat"]


for i in fnames:
    count = 0
    for j in fnames:
        if i == j:
            count += 1
            if count > 1:
                fnames.remove(j)

for i in fnames:
    if not i.endswith('.txt'):
        fnames.remove(i)

fnames.sort()
print(fnames)
