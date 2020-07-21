/*
*
* Question 1 : Combining different type of Lists together.
* Expected Output:- 
* List(a1-green, a1-blue, b1-green, b1-blue, c1-green, c1-blue, a2-green, a2-blue, 
*       b2-green, b2-blue, c2-green, c2-blue, a3-green, a3-blue, b3-green, b3-blue, 
*       c3-green, c3-blue)
* Hint : We can Use Map and FlatMap
*/

  val numbers = List(1, 2, 3)

  val chars = List("a", "b", "c")

  val colors = List("green", "blue")

  val combinedList = chars.zip(numbers).map(x => x._1 + x._2)
  println(combinedList) // List(a1, b2, c3)

  val finalList = combinedList.flatMap(x => colors.map(b => x + b))
  println(finalList) // List(a1green, a1blue, b2green, b2blue, c3green, c3blue)

  val cross = numbers.flatMap(x => chars.map(y => (x + y)))
  println(cross) // List(1a, 1b, 1c, 2a, 2b, 2c, 3a, 3b, 3c)

  val finalCross = cross.flatMap(x => colors.map(y => (x + "-" + y)))
  println(finalCross) // This will give you the expected output.

/*
* Question 2: Reverse a List without using reverse method
*  Expected Output : List(-6,5,-4,3,2)
*  Hint : Use FoldLeft
*/
  val num = List(2, 3, -4, 5, -6)

  val result = num.foldLeft(num) { (a, b) => b :: a }.distinct
  
  println(result) // This will give you expected output.
