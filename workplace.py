def movieTickets(groups): 
  # write your code here
  ans = ""

  for group in groups:
    adults, teens, children = list(map(int, group.split()))

    if adults > 1: 
      children = 0

    ans += str(adults * 25 + teens * 15 + children * 5) + "\n"

  return ans
