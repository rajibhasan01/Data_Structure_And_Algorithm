# insert value in an sorted array
def insert_value(list, inval):
   index = find_index(list, inval);
   # can be solve by online like below
   # list.insert(index, inval);
   if index == len(list):
      list.append(inval);
      return list;

   new_list = [];
   for i in range(len(list)):
      if i == index:
         new_list.append(inval);
      new_list.append(list[i]);
   return new_list;


def find_index(list, inval):
   index = 0;
   while index < len(list):
      if list[index] >= inval:
         return index;
      index += 1;
   return index;

array = list(map(int, input('Enter list value space separate: ').strip().split()));
inval = int(input('Enter the inserted value here: '));
print(insert_value(array, inval));


