import glob


# iterate files in directory
for txto in glob.glob('/Volumes/vrona_SSD/test_change/*.txt'):
  new = []
  #read input file
  with open(txto, 'r') as file :
    text = file.readline()
    while text:
      if text[0] == '1':
        new_class0 = text[0].replace('1', '0') + text[1:]
        new.append(new_class0)
      elif text[0] == '2':
        new_class1 = text[0].replace('2', '1') + text[1:]
        new.append(new_class1)
      elif text[0] == '3':
        new_class2 = text[0].replace('3', '2') + text[1:]
        new.append(new_class2)
      text = file.readline()


  with open(txto, 'w') as file:
    file.write(''.join(i for i in new))
    file.close()
