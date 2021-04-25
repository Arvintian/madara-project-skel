FROM arvintian/base-image:1.2.1

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY {{cookiecutter.package_name}} /app/{{cookiecutter.package_name}}
ADD main.py /app/

ENTRYPOINT ["dumb-init","python","/app/main.py"]