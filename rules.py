#This class contains the logical rules that are inherent to the problem.
#The methods take an arriving input, leaving input, and a boat
#to make sure that when the boat contains certain people, certain
#conditions must be met to create the node.
#The functions return true if the node is logically possible,
#and false if not.


# 3 couple case
def rules_3couple(arriving, leaving, boat):
   # if b is only thing in boat
   if boat == 'b':
       if 'B' in arriving:      #If 'B' is in the arriving node
           return True
       elif 'A' not in arriving and'C' not in arriving:
           return True

   if boat == 'a':
       if 'A' in arriving:
           return True
       elif 'B' not in arriving and 'C' not in arriving:
           return True

   if boat == 'c':
       if 'C' in arriving:
           return True
       elif 'B' not in arriving and'A' not in arriving:
           return True

   if boat == 'A':
       if (('a' in leaving and 'B' not in leaving)
           or ('a' in leaving and 'C' not in leaving)
           or ('a' in leaving and 'B' not in leaving and 'C' not in leaving)) \
           and ('a' in arriving or ('B' in arriving and 'b' in arriving) or ('C' in arriving and 'c' in arriving)):
               return True

   if boat == 'B':
       if (('b' in leaving and 'A' not in leaving)
           or ('b' in leaving and 'C' not in leaving)
           or ('b' in leaving and 'A' not in leaving and 'C' not in leaving)) \
           and ('b' in arriving or ('A' in arriving and 'a' in arriving) or ('C' in arriving and 'c' in arriving)):
               return True

   if boat == 'C':
       if (('c' in leaving and 'A' not in leaving)
           or ('c' in leaving and 'B' not in leaving)
           or ('c' in leaving and 'A' not in leaving and 'B' not in leaving)) \
           and ('c' in arriving or ('A' in arriving and 'a' in arriving) or ('B' in arriving and 'b' in arriving)):
               return True

   if 'a' in boat and 'b' in boat:
       if 'A' in arriving and 'B' in arriving:
           return True
       if arriving == ('c'):
           return True
       elif arriving == (''):
           return True
       else:
           return False

   if 'b' in boat and 'c' in boat:
       if 'B' in arriving and 'C' in arriving:
           return True
       if arriving == ('a'):
           return True
       elif arriving == (''):
           return True
       else:
           return False

   if 'a' in boat and 'c' in boat:
       if 'A' in arriving and 'C' in arriving:
           return True
       if arriving == ('b'):
           return True
       elif arriving == (''):
           return True
       else:
           return False

   if 'A' in boat and 'B' in boat:
       if 'C' in leaving:
           if 'a' in leaving or 'b' in leaving:
               return False
       if 'c' in arriving:
           if 'C' not in arriving:
               return False
       return True

   if 'A' in boat and 'C' in boat:
       if 'B' in leaving:
           if 'a' in leaving or 'c' in leaving:
               return False
       if 'b' in arriving:
           if 'B' not in arriving:
               return False
       return True

   if 'B' in boat and 'C' in boat:
       if 'A' in leaving:
           if 'b' in leaving or 'c' in leaving:
               return False
       if 'b' in arriving:
           if 'B' not in arriving:
               return False
       return True

   if 'A' in boat and 'a' in boat:
       if 'b' in arriving and 'B' not in arriving:
           return False
       if 'c' in arriving and 'C' not in arriving:
           return False
       return True

   if 'B' in boat and 'b' in boat:
       if 'a' in arriving and 'A' not in arriving:
           return False
       if 'c' in arriving and 'C' not in arriving:
           return False
       return True

   if 'C' in boat and 'c' in boat:
       if 'b' in arriving and 'B' not in arriving:
           return False
       if 'a' in arriving and 'A' not in arriving:
           return False
       return True

   return False

#Rules for 2 couple
def rules_2couple(arriving, leaving, boat):
  if boat == 'A':
      if ('a' in leaving and 'B' in arriving and 'b' in arriving) or ('a' in arriving and 'B' in leaving and 'b' in leaving):
          return True
  if boat == 'B':
      if ('b' in leaving and 'A' in arriving and 'a' in arriving) or ('b' in arriving and 'A' in leaving and 'a' in leaving):
          return True
  if boat == 'a':
      if ('b' in arriving and 'A' in leaving and 'B' in leaving) or (arriving == "") or ("A" in arriving):
          return True
  if boat == 'b':
      if ('a' in arriving and 'A' in leaving and 'B' in leaving) or (arriving == "") or ("B" in arriving):
          return True
  if boat == 'AB' or boat == 'Aa' or boat == 'Bb':
      return True
  if boat == 'ab':
      if arriving == '' or ('A' in arriving and 'B' in arriving):
          return True
  return False