from wcwidth import wcswidth

emojis = ["🧨", "🎖️"]

for emoji in emojis:
  print(wcswidth(emoji))