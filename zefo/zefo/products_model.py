import requests 

import query_builder
import consts
import json

class ProductsModel:
	def __init__(self):
		pass

	def get_products(self, category, filter_options, range_query, aggregation_options):
		query = query_builder.build_query(filter_options, range_query, aggregation_options)
		response = requests.get(consts.ES_URL + category + "/_search", data = json.dumps(query))
		if response.status_code == 200:
			body = json.loads(response.text)
			products = []
			aggregations = []
			count = 0
			if "hits" in body and "hits" in body["hits"] and len(body["hits"]["hits"]):
				count = body["hits"]["total"]
				for product in body["hits"]["hits"]:
					products.append(product['_source'])
			if "aggregations" in body:
				for key, value in body["aggregations"].iteritems():
					filter_list = { key:[] }
					for bucket in body["aggregations"][key]["buckets"]:
						filter_list[key].append({"key":bucket["key"],"count":bucket["doc_count"],"show":bucket["doc_count"] >= 1})
					aggregations.append(filter_list)
			response ={ "products":products, "filterList":aggregations, "count":count, "status":"success" }
		else:
			response = {"status":"error","reason":"problem fetching products"}
		return response