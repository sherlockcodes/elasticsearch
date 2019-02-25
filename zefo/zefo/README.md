# Product Filter : Django + elastic search 

## How to Start a Server?

Go to project root directory and then execute given command to start server:

```shell
python manage.py runserver 0.0.0.0:8000
```

Django server will start and listen at port 8000 now


Download elasticsearch from https://www.elastic.co/downloads/elasticsearch and unzip it.

```shell
bin/elasticsearch
```

go to project folder and import dummy products given in products.json with below commands

```shell
curl -s -XPOST 'http://localhost:9200/_bulk' --data-binary @products.json
```

### Filter APIs

  - `GET /product/mobile/filter/`  => to filter all mobile products.

  - `GET /product/mobile/filter/?aggregateOptions=brand,simtype,condition` => get all products aggregated by brand, simtype, condition.

  - `GET /product/mobile/filter/?filterOptions={%22condition%22:%22Unboxed%20Phones,Gently%20Used%20Phones%22}`  => to filter mobile phones in Unboxed Phones & Gently Used Phones condition
  
  - `GET /product/mobile/filter/?filterOptions={%22condition%22:%22Unboxed%20Phones,Gently%20Used%20Phones%22}&rangeQuery={%22price%22:%229000-15000,20000-35000%22,%22displaysize%22:%224.0-6.0%22}`  => to filter mobile phones in Unboxed Phones & Gently Used Phones condition and price range from Rs 9000 - 15000 or 20000 - 35000 and screen size between 4.0 to 6.0



## pre-requests

project requests requests library.
pip install requests 


To read more about: 

Read below blog :)

https://medium.com/zefo-tech/elastic-search-from-beginner-to-intermediate-e4177c4c769f


 
