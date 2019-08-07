/*
* Removing Duplicates in Array/List
*/

val String =   List("a", "b", "a", "c",  "a", "c")

val removingDuplicate = String.distinct

println(removingDuplicate) // List[java.lang.String] = List(a, b, c)

val rmDuplicate = String.toSet.toList

println( rmDuplicate ) //  List(a, b, c)

// We can do the same with Array also, We can use .distinct and .toSet.toArray

// Method to Remove Duplicate using FoldLeft

def removeDup[A](list:List[A]):List[A] = 
  list.foldLeft(List[A]()) {
    case (acc, item) if acc.contains(item) => acc
    case (acc, item) => item::acc
  }  
  
  
