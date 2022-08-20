import scala.io.Source

@main def read() = 

    val archname = "test.txt"

    val source = Source.fromFile(archname)

    // while source.hasNext do  // Printing char by char
        // println(source.next) 
    
    for line <- source.getLines do // Printing lines
            println(line)

    source.close()