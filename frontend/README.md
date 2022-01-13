# Frontend 

For running the frontend application you just have to open the file _index.html_ in the navigatior 


## Docker

The frontend does not currently use a framework. Just create the _nginx_ image using Dockerfile.

```Bash
docker build -t nginx-test .
```

and run it

```Bash
docker run -d -p 8080:80 nginx-test
```
