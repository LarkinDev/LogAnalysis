import re
import csv
import matplotlib.pyplot as plt


class CheckResidual:
    def __init__(self):
        self.text = ""
        self.p_rgh = []
        self.omega = []
        self.k = []
        self.time = []

    def read_file(self, path):
        with open(path) as f:
            self.text = f.read().rstrip()

    def get_p_rgh(self, substring):
        p_rghs = re.findall("Solving for p_rgh.*,", substring)
        x = p_rghs[len(p_rghs) - 1].split(",")
        y = x[len(x) - 2].split(" = ")
        self.p_rgh.append(float(y[len(y) - 1]))

    def get_omega(self, substring):
        omegas = re.findall("Solving for omega.*,", substring)
        x = omegas[len(omegas) - 1].split(",")
        y = x[len(x) - 2].split(" = ")
        self.omega.append(float(y[len(y) - 1]))

    def get_k(self, substring):
        ks = re.findall("Solving for k.*,", substring)
        x = ks[len(ks) - 1].split(",")
        y = x[len(x) - 2].split(" = ")
        self.k.append(float(y[len(y) - 1]))

    def get_time(self, substring):
        times = re.findall("Time = .*", substring)
        x = times[0].split("=")
        self.time.append(float(x[len(x) - 1]))

    def write_to_csv(self):
        with open('data.csv', 'a') as file:
            writer = csv.writer(file)
            header = ["time", "p_rgh", "omega", "k"]
            writer.writerow(header)
            for i in range(len(self.time)):
                t = [self.time[i], self.p_rgh[i], self.omega[i], self.k[i]]
                writer.writerow(t)

    def log_analysis(self):
        substrings = re.findall("deltaT([^<>]+)ExecutionTime", self.text)[0].split("deltaT")
        for s in substrings:
            self.get_p_rgh(s)
            self.get_omega(s)
            self.get_k(s)
            self.get_time(s)

    def draw_graph(self):
        plt.plot(self.time, self.k, label="k")
        plt.plot(self.time, self.omega, label="omega")
        plt.plot(self.time, self.p_rgh, label="p_rgh")
        plt.xlabel("Time")
        plt.ylabel("Final residual")
        plt.legend()
        plt.yscale("log")
        plt.show()


