from functions import read_localfile,get_prev_last_name,sort_name,get_sorted_name,write_localfile

if __name__ == "__main__":
	s = input("Input filename to sort: ")
	print (write_localfile(get_sorted_name(sort_name(sort_name(get_prev_last_name(read_localfile(s)),1),2)),'sorted-names-list.txt'))

