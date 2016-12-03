import io
with io.open('tweetcontent.txt', "r", encoding="UTF-8") as fopen:
    filecontent = fopen.read().splitlines()

    sarcasm = io.open("sarcasm.txt","w",encoding = "UTF-8")
    nsarcasm = io.open("nsarcasm.txt","w",encoding="UTF-8")

    stext = ''
    ntext = ''
    for str in filecontent:
        label = str[-1:]
        str = str[:-1]

        if(int(label) == 1):
            stext += str + "\n"
        elif(int(label) == 0):
            ntext += str + "\n"

    sarcasm.write(stext)
    nsarcasm.write(ntext)

    sarcasm.close()
    nsarcasm.close()