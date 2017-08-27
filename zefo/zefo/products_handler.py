from django.shortcuts import render_to_response,redirect
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str, smart_unicode
import json

from products_model import ProductsModel

# handles /product/tv/filter/
# /product/mobile/filter/
@csrf_exempt 
def handle_request(request, category, action):
    response = {"status":"error"}
    query = request.GET.dict()
    filter_options = json.loads(query.get("filterOptions", "{}"))
    range_query = json.loads(query.get('rangeQuery',"{}"))
    aggregate_options = query.get('aggregateOptions',"")
    model = ProductsModel()
    response = model.get_products(category, filter_options, range_query, aggregate_options)
    response =  HttpResponse(json.dumps(response), content_type="application/json", status=200)
    return response

