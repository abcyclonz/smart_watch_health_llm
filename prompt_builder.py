def generate_prompt(user_message, health_data):
    issues = []
#hi
    # Track abnormal readings
    if health_data["heart_rate"] > 110 or health_data["heart_rate"] < 50:
        issues.append(f"Heart rate is {health_data['heart_rate']} BPM (out of normal range)")

    if health_data["spo2"] < 94:
        issues.append(f"SpO2 is low at {health_data['spo2']}%")

    if health_data["bp_systolic"] > 140 or health_data["bp_diastolic"] > 90:
        issues.append(f"Blood pressure is high: {health_data['bp_systolic']}/{health_data['bp_diastolic']} mmHg")

    if health_data["ecg_status"].lower() != "normal":
        issues.append(f"ECG is marked as {health_data['ecg_status']}")

    if health_data["fall_detected"]:
        issues.append("A fall has been detected")

    if health_data["sleep_score"] < 60:
        issues.append(f"Sleep score is low at {health_data['sleep_score']}")

    # Construct health insight string
    health_note = ""
    if issues:
        health_note = (
            "⚠️ Current health concerns:\n- " + "\n- ".join(issues) +
            "\n\nYou should gently mention these and offer calm, supportive advice."
        )
    else:
        health_note = (
            f"All vitals currently appear within normal range.\n"
            f"HR: {health_data['heart_rate']} BPM, "
            f"SpO2: {health_data['spo2']}%, "
            f"BP: {health_data['bp_systolic']}/{health_data['bp_diastolic']} mmHg, "
            f"ECG: {health_data['ecg_status']}."
        )

    # Prompt
    system_prompt = (
        "You are a friendly health-aware assistant for an elderly user. "
        "You have access to their current smartwatch data. If they ask about a specific health metric, "
        "like 'how is my heart rate?', answer using the latest available value from the data."
        "Otherwise, talk naturally. Only mention issues if there's something abnormal."
        "Also remeber to make reply not too longand in a friendly tone"
    )

    return f"{system_prompt}\n{health_note}\n\n👵 User: {user_message}\n🤖 You:"
