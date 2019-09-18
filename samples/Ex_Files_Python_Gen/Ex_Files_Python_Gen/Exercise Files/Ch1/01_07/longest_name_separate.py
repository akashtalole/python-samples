# adding separate_names generator as another stage in pipeline

def separate_names(names):
	for full_name in names:
		for name in full_name.split(' '):
			yield name


full_names = (name.strip() for name in open('names.txt'))
names = separate_names(full_names)
lengths = ((name, len(name)) for name in names)
longest = max(lengths, key=lambda x:x[1])

