# Frontend 

The frontend does not currently use a framework. Just create the _nginx_ image using Dockerfile.

```Bash
docker build -t nginx-test .
```

and run it

```Bash
docker run -d -p 8080:80 nginx-test
```
