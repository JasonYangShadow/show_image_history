# Show Docker Image history info from Dockerhub without downloading images

There are so many Docker images on Docker Hub, but when we want to check their image history, it is always painful especially when there are many images(over 1000+), therefore, this tool could help you extract and show history info from Docker Hub.

#### Prerequisites:

1. Install python3+, python3-pip
2. pip install -r requirements.txt
3. Download web driver from https://selenium.dev/

It employs selenium to render target URL and collect info from target web pages.

main.py uses 'namespace', 'name', 'tag' and 'digest' as input, and output Docker Image History info collected from Docker Hub related pages.




