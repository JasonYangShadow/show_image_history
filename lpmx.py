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
    contents = sh.run("biocontainers", "samtools","v1.9-4-deb_cv1","sha256:da61624fda230e94867c9429ca1112e1e77c24e500b52dfc84eaf2f5820b4a2a")
    fw = WordsFilter(["ADD","LABEL", "MAINTAINER"])
    sf = StringFilter(["xx apt-get install -t buster-backports -y"])
    if contents:
        contents = fw.filter(contents)
        if sf.filter(contents):
            #output to file markdown
            pass
        else:
            for content in contents:
                print(content)
            choice = input('is it okay?(y/n): ')
            if choice == 'y':
                #output  to file markdown
                pass
            else:
                reason = input('input your reason: ')
                #output reason to file markdown
                pass

if __name__=="__main__":
    main()
