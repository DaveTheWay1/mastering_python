
# ? Define a list named scores that contains a dictionary with the following shape:
#  scores = [
#    {
#      'name': 'name of the player',
#      'points': 25  # points the player scored
#    }
#  ]
# Next, using append(), to add an additional “score” dictionary to the scores list.
# Iterate over the items in the scores list and print a string with this format
#  <name> scored <points> points
# for each dictionary item in the list.

scores = [
  {
    'name': 'david',
    'points': 25  # points the player scored
  }
]

scores.append({'name':'gisselle', 'points':32})
print(scores)

for score in scores:
  print(f"name: {score['name']}, score: {score['points']}")