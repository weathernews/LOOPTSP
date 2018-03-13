import csv


class CostMatrix:
    def __init__(self):
        self.cost_matrix = dict()
        self.port_list = set()

    def validate_matrix(self):
        for port_name1 in list(self.port_list):
            for port_name2 in self.port_list:
                if port_name1 == port_name2:
                    continue 
                self.get_cost(port_name1,port_name2)

                
    def _add_cost(self, port_name1, port_name2,cost):
        self.cost_matrix[(port_name1,port_name2)] = cost

    def add_port(self, port_name):
        self.port_list.add(port_name)
        
    def add_cost(self, port_name1, port_name2,cost):
        self._add_cost(port_name1, port_name2,cost)
        self._add_cost(port_name2, port_name1,cost)
        self.add_port(port_name1)
        self.add_port(port_name2)

    def get_cost(self, port_name1, port_name2):
        return self.cost_matrix[(port_name1,port_name2)]
        
        
class LoopTSPEnvrionment:

    @staticmethod
    def read_csv(cost_file):
        content_list = list()
        with open(cost_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                content_list.append(row)
        return content_list

    
    def calc_additional_cost(self, depareture_day, ideal_cost):
        return depareture_day % ideal_cost

    
    def calc_actual_cost(self, depareture_port, arrival_port, depareture_day):
        ideal_cost = self.cost_matrix.get_cost(depareture_port, arrival_port)
        additional_cost = self.calc_additional_cost(depareture_day, ideal_cost)

        return ideal_cost + additional_cost
        
        
    

    def list2matrix(self,content_list):
        cost_matrix = CostMatrix()
        for row in content_list:
            port_name1 = row[0]
            port_name2 = row[1]
            cost = int(row[2])
            cost_matrix.add_cost(port_name1, port_name2, cost)
        try :
            cost_matrix.validate_matrix()
        except KeyError:
                print("InvalidCostMatrix")
                raise
        return cost_matrix

    def __init__(self, cost_file):
        self.read_cost_csv(cost_file)
        self.port_list = self.cost_matrix.port_list
        
    def read_cost_csv(self, cost_file):
        content_list = self.read_csv(cost_file)
        self.cost_matrix = self.list2matrix(content_list)

        
class Voyage:
    def __init__(self, environment, start_port):
        self.environment = environment
        self.start_port = start_port
        self.arrived_ports = set()
        self.current_port = start_port
        self.elpased_time = 0
        self.finish_voyage = False

    def is_finished(self):
        return self.finish_voyage
        
    def calc_actual_cost_of_current_status(self, arrival_port):
        return self.environment.calc_actual_cost(self.current_port, arrival_port, self.elpased_time)

    def get_ideal_cost_of_current_status(self, arrival_port):
        return self.environment.cost_matrix.get_cost(self.current_port, arrival_port)
    
    def get_candidate_arrival_ports(self):
        temp = self.environment.port_list.difference(self.arrived_ports).difference({self.start_port})
        if len(temp) == 0:
            return {self.start_port}
        else:
            return temp
        

    
    def check_valid_voyage(self):
        return self.environment.port_list == self.arrived_ports
    
    def sail_to_next_port(self, arrival_port):
        actual_cost = self.calc_actual_cost_of_current_status(arrival_port)
        self.elpased_time += actual_cost
        self.current_port = arrival_port
        self.arrived_ports.add(arrival_port)
        if(arrival_port == self.start_port):
            if self.check_valid_voyage():
                self.finish_voyage = True
                return self.elpased_time
            else:
                raise Exception
        else:
            return None

