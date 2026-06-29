from role_requirements import ROLE_SKILLS

def find_skill_gap(user_skills, target_role):

    required_skills = ROLE_SKILLS.get(target_role, [])

    missing_skills = []

    for skill in required_skills:

        if skill not in user_skills:
            missing_skills.append(skill)

    return missing_skills