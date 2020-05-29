import csv
import json

def make_features(path):
    data = []
    f = open(path)
    for _ in range(1000):
        line = f.readline()
        person = json.loads(line)
        exps = person['experience']
        for i, _ in enumerate(exps):
            data += [Features(person, i)]
    return data

class Features:
    def __init__(self, person, i):
        self.id = (person['user_id'], i)

        self.primary = person['primary_skill']['skill']
        self.secondary = person['secondary_skill']['skill']
        self.industry = person['industry']
        self.raw = [skill.lower() for skill in person['raw_skills']]

        self.num_pubs = len(person['publications'])
        self.num_patents = len(person['patents'])
        self.num_certifications = len(person['certifications'])
        self.num_experiences = i
        self.max_edu = 0
        degrees = [exp['role']['level'] for exp in person['experience'][0:i] if exp_has_edu_lvl(exp)]
        if degrees:
            self.max_edu = max(degrees)
        self.has_top100 = len([True for exp in person['experience'][0:i] if exp_has_top100(exp)]) > 0
        self.faculties = []
        for exp in person['experience'][0:i]:
            if exp_has_faculties(exp):
                self.faculties += [faculty.lower() for faculty in exp['role']['faculties']]
        self.majors = []
        for exp in person['experience'][0:i]:
            if exp_has_majors(exp):
                self.majors += [major.lower() for major in exp['role']['majors']]
        self.elite = len([True for exp in person['experience'][0:i] if exp_has_elite(exp)]) > 0
        self.elite_edu = person['elite_edu']

def only_trues(lst):
    return len(lst) > 0 and len([x for x in lst if x == False]) == 0

def exp_has_edu_lvl(exp):
    return exp['is_edu'] and exp['role'] and exp['role']['level']

def exp_has_top100(exp):
    return exp['is_edu'] and exp['role'] and exp['role']['top100']

def exp_has_faculties(exp):
    return exp['is_edu'] and exp['role'] and exp['role']['faculties']

def exp_has_majors(exp):
    return exp['is_edu'] and exp['role'] and exp['role']['majors']

def exp_has_elite(exp):
    return exp['is_edu'] and exp['role'] and exp['role']['elite']

