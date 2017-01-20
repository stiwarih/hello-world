#http://stackoverflow.com/questions/33856411/how-to-join-two-rdds-by-a-key

val rdd1 = sc.textFile("input/myFile1.txt")
val rdd2 = sc.textFile("input/myFile2.txt")

val data1 = rdd1.map(line => line.split(",").map(elem => elem.trim))
val data2 = rdd2.map(line => line.split(",").map(elem => elem.trim))

val pairRdd1 = data1.map(r => (r(0), r))  /** zero index is the animal type which is the key in file 1*/
val pairRdd2 = data2.map(r => (r(0), r))  /** zero index is the animal type which is the key in file 2 as well */

val joined = pairRdd1.join(pairRdd2)

val local = joined.collect()
local.foreach{case (k, v) => {
  print(k + " : ")
  println(v._1.mkString("|") + "|" + v._2.mkString("|"))
}}
