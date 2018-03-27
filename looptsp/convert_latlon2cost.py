import csv
import sys 
import math

class Location2Cost:
    @staticmethod
    def calc_cost(port1,port2):
        # sqrt and exponential are heuristic operations
        return math.sqrt((port1["lat"]-port2["lat"])**2+
                         (port1["lon"]-port2["lon"])**2
        )**(4/5)

    @staticmethod
    def location2cost(location):
        location_list = sorted(location.keys())
        cost = dict()
        for port1 in location_list:
            for port2 in location_list:
                if port1 == port2:
                    break
                # All costs are reguralized by devined lowest_cost.
                # To avoid cost 1, all costs are added 1.
                # If an ideal cost is 1, actual cost do not change.
                cost[(port1,port2)] = Location2Cost.calc_cost(location[port1],location[port2])

        lowest_cost = min(cost.values())
        regularized_cost = dict()
        for port_pair in cost.keys():
            regularized_cost[port_pair] = int(cost[port_pair]/lowest_cost+1)
        return regularized_cost
        

    @staticmethod
    def output_cost_as_csv(regularized_cost,file_object):
        writer = csv.writer(file_object, lineterminator='\n')
        for port_pair, one_cost in sorted(regularized_cost.items(), key= lambda x:(x[0][0],x[0][1])):
            writer.writerow([port_pair[0],port_pair[1],one_cost])
        
            
        
        
if __name__ == "__main__":
    latlon_file =  sys.argv[1]
    

    location = dict()
    with open(latlon_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if int(row[2]) > 0:
                location[row[0]] ={"lat": int(row[1]), "lon": int(row[2])}
            else:
                location[row[0]] ={"lat": int(row[1]), "lon": 360+int(row[2])}

    regularized_cost = Location2Cost.location2cost(location)


    

    if len(sys.argv) == 3:
        cost_file = sys.argv[2]
        with open(cost_file,'w') as f:
            Location2Cost.output_cost_as_csv(regularized_cost,f)
    else:
        f = sys.stdout
        Location2Cost.output_cost_as_csv(regularized_cost,f)
