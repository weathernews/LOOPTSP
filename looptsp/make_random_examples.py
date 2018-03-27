import sys
import random
from convert_latlon2cost import Location2Cost 


if __name__ == "__main__":
    # random.seed(1)
    ports_num = int(sys.argv[1])
    digits = len(str(ports_num))
    location_list = list(map(lambda x: "PORT"+str(x).zfill(digits), range(ports_num)))

    location = dict()

    
    for location_name in location_list:
        while(1):
            lat = random.randint(0, 180)
            lon = random.randint(0, 360)
            latlon = {"lat": lat, "lon": lon}
            if latlon in location.values():
                pass
            else:
                location[location_name]=latlon
                break
    
    regularized_cost = Location2Cost.location2cost(location)
            
    Location2Cost.output_cost_as_csv(regularized_cost,sys.stdout)
