from question_bank import QUESTION_BANK

def generate_questions(skills):

    questions = []

    for skill in skills:

        if skill in QUESTION_BANK:

            questions.extend(
                QUESTION_BANK[skill]
            )

    return questions[:10]