import sys

input = sys.stdin.readline

n = int(input())

seminar = {'Algorithm':204, 'DataAnalysis':207, 'ArtificialIntelligence':302, 'CyberSecurity':101, 'Network':303, 'Startup':501, 'TestStrategy':105}

for _ in range(n):
    select = input().strip()
    if select == 'CyberSecurity':
        print('B'+str(seminar[select]))

    else:
        print(seminar[select])
