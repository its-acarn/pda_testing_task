### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.
# There are 6 errors in total. 

```python

class CardGame:


  def checkforAce(self, card):
    if card.value = 1: #missing an '=' sign, it should have a "==".
      return true #true in python begins with a capital 'T'
    else #missing colon here.
      return false #false in python begins with a capital 'F'

  dif highest_card(self, card1 card2) #three errors on this line: misspelling of 'def' as 'dif' | missing comma between card1 and card2 arguments | missing colon after closing bracket.
    if card1.value > card2.value #missing colon here
      return card #this should be 'card1' and not just 'card'
    else #missing colon here
      return card2
 

 def cards_total(cards): #indentation error here
   total
   for card in cards:
     total += card.value
     return "You have a total of" + total #indentation here won't run correctly. It will only go through for loop once.


```
