temperatures = []
with open('lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))
    print(temperatures)

print('min temperature in aeroport Hitroy ', min(temperatures))
print('max temperature in aeroport Hitroy ', max(temperatures))
print('average temperature in aeroport Hitroy ',
      round((sum(temperatures) / len(temperatures)), 2))
sorted(temperatures)
pozition = int(len(temperatures) / 2)
print('number of elements in file', len(temperatures))
print('medial pozition', round(pozition, 0))
print('median temperatur in aeroport Hitroy', temperatures[pozition])
print('uniqu temperature ', len(set(temperatures)))
