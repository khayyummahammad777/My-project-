import matplotlib.pyplot as plt

# Sample data
categories = ['Male', 'Female', 'Other']
counts = [45, 55, 10]

# Create bar chart
plt.figure(figsize=(6,4))
plt.bar(categories, counts, color=['skyblue', 'lightpink', 'lightgreen'], edgecolor='black')

# Add labels and title
plt.title('Gender Distribution in Population')
plt.xlabel('Gender')
plt.ylabel('Number of People')

# Show count values above bars
for i, v in enumerate(counts):
    plt.text(i, v + 1, str(v), ha='center', fontweight='bold')

# Display chart
plt.tight_layout()
plt.show()

