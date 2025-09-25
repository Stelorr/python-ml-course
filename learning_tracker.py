# Takes study time information and stores in dictionary
def learning_session(hours_studied, topic_studied, difficulty_level = 3, notes = ""):
    if not (0.25 <= hours_studied <= 8):
        print(f"Invalid hours: {hours_studied}. Must be between 0.25 and 8.")
        return None

    if not(1 <= difficulty_level <=5):
        print(f"Invalid difficulty: {difficulty_level}. Must be between 1 and 5.")
        return None

    return {
        'hours': hours_studied,
        'topic': topic_studied,
        'difficulty': difficulty_level,
        'notes': notes
    }

# # test case
# # Should work
# result = learning_session(2, "Python basics", 3, "Great session!")
# print(result)

# # Should give error
# result = learning_session(10, "Too long", 7, "Invalid data")
# print(result)

# Function to perform weekly analysis and provides recommendations based on data
def weekly_analyzer(session_list):
    total_hours = 0
    total_difficulty = 0
    topic_count = {}

    for session in session_list:
        hours = session['hours']
        topic = session['topic']
        difficulty = session['difficulty']

        total_hours += hours
        total_difficulty += difficulty

        if topic in topic_count:
            topic_count[topic] += 1
        else:
            topic_count[topic] = 1

    average_session = total_hours / len(session_list)
    average_difficulty = total_difficulty / len(session_list)

    most_studied_topic = ""
    if len(topic_count) == 0:
        print("Dictionary is empty")
        return None
    else:
        highest_count = 0
        most_studied_topic = ""
        for topic, count in topic_count.items():
            if count > highest_count:
                highest_count = count
                most_studied_topic = topic

    # Generate recommendation based on data
    if average_session >= 2.0:
        recommendation = "Great session lengths! Try increasing difficulty."
    elif average_session >= 1.0:
        recommendation = "Good consistency! Consider longer sessions."
    else:
        recommendation = "Try for longer study sessions next week."

    return {
        'total_hours': total_hours,
        'average_session_length': average_session,
        'average_difficulty': average_difficulty,
        'topic_counts': topic_count,
        'most_studied_topic': most_studied_topic,
        'recommendation': recommendation
    }


# # test case
# # Create multiple sessions using your learning_session function
# session1 = learning_session(1.5, "Python basics", 2, "Good start")
# session2 = learning_session(2.0, "Functions", 3, "Challenging")
# session3 = learning_session(1.0, "Python basics", 2, "Review")
# session4 = learning_session(2.5, "Control flow", 4, "Hard but useful")

# # Put them in a list
# weekly_sessions = [session1, session2, session3, session4]

# # Now test your weekly_analyzer
# weekly_result = weekly_analyzer(weekly_sessions)
# print(weekly_result)
