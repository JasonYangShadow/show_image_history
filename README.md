# Show Docker Image history info from Dockerhub without downloading images

There are so many Docker images on Docker Hub, but when we want to check their image history, it is always painful especially when there are many images(over 1000+), therefore, this tool could help you extract and show history info from Docker Hub.

#### Prerequisites:

1. Install python3+, python3-pip
2. pip install -r requirements.txt
3. Download web driver from https://selenium.dev/

It employs selenium to render target URL and collect info from target web pages. It usually costs around 30 seconds to get the result.

main.py uses 'namespace', 'name', 'tag' and 'digest' as input, and output Docker Image History info collected from Docker Hub related pages.

```
Example:

python main.py --namespace biocontainers --name python-bz2file --tag v0.98-1-deb_cv1 --digest sha256:7e27b32378055a5e6c748d48b55f7f708da47b6dfee1728dd814ab5a463c344a

Return:

['ADD file:9c9710c289d7b177f13da3d0943894105f022e565f8e0ceb140319bfdd170c15 in / ', ' CMD ["bash"]', "/bin/sh -c echo 'deb http://deb.debian.org/debian stable-backports main' > /etc/apt/sources.list.d/backports.list", ' LABEL base.image=biocontainers/biocontainers:debian-strech-backports', ' LABEL version=1', ' LABEL software=Biocontainers debian based image', ' LABEL website=http://biocontainers.pro', ' LABEL documentation=https://github.com/BioContainers/specs/wiki', ' LABEL license=https://github.com/BioContainers/containers/blob/master/LICENSE', ' MAINTAINER Olivier Sallou <osallou@irisa.fr>', ' ENV DEBIAN_FRONTEND=noninteractive', '/bin/sh -c mkdir /data /config', '/bin/sh -c apt-get clean all &&     apt-get update &&     apt-get upgrade -y &&     apt-get install -y          fuse          &&          apt-get
clean &&         apt-get purge &&         rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*', '/bin/sh -c groupadd fuse &&     useradd --create-home --shell /bin/bash --user-group --uid 1000 --groups sudo,fuse biodocker &&     echo `echo "biodocker\\nbiodocker\\n" | passwd biodocker` &&     chown biodocker:biodocker /data &&     chown biodocker:biodocker /config', ' ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/biodocker/bin', ' ENV HOME=/home/biodocker', '/bin/sh
-c mkdir /home/biodocker/bin', ' VOLUME [/data /config]', ' CMD ["/bin/bash"]', 'WORKDIR /data', ' MAINTAINER biocontainers <biodocker@gmail.com>', ' LABEL software=python-bz2file container=python-bz2file about.summary=Python library for reading and writing bzip2-compressed files about.home=https://github.com/nvawda/bz2file software.version=0.98-1-deb version=1 about.copyright= 2012-2015 Nadeem Vawda <nadeem.vawda@gmail.com> about.license=Apache about.license_file=/usr/share/doc/python-bz2file/copyright about.tags=', ' ENV DEBIAN_FRONTEND=noninteractive', '/bin/sh -c apt-get update && apt-get install -y python-bz2file && apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*', ' USER [biodocker]']
```




