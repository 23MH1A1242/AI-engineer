import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/emails.csv")

df['sent_date'] = pd.to_datetime(df['sent_date'], errors='coerce')

print("Dataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nSample Data:\n", df.head())


sender_counts = df['sender'].value_counts()
print("\nEmails per Sender:\n", sender_counts)

sender_counts.plot(kind='bar', title="Emails per Sender")
plt.xlabel("Sender")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("../data/emails_per_sender.png")
plt.close()

if 'sent_date' in df:
    daily_counts = df.groupby(df['sent_date'].dt.date).size()
    print("\nEmails per Day:\n", daily_counts)

    daily_counts.plot(kind='line', title="Emails Over Time")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("../data/emails_over_time.png")
    plt.close()
