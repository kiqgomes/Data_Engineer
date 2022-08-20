import java.io.File
import java.io.PrintWriter

@main def arch() = 
    
    val arch = new File("test.txt") //If don't exist, this command creates too.

    val printWriter = new PrintWriter(arch)

    printWriter.write("Writing by my scala code")

    printWriter.close()