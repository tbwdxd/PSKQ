/*Ver 0.1
Author: Bowen, Yijie
Usage: scalac PSKQ_STP_ver_0.1.scala >> scala PSKQ

*****This is a single-node version, without utilizing Spark*****

*/

//Need to use the java json library
//import org.json.*;
import org.json4s._ 
import org.json4s.native.JsonMethods._ 
//actuall code

/*
Generator Filter
Keyword Match Processor
Popularity Evaluator
Spatial Constraint Processor
PSK Randk Evaluator
*/

import org.apache.spark.graphx._
// Import random graph generation library
import org.apache.spark.graphx.util.GraphGenerators
// A graph with edge attributes containing distances
val graph: Graph[Int, Double] =
  GraphGenerators.logNormalGraph(sc, numVertices = 100).mapEdges(e => e.attr.toDouble)
val sourceId: VertexId = 42 // The ultimate source
// Initialize the graph such that all vertices except the root have distance infinity.
val initialGraph = graph.mapVertices((id, _) => if (id == sourceId) 0.0 else Double.PositiveInfinity)
val sssp = initialGraph.pregel(Double.PositiveInfinity)(
  (id, dist, newDist) => math.min(dist, newDist), // Vertex Program
  triplet => {  // Send Message
    if (triplet.srcAttr + triplet.attr < triplet.dstAttr) {
      Iterator((triplet.dstId, triplet.srcAttr + triplet.attr))
    } else {
      Iterator.empty
    }
  },
  (a,b) => math.min(a,b) // Merge Message
  )
println(sssp.vertices.collect.mkString("\n"))