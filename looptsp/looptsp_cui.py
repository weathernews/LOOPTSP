from looptsp_env import LoopTSPEnvrionment, CostMatrix, Voyage

if __name__ == "__main__":
    tsp_env = LoopTSPEnvrionment('data/sample/cost.csv')
    voyage = Voyage(tsp_env,'TOKYO')
    while True:
        print('elpased date: {}'.format(voyage.elpased_time))
        print('Candidate ports')
        candidate_ports = voyage.get_candidate_arrival_ports()
        print(candidate_ports)
        for port in candidate_ports:
            print('{}: {} (Ideal : {})'.format(port, voyage.calc_actual_cost_of_current_status(port), voyage.get_ideal_cost_of_current_status(port)))
        print('Please input arrival port')
        arrival_port = input()
        if(arrival_port in candidate_ports):
            voyage.sail_to_next_port(arrival_port)
            if voyage.is_finished():
                print('Total date is {}'.format(voyage.elpased_time))
                break
        else:
            print('Illegal input')
