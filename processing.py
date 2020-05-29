import json

irrelevant_fields = [
    'user_id',
    'external_id',
    'profile_url',
    'name',
    'year_of_birth',
    'gender',
    'ethnicity',
    'connections',
    'city',
    'country',
    'languages',
    'core_values',
    'related_people',
    'last_updated'
]

guide_fields = [
    'primary_skill',
    'secondary_skill',
    'raw_skills',
    'industry',
    'bio'
]

high_importance_fields = [
    'patents',
    'publications'
]

low_importance_fields = [
    'recommendations',
    'awards',
    'certifications',
    'volunteering',
    'groups',
    'courses_taken'
]

degrees = {
    0:'unknown',
    1:'High School',
    2:'Vocational',
    3:'Associate Degree',
    4:'Undergraduate',
    5:'Masters Degree',
    6:'MBA Equiv.',
    7:'Ph.D Equiv.'
}

curr = 0

#no longer in use
def print_person(n):
    file1 = open('profile_data/data_analysis_random_profiles.json')
    for _ in range(n):
        line = file1.readline()
    person = json.loads(line)
    for key in person.keys():
        if key == 'experience':
            print()
            experience_list = person[key]
            for exp in experience_list:
                print(exp)
                print()
                for key2 in exp.keys():
                    print('    ' + key2 + ':')
                    print('        ' + str(exp[key2]))
        else:
            if key not in irrelevant_fields and person[key]:
                print(key + ':')
                print('    ' + str(person[key]))


def print_keys(dict, keys):
    for key in keys:
        if(dict[key]):
            print('\t' + key + ':')
            print('\t\t' + str(dict[key]))
    print()

def print_keys_indent(dict, keys):
    for key in keys:
        if(dict[key] and key!='level'):
            print('\t\t' + key + ':')
            print('\t\t\t' + str(dict[key]))
    print()

def print_exp_elem(title, content):
    print('\t' + title + ': ' + str(content))

def print_exp_elem_indent(title, content):
    print('\t' + title + ':')
    print('\t\t' + str(content))

def print_exp(exp):
    role_exists = True if exp['role'] else False

    if role_exists:
        print_exp_elem('role', exp['role']['original'])
    else:
        print_exp_elem('role', 'NONE')

    print()
    print_exp_elem('org', exp['org'])
    print()
    
    if exp['is_edu']:
        print('\teducation data:')
        if exp['role'] and exp['role']['level']:
            print('\t\tlevel:')
            print('\t\t\t' + degrees[exp['role']['level']])
    else:
        print('\tjob data:')
    if role_exists:
        print_keys_indent(exp['role'], exp['role'].keys())
    
    print()
    print('\tfrom ' + exp['start'] + ' to ' + exp['end'])

def exp_key(exp):
    if exp['current_job']:
        return 1111111
    if len(exp['start']) != 10:
        return 0
    else:
        day = int(exp['start'][8:10], 10)
        month = int(exp['start'][5:7], 10)
        year = int(exp['start'][0:4], 10)
        return day + month*32 + year*500

def print_highs(start, end):
    how_many = 1 + end - start 
    for i in range(how_many):
        print_high(end - i)

def print_lows(start, end):
    how_many = 1 + end - start 
    for i in range(how_many):
        print_low(end - i)

def print_high(n):
    file1 = open('profile_data/data_analysis_random_profiles.json')
    for _ in range(n):
        line = file1.readline()
    person = json.loads(line)
    print('-------------------------------------')
    print(str(n) + ' FIELDS:')
    print_keys(person, high_importance_fields)

def print_low(n):
    file1 = open('profile_data/data_analysis_random_profiles.json')
    for _ in range(n):
        line = file1.readline()
    person = json.loads(line)
    print('-------------------------------------')
    print(str(n) + ' FIELDS:')
    print_keys(person, low_importance_fields)

def print_person_new(n):

    print('person #' + str(n))
    global curr
    curr = n

    file1 = open('profile_data/data_analysis_random_profiles.json')
    for _ in range(n):
        line = file1.readline()
    person = json.loads(line)

    for _ in range(9):
        print('__________________________________________________________________________')
    print('______________________________START HERE__________________________________')
    for _ in range(9):
        print('__________________________________________________________________________')


    print('GUIDE FIELDS:')
    print_keys(person, guide_fields)

    print('HIGH IMPORTANCE FIELDS:')
    print_keys(person, high_importance_fields)

    print('LOW IMPORTANCE FIELDS:')
    print_keys(person, low_importance_fields)

    print('EXPERIENCE:')
    exps = person['experience']
    for exp in exps:
        print_exp(exp)
        print('----------------------------------------------')
    print('total exp count:' + str(len(exps)))
    print('----------------------------------------------')

def next():
    global curr
    print_person_new(curr)
    curr = curr + 1