/*Ver 0.1
Author: Bowen, Yijie
Usage: scalac PSKQ_STP_ver_0.1.scala >> scala PSKQ

*****This is a single-node version, without utilizing Spark*****

*/
package PSKQ

/*
Generator Filter
Keyword Match Processor
Popularity Evaluator
Spatial Constraint Processor
PSK Randk Evaluator
*/

object PSKQ_shortest_path extends App {
  //Need to use the java json library
  //import org.json.*;
  import org.json4s._ 
  import org.json4s.JsonDSL._
  import org.json4s.jackson.JsonMethods._
  //actuall code

  def main{
    case class Winner(id: Long, numbers: List[Int])
    case class Lotto(id: Long, winningNumbers: List[Int], winners: List[Winner], drawDate: Option[java.util.Date])

    val winners = List(Winner(23, List(2, 45, 34, 23, 3, 5)), Winner(54, List(52, 3, 12, 11, 18, 22)))
    val lotto = Lotto(5, List(2, 45, 34, 23, 7, 5, 3), winners, None)

    val json =
      ("lotto" ->
      ("lotto-id" -> lotto.id) ~
      ("winning-numbers" -> lotto.winningNumbers) ~
      ("draw-date" -> lotto.drawDate.map(_.toString)) ~
      ("winners" ->
        lotto.winners.map { w =>
          (("winner-id" -> w.id) ~
           ("numbers" -> w.numbers))}))

    println(compact(render(json)))
  }
}

//TODO
/*object {
  /*val edges1 List = ();
  val verticies1 List= ();
  val edges2 List= ();
  val verticies2 List= ();*/


  def load_json();
}*/