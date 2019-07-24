/* Input IS Array(16,17,4,5,3,0)
* Output is 17,5,5,3,0
*/

val input = List(16, 17, 4, 5, 3, 0)

//variation 1 with scan
val v1 = input.scanRight(Int.MinValue)(math.max).dropRight(1)
println("variation 1, with scan")
println(v1)
//variation 1 with for loop
locally {
  var max = Int.MinValue
  val buffer = new scala.collection.mutable.ArrayBuffer[Int](input.length)
  for (i <- input.reverse) {
    if(i > max) { max = i }
    max +=: buffer
  }
  println("variation 1, with for loop")
  println(buffer.toList)
}
//variation 2 with for loop
locally {
  var max = Int.MinValue
  val buffer = new scala.collection.mutable.ArrayBuffer[Int](input.length)
  for (i <- input.reverse if i >= max) {
    max = i
    i +=: buffer
  }
  println("variation 2, with for loop")
  println(buffer.toList)
}

//Output
/*
variation 1, with scan
List(17, 17, 5, 5, 3, 0)

variation 1, with for loop
List(17, 17, 5, 5, 3, 0)

variation 2, with for loop
List(17, 5, 3, 0)

*/
