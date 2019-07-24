// Using Recursion

/** Unsafe, fails for empty lists. */
def maximums(list: List[Int]): List[Int] = { 
  @annotation.tailrec
  def loop(remaining: List[Int], acc: List[Int], excludedValues: Set[Int]): List[Int] = remaining match {
    case _ :: Nil =>
      acc.reverse
      
    case x :: xs =>
      val newMaximum = findMaximum(remaining, excludedValues)
      loop(remaining = xs, newMaximum :: acc, excludedValues + newMaximum)
  }
  
  loop(remaining = list, acc = List.empty, excludedValues = Set.empty)
}

/** Unsafe, fails for empty lists. */
def findMaximum(list: List[Int], excludedValues: Set[Int]): Int = {
  @annotation.tailrec
  def loop(remaining: List[Int], currentMaximum: Int): Int = remaining match {
    case Nil =>
      currentMaximum
      
    case x :: xs =>
      if (x > currentMaximum && !excludedValues.contains(x))
        loop(remaining = xs, currentMaximum = x)
      else
        loop(remaining = xs, currentMaximum)
  }
  
  loop(remaining = list, currentMaximum = Int.MinValue)
}

val l = List(16,17,4,5,3,0)

maximums(l).foreach(println)

// Output
/*
17
5
4
3
0
*/
