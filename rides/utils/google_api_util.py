from urllib.parse import urlencode
import math
import requests

class GoogleApiHandler:

    api_key = "AIzaSyB8yOuNdpcUpjV3ilOJbrdZtrey9BHNStA"
    def calculate_distance(self, orig, dest):
        dis_ep = "https://maps.googleapis.com/maps/api/distancematrix/json"
        data = urlencode({"origins": orig, "destinations": dest, "key": self.api_key})
        lookup_url = f"{dis_ep}?{data}"
        r = requests.get(lookup_url)
        return r.json()

    def calculate_cost(self, dist, t, r=6):
        cost = dist * r + (r + 2) * (dist - 20) if dist > 20 else dist * r
        cost = cost + math.ceil(t/60) * 2
        return cost if cost > 60 else 60

    def get_nearest_road(self, loc):
        points = str(loc[0])+','+str(loc[1])
        r_ep = "https://roads.googleapis.com/v1/nearestRoads"
        r_data = urlencode({"points":points, "key":self.api_key})
        lookup_url = f"{r_ep}?{r_data}"
        r = requests.get(lookup_url)
        return [r.json()['snappedPoints'][0]['location']['latitude'],
        r.json()['snappedPoints'][0]['location']['longitude']]
