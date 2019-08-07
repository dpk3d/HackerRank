/*
* Sorting a Array or List
*/

import scala.util.Sorting._

val arr = Array(7,5,1, 9,2)

val sort = scala.util.Sorting.quickSort(arr)

println(sort)


val deep = List(1, 2,3 ,4, 5, 62, 3,4,)

val sorting = deep.sortWith(_ < _)

println(sorting)

val deepak = List(4, 3, 8, 2, 67, 4)

val srt = deepak.sorted

println(srt)

// Sorting A Array in Place

val a = Array(7,5,1, 9,2) 

implicit class ArrayExtensions[A <: AnyRef](a: Array[A]) {
    /**
     * Sort a slice [from, until) of this array
     */
    def sort(from: Int, until: Int)(implicit cmp: Ordering[A]) = java.util.Arrays.sort(a, from, until, cmp)
}
a.slice(from, until).sorted.copyToArray(a, from)
