class Node():
	def __init__(self, value, is_end=False):
		self.value = value
		self.is_end = is_end

class NorvigWordTree():
	"""A data structure that will generate a tree given
	the file format <word> <frequency_count> and provide a
	function to determine whether or not a word is in the tree
	"""
	def __init__(self, filename):
		self.__words = self.__get_words_from_file(filename)
		self.__root = self.__buildTree()

	def __get_words_from_file(self, filename):
		"""Receives a filename and returns a set of words
			the format of the file in filename must be
			<word>	<frequency_count>
		""" 
		words = set()
		for line in open(filename):
			word, _ = line.split()
			words.add(word.upper())
		return words

	def __buildTree(self):
		"""Builds a tree where each node represents a letter.  Each
		node will have children that, when combined with the path up to the parent
		will make a word. a->p->p->l->e and a->p->e together will represent 6 nodes
		"""
		root = Node("")
		for word in self.__words:
			current = root
			for letter in word:
				if not hasattr(current, letter):
					setattr(current, letter, Node(letter))
				current = getattr(current, letter)
			current.is_end = True
		return root

	def exists(self, word):
		"""Consumes one letter at a time while descending down
		the letter tree until the end is reached or until a node
		fails to contain an expected child (the word doesn't exist)
		"""
		word = word.upper()
		exists = False
		current = self.__root
		for letter in word:
			if hasattr(current, letter):
				current = getattr(current, letter)
			else:
				break
		else:
			if current.is_end:
				exists = True
		return exists

def test():
	return NorvigWordTree("norvigWords.txt")


if __name__ == '__main__':
	test()

