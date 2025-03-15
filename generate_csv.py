import pandas as pd

# Define correct synthetic government policy data
data = {
    "Policy Name": [
        "Tax Policy", 
        "Education Policy", 
        "Healthcare Policy", 
        "Employment Policy", 
        "Environmental Policy"
    ],
    "Description": [
        "Guidelines and laws related to taxation and revenue collection.",
        "Rules and regulations for public and private education systems.",
        "Policies on public health, hospitals, and medical support programs.",
        "Government rules on job creation, labor laws, and employee benefits.",
        "Regulations on pollution control, climate change, and conservation efforts."
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV file with correct format
df.to_csv("government_policies.csv", index=False)

print("✅ Fixed: 'government_policies.csv' has been created successfully!")
