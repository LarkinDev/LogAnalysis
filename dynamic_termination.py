class DynamicTermination:
    def __init__(self):
        self.text = ""
        self.time = []
        self.w_fraction = []
        self.found_time = []

    def transform_input(self, list):
        new_l = []
        for i in list:
            if i != "":
                new_l.append(i)
        return new_l

    def read_file(self, path):
        with open(path) as f:
            self.text = f.readlines()
        for i in range(3, len(self.text)):
            sp = self.text[i].strip().split("  ")
            new_sp = self.transform_input(sp)
            self.time.append(float(new_sp[0]))
            self.w_fraction.append(float(new_sp[1]))

    def find_t(self):
        for i in range(19999, len(self.time)):
            tmp_slice = []
            end = i - 20000
            if end < 0:
                tmp_slice = self.w_fraction[i::-1]
            else:
                tmp_slice = self.w_fraction[i:end:-1]
            if max(tmp_slice) - min(tmp_slice) < 0.1 and self.w_fraction[i] < 0.5:
                self.found_time.append(self.time[i])
