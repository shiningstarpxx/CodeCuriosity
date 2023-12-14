class VectorClock:
    def __init__(self):
        self.clock = {}

    def increment(self, node_id):
        if node_id not in self.clock:
            self.clock[node_id] = 0
        self.clock[node_id] += 1

    def update(self, other_clock):
        for node_id, timestamp in other_clock.clock.items():
            if node_id not in self.clock or self.clock[node_id] < timestamp:
                self.clock[node_id] = timestamp

    def compare(self, other_clock):
        is_less_than = False
        is_greater_than = False

        for node_id, timestamp in self.clock.items():
            if node_id not in other_clock.clock or other_clock.clock[node_id] < timestamp:
                is_greater_than = True
            elif other_clock.clock[node_id] > timestamp:
                is_less_than = True

        for node_id, timestamp in other_clock.clock.items():
            if node_id not in self.clock:
                is_less_than = True

        if is_less_than and is_greater_than:
            return "concurrent"
        elif is_less_than:
            return "less_than"
        elif is_greater_than:
            return "greater_than"
        else:
            return "equal"