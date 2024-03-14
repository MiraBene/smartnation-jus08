class BaseStage:
    def __init__(self, uuid: str):
        self.uuid = uuid
        self.data = None
        self.success = False

    def reset(self):
        self.data = None
        self.success = False

    def action(self):
        raise NotImplementedError()
    
    def run(self, *args, **kwargs):
        print(f"run {self.uuid} stage")
        self.action(*args, **kwargs)

    def did_succeed(self):
        return self.success
