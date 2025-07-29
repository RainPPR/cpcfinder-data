import school
import student

if __name__ == '__main__':
    print('Fetching school data...')
    school.Main('./data/school')
    print('Fetching student data...')
    student.Main('./data/student')
    print('Data fetching completed.')
