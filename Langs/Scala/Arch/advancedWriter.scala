import java.io.File
import java.io.PrintWriter

@main def adWriter(args: String*) =

    val fileWrite = new PrintWriter(new File("Myinfos.txt"))

    var name: String = args(0)
    var age: String = args(1)
    var student: String = if (args(2) == "yes") "I'm a student" else "I'm not a student"

    fileWrite.printf("My name is %s\nI have %s years old\nAnd %s",name,age,student)
     
    fileWrite.close()
