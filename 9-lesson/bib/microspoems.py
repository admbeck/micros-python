def obrabotkastiha(file1, file2):
    '''lkbfxlfcbfgb./g,m'''
    with open(file1, mode='r', encoding="UTF-8") as f1:
        stix1 = []
        vline = f1.readlines()
        for line in vline:
            stix1.append(line.strip())

        cnt = 0
        test = open(file2, mode='a', encoding="UTF-8")
        test.write("\n")
        test.write(f"\t--------{file1}------\n")

        for line1 in stix1[::-1]:
            if cnt == len(stix1) // 2:
                test.write(f"{stix1[cnt]:50}\t => \t{line1}\n")
            else:
                test.write(f"{stix1[cnt]:50}\t    \t{line1}\n")
            cnt += 1
        test.close()


print(obrabotkastiha.__doc__)