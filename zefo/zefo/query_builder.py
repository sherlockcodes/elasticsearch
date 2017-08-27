# method to build complex filter with both filter options, range query and aggregation 
# with help of nested filters.
def build_query(filter_options, range_query, aggregation_options):
	query = {"constant_score":{"filter":{"bool":{"must":[]}}}}
	inner_query = query["constant_score"]["filter"]["bool"]["must"]
	add_filter_options(inner_query, filter_options)
	inner_query = query["constant_score"]["filter"]["bool"]["must"]
	add_range_query(inner_query, range_query)
	aggr_query = get_aggreate_query(aggregation_options)
	final_query = {"query":query}
	if len(aggr_query):
		final_query["aggs"] = aggr_query
	return final_query

def add_filter_options(inner_query, filter_options):
	if len(filter_options):
		for key,value in filter_options.iteritems():
			inner_query.append({"terms":{key:value.split(",")}})

def add_range_query(inner_query, range_query):
	if len(range_query):
		new_query = {"bool":{"should":[]}}
		sub_range_query = new_query["bool"]	
		for key,value in range_query.iteritems():
			for range in value.split(","):
				if "-" in range:
					from_range , to_range = (range.split('-'))
				else:
					from_range = to_range = range
				sub_range_query["should"].append({ "range": { key: { "gte": float(from_range), "lte": float(to_range) } } } )
			sub_range_query["must"] = [{"bool":{"should":[]}}]
			sub_range_query = sub_range_query["must"][0]["bool"]
		inner_query.append(new_query)

def get_aggreate_query(aggregation_options):
	aggr_query = {}
	if aggregation_options:
		aggregation_options = aggregation_options.split(',')
		for option in aggregation_options:
			aggr_query[option] = {"terms":{"field":option}}
	return aggr_query



# query = build_query({},{},"brand,screentype,price,size")
# print query

# query = build_query({"condition":"Unboxed,Unboxed Plus"}, {"price":"10000-14000,20000-25000","size":"30-32,36-38","dummy":"100-200"},"brand,screentype,price,size")
# print query


