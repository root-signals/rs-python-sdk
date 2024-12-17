from root import RootSignals

# Connect to the Root Signals API
client = RootSignals()

# Add a self-hosted model using Ollama
model = client.models.create(
    name="ollama/llama3",
    # URL pointing to the model's endpoint. Replace this with your own endpoint.
    url="https://d65e-88-148-175-2.ngrok-free.app",
)

# Use the model in a skill
skill = client.skills.create(name="My model test", prompt="Hello, my model!", model="ollama/llama3")
