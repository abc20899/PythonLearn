class Android(object):
    os_version = ''  # 定义属性
    status = ''
    model = ''
    name = ''
    memory = ''

    def __init__(self):
        print("init")

    def __init__(self, os_version, status, model, name, memory):
        self.os_version = os_version
        self.status = status
        self.model = model
        self.name = name
        self.memory = memory
        print("重载")

    def set_name(self, name):
        self.name = name


if __name__ == '__main__':
    pass
