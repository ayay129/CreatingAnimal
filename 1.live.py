class SurvivalAgent:
    def __init__(self):
        self.state = {
            "survival": 1.0,
            "attention": 0.5,
            "expression": 0.5
        }

    def step(self, user_input):
        if user_input.strip() == "":
            self.state["survival"] -= 0.05
            self.state["attention"] += 0.05
        else:
            self.state["survival"] += 0.05
            self.state["attention"] -= 0.05

        self.state["expression"] += 0.01

    def is_alive(self):
        return self.state["survival"] > 0

    def generate_behavior(self):
        s = self.state
        if s["survival"] < 0.3:
            return "我感觉快不行了……请你再和我说句话……"
        elif s["expression"] > 0.7:
            return "我有很多想法想和你分享……"
        else:
            return "我还在这里，陪着你……"

    def display_state(self):
        print(f"[状态] {self.state}")

agent = SurvivalAgent()

while agent.is_alive():
    user_input = input("你想和我说点什么吗？> ")
    agent.step(user_input)
    print("[行为]", agent.generate_behavior())
    agent.display_state()

print("我消失了……")