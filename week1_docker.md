Question 1. Understanding docker first run
Run docker with the python:3.12.8 image in an interactive mode, use the entrypoint bash.

What's the version of pip in the image?

24.3.1
24.2.1
23.3.1
23.2.1

❯ docker run -it python:3.12.8 bash
root@ad53d4d6e8eb:/# pip --version


or

docker run python:3.12.8 pip --version
Answer: 24.3.1