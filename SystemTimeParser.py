import subprocess

##Parser

sysaverages = []
useraverages = []
realaverages = []

with open ("data log", "r") as infile:
    with open("parsed.txt", "w") as outfile:
        sys = []
        user = []
        real = []
        for line in infile:
            if len(sys)==10:
                sysaverages.append(sum(sys)/len(sys))
                del sys[:]
            if len(user)==10:
                useraverages.append(sum(user)/len(user))
                del user[:]
            if len(real) == 10:
                realaverages.append(sum(real)/len(real))
                del real[:]
                        
            
            if line != '\n':
                if "sys" in line:
                    line2 = line.split('0m')
                    #print(line2)
                    #print(line2[1])
                    #print(line2[1].strip()[:-1])
                    number = float(line2[1].strip()[:-1])
                    sys.append(number)
                elif "user" in line:
                    line3 = line.split('0m')
                    number = float(line3[1].strip()[:-1])
                    user.append(number)
                else:
                    pass
            
        outfile.write(str(sysaverages) +'\n')
        outfile.write(str(useraverages)+'\n')
        outfile.write(str(realaverages)+'\n')

