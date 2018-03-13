from looptsp_env import LoopTSPEnvrionment, CostMatrix, Voyage
import sys

if __name__ == "__main__":
    cost_file = sys.argv[1]
    start_port = sys.argv[2]
    plan_file = sys.argv[3]
    tsp_env = LoopTSPEnvrionment(cost_file)
    voyage = Voyage(tsp_env,start_port)
    plan = list()
    with open(plan_file, 'r') as f:
        for line in f:
            plan.append(line.rstrip('\r\n'))

    for arrival_port in plan:
        voyage.sail_to_next_port(arrival_port)

    if voyage.is_finished():
        print('Total date is {}'.format(voyage.elpased_time))
    else:
        print('Illegal plan file')
