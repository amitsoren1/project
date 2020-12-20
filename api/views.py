from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connections
# Create your views here.
class Api(APIView):
	def post(self,request):
		database = request.data.get("database_name",None)
		# cursor = connections[database].cursor()
		data = request.data.get("data",None)
		table_name = None
		select_list = None
		worksheet_id = None
		aggregate = None
		groupby = None
		if data:
			table_name = request.data["data"].get("table_name",None)
			select_list = request.data["data"].get("select_list",None)
			worksheet_id = request.data["data"].get("worksheet_id",None)
			aggregate = request.data["data"].get("aggregate",None)
			groupby = request.data["data"].get("groupby",None)
		print(database,table_name,select_list,worksheet_id,aggregate,groupby)
		
		if table_name:
			res = {"column":[],
					"data":[]}
			cursor.execute(f"select * from {table_name}")
			res["column"] = [x[0] for x in cursor.description]
			res["data"] = cursor.fetchall()
			return Response(res)

		if select_list:
			res = {"column":[],
					"data":[],
					"length":0}
			cols = ""
			for col in select_list:
				cols = cols + " " + col["column"]
			cursor.execute(f"select {cols} from {table_name}")
			res["column"] = [x[0] for x in cursor.description]
			res["data"] = cursor.fetchall()
			res["length"] = len(res["data"])
			return Response(res)

		return Response({"rsgrs":[("EFds",)]})