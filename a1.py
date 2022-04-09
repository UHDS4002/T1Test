

class Core:
    def __init__(self):
        self.d = dict()

    def add_stu(self, _id, name, point):
        self.d[_id] = (name, point)

    def find_stu(self, _id):
        return self.d.get(_id)
        # or
        # if _id in self.d:
        #     return self.d[_id]
        # else:
        #     return None
