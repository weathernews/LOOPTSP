import csv
import sys 
import math

def calc_cost(port1,port2):
    # sqrt and exponential are heuristic operations
    return math.sqrt((port1["lat"]-port2["lat"])**2+
                     (port1["lon"]-port2["lon"])**2
    )**(4/5)


if __name__ == "__main__":
    latlon_file =  sys.argv[1]
    cost_file = sys.argv[2]

    location = dict()
    with open(latlon_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if int(row[2]) > 0:
                location[row[0]] ={"lat": int(row[1]), "lon": int(row[2])}
            else:
                location[row[0]] ={"lat": int(row[1]), "lon": 360+int(row[2])}

    location_list = sorted(location.keys())
    cost = dict()
    for port1 in location_list:
        for port2 in location_list:
            if port1 == port2:
                break
            cost[(port1,port2)] = calc_cost(location[port1],location[port2])

    lowest_cost = min(cost.values())

    with open(cost_file,'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for port_pair, one_cost in sorted(cost.items(), key= lambda x:(x[0][0],x[0][1])):
            # All costs are reguralized by devined lowest_cost.
            # To avoid cost 1, all costs are added 1.
            # If an ideal cost is 1, actual cost do not change.
            writer.writerow([port_pair[0],port_pair[1],int(one_cost/lowest_cost+1)])
