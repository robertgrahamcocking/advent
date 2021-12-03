def part1(items):

   count = 0

   for key,item in enumerate(items):
      if key != 0:
         if item - items[key-1] > 0:
            count += 1
   return(count)

def part2(items):

   count = 0

   for key,item in enumerate(items[:-3]):
      a = (items[key] + items[key+1] + items[key+2])
      b = (items[key+1] + items[key+2] + items[key+3])
      if b > a:
         count += 1

   return count
