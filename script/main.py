import school
import student

if __name__ == '__main__':
    print('Fetching school data...')
    school.Main('./data/school.json')
    print('Fetching student data...')
    student.Main('./data/student.json')
    print('Data fetching completed.')
