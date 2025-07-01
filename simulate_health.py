# import random
# from datetime import datetime

# def simulate_health_data():
#     return {
#         "timestamp": datetime.now().isoformat(),
#         "heart_rate": random.randint(55, 130),
#         "spo2": random.randint(90, 99),
#         "bp_systolic": random.randint(110, 150),
#         "bp_diastolic": random.randint(70, 95),
#         "ecg_status": random.choice(["Normal", "Irregular", "Possible AFib"]),
#         "fall_detected": random.choice([False, False, False, True]),
#         "sleep_score": random.randint(50, 100),
#     }


def simulate_health_data():
    return {
        "heart_rate": 80,               
        "spo2": 97,                      
        "bp_systolic": 125,              
        "bp_diastolic": 75,              
        "ecg_status": "Normal",       
        "fall_detected": False,         
        "sleep_score": 90             
    }


# Metric	                 Normal Range               	Alert Thresholds
# Heart Rate (HR)	    60–100 BPM at rest	                🔴 <50 or >110 BPM
# SpO₂ (Oxygen)	        95–99%	                            🔴 <94%
# Blood Pressure (BP)	~110–130 / 70–85 mmHg	            🔴 >140 systolic or >90 diastolic
# ECG Status	        “Normal”	                        🔴 Irregular or “Possible AFib”
# Fall Detected	        False	                            🔴 True
# Sleep Score	        ≥ 70	                            ⚠️ <60 = poor sleep
# Respiratory Rate	    12–20 breaths/min	                🔴 >22 or <10
# Temperature (skin/core)	~36.5–37.5°C	                🔴 >38°C or <35°C