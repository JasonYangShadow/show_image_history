import argparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

class ShowHistory:
    
    def __init__(self, wait):
        self.__base_url = 'https://hub.docker.com/layers/biocontainers'
        self.__timewait = wait

    def run(self, namespace, name, tag, digest):
        target_url = "%s/%s/%s/%s/images/%s" %(self.__base_url, namespace, name, tag, digest.replace(':','-'))
        content = []
        try:
            options = Options()
            options.add_argument('-headless')
            driver = Firefox(executable_path='geckodriver', options=options)
            driver.implicitly_wait(self.__timewait)
            driver.get(target_url)
            divs = driver.find_elements(By.XPATH, "//div[@data-testid='imglayersLayerListItem']")
            if divs:
                for div in divs:
                    #click every layer info
                    div.click()
                    #get details info on the right detail panel
                    detail_div = driver.find_element_by_xpath("//div[@data-testid='imglayersLayerInstruction']")
                    if detail_div:
                        ddivs = detail_div.find_elements(By.XPATH,".//div")
                        content.append(ddivs[3].text)
            driver.quit()
            return content
        except Exception as e:
            raise e

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--namespace', help = 'target namespace on Dockerhub', required = True)
    parser.add_argument('--name', help = 'image name on github', required = True)
    parser.add_argument('--tag', help = 'tag info of target image', required = True)
    parser.add_argument('--digest', help = 'digest value of target image', required = True)
    args = vars(parser.parse_args())
    sh = ShowHistory(20)
    print(sh.run(args['namespace'], args['name'], args['tag'], args['digest']))

if __name__ == "__main__":
    main()
