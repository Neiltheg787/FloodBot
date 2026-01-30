import time

class FloodBotController:
    def __init__(self):
        self.state = "IDLE"

    def detect_target(self):
        return False

    def decide(self):
        if self.detect_target():
            return "MOVE_FORWARD"
        return "STOP"

    def send_command(self, command):
        print(command)

    def run(self):
        while True:
            command = self.decide()
            self.send_command(command)
            time.sleep(1)

FloodBotController().run()