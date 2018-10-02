Building the image

```

docker image build -t akirachix-simple-invoice  .

```

Running the images

```
docker container run -p 8080:8080 --rm  -v /Users/jchencha/Google\ Drive/GDocuments/akirachix/classes/sem3/simple_invoice/app:/app akirachix-simple-invoice
```
