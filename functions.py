from operator import itemgetter

def read_localfile(file):
	
	f = open(file,"r")
	contents = f.read()
	lines = contents.splitlines()
	f.close()
	print("==================================================== Unsorted =====================================")
	print ('\n'.join(lines)) 
	return lines
	
def get_prev_last_name (content):
	arr_multi=[]
	length = len(content) 
	for i in range(length):
		#print(content[i],"length:",len(content[i]))
		#print("Complete Name:",content[i])
		name = content[i]
		#arr_content.append(name)
		name_length = len(name)
		count=0
		space_count=0
		space_pos=0
		arr=[]

		for element in name: 
			if element ==' ':
				#print ("Substring space found at index:", result) 
				space_pos = result
				space_count=space_count+1
				arr.append(space_pos)
				
				
			count = count + 1
			result=count
		#print(arr)
		length_arr = len(arr)
		
		j=0
		while j <= length_arr: 
				if j==length_arr-1:	
				#print(arr[j-1],arr[j]) 
					prev_name_start=(arr[j-1])
					prev_name_end=(arr[j])+1
					#print ("Prev Name End:", prev_name_end) 
					#print ("Prev Name Start:", prev_name_start) 
					if prev_name_start+1 != prev_name_start+(prev_name_end-prev_name_start):
						#print ("Prev Name:",name[prev_name_start+1:prev_name_start+(prev_name_end-prev_name_start)-1])
						prev_name=name[prev_name_start+1:prev_name_start+(prev_name_end-prev_name_start)-1]
						#arr_content.append(prev_name)
					elif prev_name_start+1 == prev_name_start+(prev_name_end-prev_name_start):
						#print ("Prev Name:",name[0:prev_name_start])
						prev_name=name[0:prev_name_start]
						#arr_content.append(prev_name)
				j = j+1	
				
		latest_space = space_pos+1
		#print ("Last index:",latest_space)
		
		#print ("Last Name:",name[latest_space:],"\n")
		last_name=name[latest_space:]
		arr_multi.append([])	
		arr_multi[i].append(name)
		arr_multi[i].append(prev_name)
		arr_multi[i].append(last_name)	
	#print(arr_multi)
	return arr_multi 
	
def sort_name (content,key):

	return sorted(content,key=itemgetter(key))

def get_sorted_name(content):
	length = len(content)
	lines =[]
	for i in range(length):
		lines.append(content [i][0])
	return lines
	
def write_localfile(lines,file):
	print("================================================= Sorted ===========================================")
	print ('\n'.join(lines))
	f = open(file,"w")
	for ele in lines: 
         f.write(ele +"\n") 
		 
		 
	f.close()
	return "============================================= Write Success ========================================"
	