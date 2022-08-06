from check_residual import CheckResidual
from dynamic_termination import DynamicTermination

if __name__ == '__main__':
    # Task 1
    check_r = CheckResidual()
    check_r.read_file("log.run")
    check_r.log_analysis()
    check_r.write_to_csv()
    check_r.draw_graph()
    # Task 2
    dyn_term = DynamicTermination()
    dyn_term.read_file("alpha.water")
    dyn_term.find_t()
    print("Found time")
    print(dyn_term.found_time)
