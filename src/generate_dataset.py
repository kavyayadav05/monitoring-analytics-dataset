import pandas as pd
import random

def generate_data(num_records=100):
    data = []

    for i in range(1, num_records + 1):
        candidate_id = 100 + i
        risk_score = random.randint(0, 100)
        phone_events = random.randint(0, 5)
        session_duration = random.randint(10, 120)

        data.append([
            candidate_id,
            risk_score,
            phone_events,
            session_duration
        ])

    df = pd.DataFrame(data, columns=[
        "candidate_id",
        "risk_score",
        "phone_events",
        "session_duration"
    ])

    # Remove duplicates
    df = df.drop_duplicates(subset=["candidate_id"])

    # Handle missing values
    df = df.fillna(0)

    # Validation checks
    assert df['risk_score'].between(0, 100).all()
    assert (df['phone_events'] >= 0).all()
    assert (df['session_duration'] > 0).all()

    return df


if __name__ == "__main__":
    df = generate_data(200)
    df.to_csv("data/dataset.csv", index=False)
    print("✅ Dataset generated successfully!")