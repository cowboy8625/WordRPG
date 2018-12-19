import json


class example:
    def __init__(self):
        self.running = 4
        self.ran = 5


def jdefault(o):
    return o.__dict__


class save_engine:
    def save(self, object):
        data = open('saved_data.txt', 'wb')
        save = json.dumps(object, default=jdefault)
        data.write(save.encode())
        data.close()
    def load(self,file,object):
        data = open(file,'r')
        raw_data = data.read()
        data.close()
        read_data = json.loads(raw_data)
        object.__dict__ = read_data
        print(object.running)


save_engine1 = save_engine()
eg = example()
save_engine1.save(eg)
save_engine1.load("saved_data.txt",eg)

