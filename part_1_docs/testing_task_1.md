### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # comparative equality is "==" not "=", an assignment, and else doesn't have ":"
    # if card.value = 1:
      return True
    # else
      return False
   
# Key word "dif" should be "def", card variable should be card1.
# The if is not indented, the parameters are missing one comma after "card1".
  # dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    # return card
  else:
    return card2
  

# method should be indented and
# total should be initialised, not sure if python
# will allow the concatenating of different types
# if it doesn't conversion is needed - str(total)
# return should be de-indented

# def cards_total(self, cards):
  # total
  for card in cards:
    total += card.value
    # return "You have a total of" + total
  
```
