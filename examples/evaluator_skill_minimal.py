from root import RootSignals
from root.validators import Validator

client = RootSignals()

cooking_skill = client.skills.create(
    name="Cooking skill with validators",
    prompt="Find me a good recipe for Italian food.",
    validators=[
        Validator(
            evaluator_name="Cooking recipe evaluator",
            prompt="Is the following a cooking recipe: {{output}}",
            threshold=0.1,
        ),
        Validator(
            evaluator_name="Truthfulness",
            threshold=0.5,
        ),
    ],
)
response = cooking_skill.run()

# Check if the recipe was about cooking
print(response.validation)
