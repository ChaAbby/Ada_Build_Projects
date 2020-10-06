student_names = ["TIMMY TURNER", "WANDA MAGIC", "COSMO MAGIC", "DOUG DIMMADOME", "TRIXIE TANG"]

student_id = list()

email_list = list()


def id_num():
    import random
    for id in range(0,5):
        id = random.randint(111111,999999)
        student_id.append(id)

def first_letter():
    name = 0
    letter = 0
    for name in range(len(student_names)):
        letter = student_names[name]
        word = student_names[name]
        x = word.find(" ")
        word = word[x+1:]
        letter = letter[0]
        id2 = student_id[name]
        id2 = str(id2)
        id2 = id2[3:6]
        string = f'{letter}{word}{id2}@email.com\n'
        print(string)
        email_list.append(string)

id_num()
first_letter()

def list_values():
  name = 0
  id3 = 0
  address = 0
  for name in range(len(student_names)):
      print(f'\nNAME: {student_names[name]}\n' f'ID: {student_id[id3]}\n' f'EMAIL: {email_list[address]}')
      id3 += 1
      address += 1


list_values()
