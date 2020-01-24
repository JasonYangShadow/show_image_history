from main import ShowHistory

"""
This file is only used for lpmx
"""

#remove content if starts with any word in words
class WordsFilter:
    def __init__(self, words):
        self.__words = words

    def filter(self, contents):
        if not isinstance(contents, list):
            raise Exception('content should be list type')
        new_content = []
        for c in contents:
            if self.__words:
                skip = False
                for word in self.__words:
                    if c.strip().startswith(word):
                        skip = True
                        break
                if not skip:
                    new_content.append(c)

        return new_content


#return True if any string in strings inside content
class StringFilter:
    def __init__(self, strings):
        self.__strings = strings

    def filter(self, contents):
        if not isinstance(contents, list):
            raise Exception('contents should be list type')

        for c in contents:
            if self.__strings:
                for string in self.__strings:
                    if c.find(string) >= 0:
                        return True
        return False

def main():
    sh = ShowHistory(20)
    fw = WordsFilter(["ADD","LABEL", "MAINTAINER"])
    sf = StringFilter(["apt-get install -t buster-backports -y"])
    #read data
    with open('biocontainers_digest') as data:
        with open('biocontainers_report','w+') as f:
            for line in data:
                vals = line.split( )
                print("**************** working on %s/%s:%s **********************\n" %(vals[0], vals[1],vals[2]))
                contents = sh.run(vals[0],vals[1],vals[2],vals[3])
                if contents:
                    contents = fw.filter(contents)
                    if sf.filter(contents):
                        #output to file markdown
                        f.write("| %s/%s:%s | 🆗 | |\n" %(vals[0], vals[1], vals[2]))
                    else:
                        for content in contents:
                            print(content)
                        choice = input('is it okay?(y/n): ')
                        if choice == 'y':
                            #output  to file markdown
                            f.write("| %s/%s:%s | 🆗 | |\n" %(vals[0], vals[1], vals[2]))
                        else:
                            reason = input('input your reason: ')
                            #output reason to file markdown
                            f.write("| %s/%s:%s | ⭕😭 | %s |\n" %(vals[0], vals[1], vals[2], reason))

if __name__=="__main__":
    main()
