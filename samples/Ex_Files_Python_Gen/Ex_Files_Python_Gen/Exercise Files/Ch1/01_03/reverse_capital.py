# list of names
names_list = ['Adam','Anne','Barry','Brianne','Charlie','Cassandra','David','Dana']

# too long
# reverse_uppercase = (name[::-1] for name in (name.upper() for name in names_list))

# breaking it up 
uppercase = (name.upper() for name in names_list)
reverse_uppercase = (name[::-1] for name in upper_case)


