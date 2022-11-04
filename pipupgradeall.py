import subprocess

def main():
    p = subprocess.run(['pip', 'list', '-o'], check=True, capture_output=True)

    data = p.stdout.decode()
    print(data)
    pkg = []

    for entry in data.splitlines()[2:]:
        pkg.append(entry.split()[0])

    if pkg:
        cmd = ['pip', 'install', '-U', *pkg]
        print(' '.join(cmd))
        subprocess.run(cmd, check=True)
    else:
        print('Up to date.')

if __name__ == '__main__':
    main()
