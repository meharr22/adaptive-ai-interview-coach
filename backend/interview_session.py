from database import cursor, conn
sessions = {}

def create_session():

    session_id = str(len(sessions) + 1)

    sessions[session_id] = {
        "scores": [],
        "questions_attempted": 0
    }

    return session_id


def update_session(
    session_id,
    score
):

    sessions[session_id]["scores"].append(
        score
    )

    sessions[session_id]["questions_attempted"] += 1

    avg = (
        sum(
            sessions[session_id]["scores"]
        )
        /
        len(
            sessions[session_id]["scores"]
        )
    )

    return avg


def get_session(
    session_id
):

    return sessions.get(
        session_id
    )

def save_history_to_db(
    session_id,
    report
):

    cursor.execute(
        """
        INSERT INTO interview_history(
            session_id,
            average_score,
            verdict
        )
        VALUES (?, ?, ?)
        """,
        (
            session_id,
            report["average_score"],
            report["verdict"]
        )
    )

    conn.commit()
    
def get_history_from_db():

    cursor.execute(
        """
        SELECT *
        FROM interview_history
        """
    )

    return cursor.fetchall()
