import unittest
from looptsp_env import LoopTSPEnvrionment, CostMatrix, Voyage

class TestLoopTSPENvironment(unittest.TestCase):
    def test_read_cost_csv(self):
        tsp_env = LoopTSPEnvrionment('data/sample/cost.csv')
        with self.assertRaises(KeyError):
            tsp_env.read_cost_csv('data/sample/invalid_cost.csv')
        
    def test_read_csv(self):
        content = LoopTSPEnvrionment.read_csv('data/sample/cost.csv')
        self.assertEqual('TOKYO',content[0][0])
        self.assertEqual('OSAKA',content[0][1])
        self.assertEqual('4',content[0][2])
        self.assertEqual('LONG_BEACH',content[14][0])
        self.assertEqual('SEATTLE',content[14][1])
        self.assertEqual('4',content[14][2])

    def test_calc_actual_cost(self):
        tsp_env = LoopTSPEnvrionment('data/sample/cost.csv')
        self.assertEqual(4,tsp_env.calc_actual_cost('TOKYO','OSAKA',0))
        self.assertEqual(4,tsp_env.calc_actual_cost('OSAKA','TOKYO',0))
        self.assertEqual(22,tsp_env.calc_actual_cost('NAGOYA','SEATTLE',0))

        self.assertEqual(4 + 1,tsp_env.calc_actual_cost('TOKYO','OSAKA',1))
        self.assertEqual(4 + 1,tsp_env.calc_actual_cost('TOKYO','OSAKA',5))
        self.assertEqual(4 + 0,tsp_env.calc_actual_cost('TOKYO','OSAKA',4))

        self.assertEqual(22 + 1,tsp_env.calc_actual_cost('NAGOYA','SEATTLE',1))
        self.assertEqual(22 + 0,tsp_env.calc_actual_cost('NAGOYA','SEATTLE',22))
        self.assertEqual(22 + 3,tsp_env.calc_actual_cost('NAGOYA','SEATTLE',25))
        self.assertEqual(22 + 7,tsp_env.calc_actual_cost('NAGOYA','SEATTLE',51))


class TestCostMatrix(unittest.TestCase):
    def test_add_cost(self):
        cost_matrix = CostMatrix()
        cost_matrix.add_cost("TOKYO","OSAKA",4)
        self.assertEqual(4,cost_matrix.cost_matrix[("TOKYO","OSAKA")])

class TestVoyage(unittest.TestCase):
    def invalid_voyage(self):
        tsp_env = LoopTSPEnvrionment('data/sample/cost.csv')
        voyage = Voyage(tsp_env,'TOKYO')
        voyage.sail_to_next_port('OSAKA')
        with self.assertRaises(Exception):
            voyage.sail_to_next_port('TOKYO')
        
    def test_voyage(self):
        tsp_env = LoopTSPEnvrionment('data/sample/cost.csv')
        voyage = Voyage(tsp_env,'TOKYO')
        self.assertEqual(4, voyage.calc_actual_cost_of_current_status('OSAKA'))
        with self.assertRaises(KeyError):
            self.assertEqual(4, voyage.calc_actual_cost_of_current_status('TOKYO'))

        voyage.sail_to_next_port('OSAKA')
        self.assertEqual(4, voyage.elpased_time)
        self.assertEqual({'OSAKA'}, voyage.arrived_ports)

        self.assertEqual(2, voyage.calc_actual_cost_of_current_status('NAGOYA'))     
        voyage.sail_to_next_port('NAGOYA')
        self.assertEqual(6, voyage.elpased_time)
        self.assertEqual(8 + 6, voyage.calc_actual_cost_of_current_status('SHANGHAI'))     
        voyage.sail_to_next_port('SHANGHAI')
        self.assertEqual(20, voyage.elpased_time)

        self.assertEqual(28 + 20, voyage.calc_actual_cost_of_current_status('LONG_BEACH'))     
        voyage.sail_to_next_port('LONG_BEACH')
        self.assertEqual(68, voyage.elpased_time)

        self.assertEqual(4 + 0, voyage.calc_actual_cost_of_current_status('SEATTLE'))
        self.assertEqual({'TOKYO','SEATTLE'}, voyage.get_candidate_arrival_ports())
        voyage.sail_to_next_port('SEATTLE')
        self.assertEqual(72, voyage.elpased_time)
        self.assertEqual(22 + 6, voyage.calc_actual_cost_of_current_status('TOKYO'))
        self.assertEqual({'TOKYO'}, voyage.get_candidate_arrival_ports())
        voyage.sail_to_next_port('TOKYO')
        self.assertEqual(True, voyage.finish_voyage)
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
        unittest.main()
