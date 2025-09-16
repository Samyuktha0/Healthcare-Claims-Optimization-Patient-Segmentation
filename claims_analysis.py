import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load data
df = pd.read_excel("data/claims_data.xlsx")

# RFM Segmentation
rfm = df.groupby('PatientID').agg({
    'ClaimDate': lambda x: (df['ClaimDate'].max() - x.max()).days,
    'ClaimID': 'count',
    'ClaimAmount': 'sum'
}).rename(columns={'ClaimDate': 'Recency', 'ClaimID': 'Frequency', 'ClaimAmount': 'Monetary'})

# Clustering
kmeans = KMeans(n_clusters=4)
rfm['Segment'] = kmeans.fit_predict(rfm)

# Save segmented data
rfm.to_csv("rfm_segments.csv")

# Plot segments
rfm.plot(kind='scatter', x='Recency', y='Monetary', c=rfm['Segment'], colormap='viridis')
plt.title("Patient Segmentation")
plt.show()
