FROM python:latest  #latest python version
COPY server.py ./    #puts the script from linux machine to container
EXPOSE 8080 #exposes the port so that the data can transfer on that port.
CMD [ "python", "./server.py"]
