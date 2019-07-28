# Dream 11 ANAGRAMS
#Two Strings are anagrams if they are Permutations of each other.
#Result will be in alphabetical ascending order

def remove_duplicates(arr):
   tmp_dict = {}
   for i in range(0, len(arr)):
      key = ''.join(sorted(arr[i]))
      if tmp_dict.get(key, ()):
         pass
      else:
         tmp_dict[key] = (i,0)
   all_vals = tmp_dict.values()
   final_arr = [arr[index] for (index,c) in all_vals]
   return sorted(final_arr)

arr = ['poke', 'okep', 'peko']
result_arr = remove_duplicates(arr)
print (result_arr)

