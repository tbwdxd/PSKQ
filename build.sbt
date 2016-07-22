name := "PSKQ"

version :=  "0.1"

scalaVersion := "2.11.7"

libraryDependencies ++= Seq(
	"org.apache.spark" %% "spark-core" % "1.6.2",
	"org.json4s" %% "json4s-native" % "3.4.0",
	"org.apache.spark" % "spark-graphx_2.10" % "0.9.0-incubating"
)
