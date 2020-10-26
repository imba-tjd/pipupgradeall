import pkg_resources, subprocess
import os

def get_all_pythons():
    '''https://stackoverflow.com/a/52123490'''
    output, err = subprocess.Popen(
        ['which', '-a', 'python', 'python3','python2'], 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
        ).communicate()
    return output.decode('utf8').split('\n')[:-1]

def _main():
    
    all_pythons = []
    if os.name == 'posix':
        all_pythons = get_all_pythons()
    if not all_pythons:
        all_pythons = ['python']
    for py in all_pythons:
        subprocess.run([py, '-m', 'pip','install','-U',
            *[dist.project_name for dist in pkg_resources.working_set]
        ])
