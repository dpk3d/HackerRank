/*
* IP Address Validation Hacker Rank.
*
*/

def validateAddresses(addresses: Array[String]): Array[String] = {
  // Write your code here
  val ipv4 = """^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$""".r
  val ipv6 = """^[0-9abcdef]{1,4}\:[0-9abcdef]{1,4}\:[0-9abcdef]{1,4}\:[0-9abcdef]{1,4}\:[0-9abcdef]{1,4}\:[0-9abcdef]{1,4}\:[0-9abcdef]{1,4}\:[0-9abcdef]{1,4}$""".r
  addresses map { l =>
    (ipv4 findFirstIn l).map(_ => "IPv4").getOrElse((ipv6 findFirstIn l).map(_ => "IPv6").getOrElse("Neither"))
  }
}
