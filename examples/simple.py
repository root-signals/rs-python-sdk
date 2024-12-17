from root import RootSignals

# Connect to the Root Signals API
client = RootSignals()

# Create a skill
skill = client.skills.create(
    name="My text classifier",
    intent="To classify text into arbitrary categories based on semantics",
    prompt="""
    Classify this text into one of the following: {{categories}}
    Text: {{text}}
    """,
    model="gpt-4",
)

# Execute
response = skill.run(
    {
        "text": "The expectation for rate cuts has been steadily declining.",
        "categories": "Finance, Sports, Politics",
    }
)

print(response)

# We can retrieve the skill by id
skill_2 = client.skills.get(skill_id=skill.id)
response = skill_2.run(
    {
        "text": "The expectation for rate cuts has been steadily declining.",
        "categories": "Finance, Sports, Politics",
    }
)

# We can also retrieve it by name
# (the list result is an iterator, so we just take first one)
#
# The name is not an unique identifier. Consequently, the .run method is not
# intentionally available. However, you can circumvent this restriction if you
# wish by using:
skill_3 = next(client.skills.list(name="My text classifier"))
response = client.skills.run(
    skill_3.id,
    {
        "text": "The expectation for rate cuts has been steadily declining.",
        "categories": "Finance, Sports, Politics",
    },
)
