@main def lista() =

    val frutas: List[String] = List("melancia","banana","abacaxi")

    println("List length: " + frutas.length)

    frutas.foreach(f => println("Fruta: " + f))

    // Tuple of five itens 
    val itens = new Tuple5(1,"Carro",true,'A',1.25)

    itens.productIterator.foreach(i => println("Item: " + i))
    
    println(itens._5)

    val t_infninte = (1,5,6,8,2,3,96,4,8,"Arroz","Frango",'A')

