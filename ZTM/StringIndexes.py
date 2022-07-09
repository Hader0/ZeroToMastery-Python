stringIndex = "My name is Hayden"

introduction = f"Introduction: {stringIndex}"
print(introduction)

# [start:stop]
print(stringIndex[0:17])
print(stringIndex[0:])
print(stringIndex[:17])
print(stringIndex[::1])

# [start:stop:stepover]
print(stringIndex[0::2]) # Every secoond index is skipped

# Reverse a string
print(stringIndex[::-1])

