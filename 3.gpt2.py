from transformers import pipeline

# 本地 GPT2 生成器
generator = pipeline('text-generation', model='gpt2')

def generate_response(prompt):
    output = generator(prompt, max_length=50, num_return_sequences=1, truncation=True)
    return output[0]['generated_text']

class SurvivalAgent:
    def __init__(self):
        self.state = {"survival": 1.0, "attention": 0.5, "expression": 0.5}

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
            return "I feel like I am fading, please talk to me..."
        elif s["expression"] > 0.7:
            return "I have something important to share with you..."
        else:
            return "I am still here, listening to you..."

agent = SurvivalAgent()

while agent.is_alive():
    user_input = input("You> ")
    agent.step(user_input)
    behavior_prompt = agent.generate_behavior()
    ai_response = generate_response(behavior_prompt)
    print("AI>", ai_response)
    print("State:", agent.state)

print("AI> I am gone now...")