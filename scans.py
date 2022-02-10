import os, random
path = os.getcwd()

# def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
#     """
#     Call in a loop to create terminal progress bar
#     @params:
#         iterable    - Required  : iterable object (Iterable)
#         prefix      - Optional  : prefix string (Str)
#         suffix      - Optional  : suffix string (Str)
#         decimals    - Optional  : positive number of decimals in percent complete (Int)
#         length      - Optional  : character length of bar (Int)
#         fill        - Optional  : bar fill character (Str)
#         printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
#     """
#     total = len(iterable)
#     # Progress Bar Printing Function
#     def printProgressBar (iteration):
#         percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
#         filledLength = int(length * iteration // total)
#         bar = fill * filledLength + '-' * (length - filledLength)
#         print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
#     # Initial Call
#     printProgressBar(0)
#     # Update Progress Bar
#     for i, item in enumerate(iterable):
#         yield item
#         printProgressBar(i + 1)
#     # Print New Line on Complete
#     print()

files = [f for f in os.listdir(path) if f.endswith('.mp3')]
clean_files = [{'oldname':a, 'newname':a if len(a.split(' || ')) == 1 else a.split(' || ')[1]} for a in files]
sorted_files = sorted(clean_files, key=lambda d: (str.casefold, d['newname']))

acak = input("Acak playlist? y/n : ")
if(acak.lower() == 'y'):
    random.shuffle(sorted_files)

number = ["%04d" % x for x in range(1, len(files)+1)]
new_filenames = [{'oldname':file['oldname'], 'newname':''.join([number[index], ' || ', file['newname'].replace('[', '(').replace(']', ')')])} for index, file in enumerate(sorted_files)]
sorted_new_filenames = sorted(new_filenames, key=lambda d: d['newname'])

print('\nFound %d MP3 Files\n' % len(files))

m3u = open("playlist.m3u", "w")
txt = open("playlist.txt", "w")
# for newfilename in progressBar(sorted_new_filenames, prefix = 'Progress:', suffix = 'Complete', length = 50):
for newfilename in sorted_new_filenames:
    # print(newfilename['oldname'])
    # print(newfilename['newname'])
    os.rename(os.path.join(path, newfilename['oldname']), os.path.join(path, newfilename['newname']))
    m3u.write(newfilename['newname'])
    m3u.write('\n')
    txt.write(newfilename['newname'])
    txt.write('\n')
m3u.close()
txt.close()

print('Success generated playlist.m3u & playlist.txt')
