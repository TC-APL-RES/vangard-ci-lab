import pandas as pd
import matplotlib.pyplot as plt

# Load the master POA&M summary CSV
df = pd.read_csv('scans/master-poam-summary.csv')

# Count findings by tool and severity
summary = df.groupby(['Tool', 'Severity']).size().unstack(fill_value=0)

# Plotting
summary.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('VANGUARD CI: Findings by Tool and Severity')
plt.xlabel('Tool')
plt.ylabel('Number of Findings')
plt.legend(title='Severity')
plt.tight_layout()
plt.savefig('scans/vanguard-poam-summary.png')
print("📊 Visualization saved: scans/vanguard-poam-summary.png")
