import os
import traceback

import plotly
import numpy as np

from flask.json import JSONEncoder
from flask import Flask, request, jsonify, make_response
from flask_restplus import Api, Resource, fields
from flask_cors import CORS

from sisl.viz import BlankSession
from sisl.viz.plotutils import load

class CustomJSONEncoder(JSONEncoder):

	def default(self, obj):

		if hasattr(obj, "to_json"):
			return obj.to_json()
		elif isinstance(obj, np.generic): 
			return obj.item() 

		try:
			return plotly.utils.PlotlyJSONEncoder.default(self, obj)
		except Exception:
			return JSONEncoder.default(self, obj)

app = Flask("SISL GUI Api")
app.json_encoder = CustomJSONEncoder

#This is so that the GUI's javascript doesn't complain about permissions
CORS(app)

api = Api(app = app, 
		  version = "1.0", 
		  title = "Sisl GUI Api", 
		  description = "Interact with your simulations results with the help of a graphical interface")

session = BlankSession()

class SessionManager(Resource):
	
	def get(self):
		try: 

			response = jsonify({
				"statusCode": 200,
				"status": "Plot types delivered",
				"session": session._getJsonifiableInfo()
			})
			return response
		except Exception as error:
			print(traceback.format_exc())
			return jsonify({
				"statusCode": 500,
				"status": "Could not make prediction",
				"error": str(error)
			})

	def post(self):
		
		try:

			global session

			requestBody = request.json
			additionalParams = {}

			if requestBody["action"] == "updateSettings":
				#Update this session's settings
				session.updateSettings(**requestBody["settings"])

			elif requestBody["action"] == "undoSettings":
				#Go back to previous settings
				session.undoSettings()
			
			elif requestBody["action"] == "save":
				#Save the session
				session.save( os.path.join(session.settings["rootDir"], requestBody["path"]) )
			
			elif requestBody["action"] == "load":
				#Load a saved session
				session = load( os.path.join(session.settings["rootDir"], requestBody["path"]) )
			
			elif requestBody["action"] == "updatePlots":
				#Update this session's settings
				additionalParams = {"justUpdated" : session.updates_available()}
				session.commit_updates()

			response = jsonify({
				"statusCode": 200,
				"status": "Options delivered",
				"session": session._getJsonifiableInfo(),
				**additionalParams
			})

			return response
		except Exception as error:
			print(traceback.format_exc())
			return jsonify({
				"statusCode": 500,
				"status": "Could not make perform operation on the current session",
				"error": str(error)
			})

class PlotTypes(Resource):

	def get(self):
		try: 

			options = [ {"value": subclass.__name__, "label": subclass._plotType} for subclass in session.getPlotClasses()]

			response = jsonify({
				"statusCode": 200,
				"status": "Plot types delivered",
				"plotOptions": options
			})
			return response
		except Exception as error:
			print(traceback.format_exc())
			return jsonify({
				"statusCode": 500,
				"status": "Could not find plot types",
				"error": str(error)
			})
	
class PlotManager(Resource):
		
	def get(self, plotID = False):
		
		try:
			if plotID:
				
				plot = session.getPlot(plotID)
			else:
				raise Exception("No ID of the desired plot was specified")

			response = jsonify({
				"statusCode": 200,
				"status": "Options delivered",
				"plot": plot._getDictForGUI()
			})

			return response
		except Exception as error:
			print(traceback.format_exc())
			return jsonify({
				"statusCode": 500,
				"status": "Could not make prediction",
				"error": str(error)
			})
	
	def post(self, plotID = False):
		
		try:
			if plotID:
				requestBody = request.json

				if requestBody["action"] == "updateSettings":
					#Update this plot settings
					plot = session.updatePlot(plotID, requestBody["settings"])

				elif requestBody["action"] == "undoSettings":
					#Go back to previous settings
					plot = session.undoPlotSettings(plotID)

				elif requestBody["action"] == "fullScreen":
					#Show the plot in full screen
					plot = session.getPlot(plotID)
					plot.show()


			else:
				#Get a new plot following the request parameters
				requestBody = request.json

				plot = session.newPlot( requestBody["plotClass"], tabID = requestBody["tabID"] , structID = requestBody["struct"], animation = requestBody["animation"])

			response = jsonify({
				"statusCode": 200,
				"status": "Options delivered",
				"plot": plot._getDictForGUI()
			})

			return response
		except Exception as error:
			print(traceback.format_exc())
			return jsonify({
				"statusCode": 500,
				"status": "Could not make prediction",
				"error": str(error)
			})
	
	def delete(self, plotID = False):
		
		try:
			if plotID:
				
				session.removePlot(plotID)

			else:
				raise Exception("A plot deletion was asked but no plot ID was provided.")

			response = jsonify({
				"statusCode": 200,
				"status": "Plot removed",
				"session": session._getJsonifiableInfo()
			})

			return response
		except Exception as error:
			print(traceback.format_exc())
			return jsonify({
				"statusCode": 500,
				"status": "Could not make prediction",
				"error": str(error)
			})
	
class StructsHandler(Resource):
	
	def get(self):

		try:

			response = jsonify({
				"statusCode": 200,
				"status": "Structures delivered",
				"structures": session.getStructures()
			})

			return response
		except Exception as error:
			print(traceback.format_exc())
			return jsonify({
				"statusCode": 500,
				"status": "Could not make prediction",
				"error": str(error)
			})

class TabManager(Resource):
	
	def get(self, tabID = None):

		try:

			if tabID == "new":

				session.addTab()
			
			#Return the current tabs of the session
			response = jsonify({
				"statusCode": 200,
				"status": "Tabs delivered",
				"tabs": session.getTabs()
			})

			return response
		except Exception as error:
			print(traceback.format_exc())
			return jsonify({
				"statusCode": 500,
				"status": "Could not make prediction",
				"error": str(error)
			})
	
	def delete(self, tabID = None):

		try:

			if tabID:
				session.removeTab(tabID)
			
			#Return the current tabs of the session
			response = jsonify({
				"statusCode": 200,
				"status": "Tab removed",
				"tabs": session.getTabs()
			})

			return response
		except Exception as error:
			print(traceback.format_exc())
			return jsonify({
				"statusCode": 500,
				"status": "Could not make prediction",
				"error": str(error)
			})
	
	def put(self, tabID = None):

		try:

			requestBody = request.json

			if tabID:
				session.updateTab(tabID, requestBody)
			
			#Return the current tabs of the session
			response = jsonify({
				"statusCode": 200,
				"status": "Tab removed",
				"tabs": session.getTabs()
			})

			return response

		except Exception as error:
			print(traceback.format_exc())
			return jsonify({
				"statusCode": 500,
				"status": "Could not make prediction",
				"error": str(error)
			})

api.add_resource(SessionManager, '/sislGUI/session')
api.add_resource(PlotTypes, '/sislGUI/plotTypes')
api.add_resource(StructsHandler, '/sislGUI/structs')
api.add_resource(TabManager, '/sislGUI/tab', '/sislGUI/tab/<string:tabID>' )
api.add_resource(PlotManager, '/sislGUI/plot','/sislGUI/plot/<string:plotID>')

if __name__ == '__main__':
	app.run(debug=True, port = 4000) #host = "192.168.0.103"
