from lib.stage.base import BaseStage

class RetryCounterStage(BaseStage):
    def __init__(self, uuid: str, 
                 n_retry: int):
        BaseStage.__init__(self, uuid)
        self.n_retry = n_retry

    def action(self):
        self.n_retry -=1
        self.success = True