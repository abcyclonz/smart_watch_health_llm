import json

def get_health_from_file(file_path="health_data.json"):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Error reading health data: {e}")
        return {
            "heart_rate": 80,
            "spo2": 98,
            "bp_systolic": 120,
            "bp_diastolic": 80,
            "ecg_status": "Normal",
            "fall_detected": False,
            "sleep_score": 75
        }
