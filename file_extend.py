import sql_tools as sq
import os
import shutil


def replicant(img_name, user_name, source, destination):              #Copy file from one destination, to another

    source = source +'/'+ img_name
    
    destination = destination + "/" + user_name
    try:
        if not os.path.exists(destination):
            os.makedirs(destination)
        shutil.copy(source, destination)
        print(img_name, 'copied successfully!')
    except:
        print(img_name, 'DENIED!')


id_list = sq.find_all_id()
# d template: 188A<number>.jpg
# a template: photo00-<number>.jpg

for i in range(2,10):
    row = (sq.find_by_id(i))[0]
    row_ch = []
    for j in range(len(row)):
        row_ch.append(row[j])
    #anastasia template
    for j in range(3, 7):
        if row_ch[j] != '0':
            row_ch[j] = 'photo00-'+str(row_ch[j])+'.jpg'
    #dmitriy template
    for j in range(7, 11):
        if row_ch[j] != '0':
            row_ch[j] = '188A'+str(row_ch[j])+'.jpg'

    #copy to anastasia
    for j in range(3, 7):
        if row_ch[j] != '0':
            replicant(row_ch[j], row_ch[1]+' '+row_ch[2] , '/home/maxomenes/Pictures/PhotoSortBase/a','/home/maxomenes/Pictures/PhotoSort/anastasia')
    a_file = open("/home/maxomenes/Pictures/PhotoSort/anastasia/"+row_ch[1]+' '+row_ch[2]+"/comment.txt", "w+")
    a_file.write(row_ch[11])
    a_file.close()

    #copy to dmitriy
    for j in range(7, 11):
        if row_ch[j] != '0':
            replicant(row_ch[j], row_ch[1]+' '+row_ch[2], '/home/maxomenes/Pictures/PhotoSortBase/d','/home/maxomenes/Pictures/PhotoSort/dmitriy')
    d_file = open("/home/maxomenes/Pictures/PhotoSort/dmitriy/"+row_ch[1]+' '+row_ch[2]+"/comment.txt", "w+")
    d_file.write(row_ch[12])
    d_file.close()

    
    
