import numpy as np
import math
import logging as log
import time
from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
from geopy import distance
from code_pipeline.tests_generation import RoadTestFactory


class OSMTestsGenerator():
    """
        Generates a single test to show how to control the shape of the road by controlling the positio of the
        road points. We assume a map of 200x200
    """

    SHEFFIELD_BBOX = [53.356987, -1.510101, 53.402656, -1.433196]
    KRAKOW_BBOX = [49.973493, 19.807804, 50.123627, 20.097225]

    def __init__(self, executor=None, map_size=None):
        self.executor = executor
        self.map_size = map_size #200

    def middle(self, points):
        return (max(points) + min(points)) / 2

    def query_osm(self, street_name, bbox):
        overpass = Overpass()
        query = overpassQueryBuilder(bbox=bbox,
        elementType='way',selector=f'"name"="{street_name}"')

        road_points = []
        for e in overpass.query(query).elements():
            for node in e.nodes():
                road_points.append((node.lat(),node.lon()))

        return road_points

    def _geo_to_simulation_points(self, geo_points):

        lats = [x for x,_ in geo_points] #geo x's
        lons = [y for _,y in geo_points] #geo y's
        geo_center = np.array((self.middle(lats),self.middle(lons)))

        sim_points = []

        for geo_point in geo_points:
            geo_point = np.array(geo_point)

            relative_to_geo_center = geo_point-geo_center
            dist = distance.distance(geo_center, geo_point).m
            theta = distance.atan2(relative_to_geo_center[1], relative_to_geo_center[0])

            sim_x = dist * np.cos(theta)
            sim_y = dist * np.sin(theta)
            
            sim_x += self.map_size/2
            sim_y += self.map_size/2

            sim_points.append((sim_x, sim_y))

        return sim_points

    @property
    def abney_street_points(self):
        geo_points = self.query_osm("Abney Street", self.SHEFFIELD_BBOX)
        return self._geo_to_simulation_points(geo_points)
    
    @property
    def burgundzka_street_points(self):
        geo_points = self.query_osm("Burgundzka", self.KRAKOW_BBOX)
        return self._geo_to_simulation_points(geo_points)    
    
    @property
    def skosna_street_points(self):
        geo_points = self.query_osm("Skośna", self.KRAKOW_BBOX)
        return self._geo_to_simulation_points(geo_points)    



    def _execute(self, test):
        # Creating the RoadTest from the points
        the_test = RoadTestFactory.create_road_test(test)
        # Send the test for execution
        test_outcome, description, execution_data = self.executor.execute_test(the_test)

        # Print test outcome
        log.info("test_outcome %s", test_outcome)
        log.info("description %s", description)

    def start(self):
        log.info("Starting test generation")
        

        # self._execute(self.abney_street_points)
        self._execute(self.skosna_street_points)
        log.info("Finished executing all tests!")


