import numpy as np
import math
import logging as log
import time

from code_pipeline.tests_generation import RoadTestFactory


class TestsGenerator():
    """
        Generates a single test to show how to control the shape of the road by controlling the positio of the
        road points. We assume a map of 200x200
    """

    def __init__(self, executor=None, map_size=None):
        self.executor = executor
        self.map_size = map_size

    @property
    def road_points_1(self):
        road_points = []

        # Create an horizontal segment starting close to the left edge of the map
        x = 50.0
        y = 50.0
        road_points.append((x, y))
        x = x + 50
        y = y 
        road_points.append((x, y))

        return road_points
    
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

        self._execute(self.road_points_1)
        log.info("Finished executing all tests!")


