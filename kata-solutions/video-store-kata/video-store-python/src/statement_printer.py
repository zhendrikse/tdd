class StatementPrinter:
  @staticmethod
  def print(statement_data, html = False):
    result = "<h1>" if html else "" 
    result += "Rental Record for " + ("<em>" if html else "") + statement_data.name + ("</em></h1>" if html else "") + "\n"
    
    result += "<table>\n" if html else "" 
    for i in range(len(statement_data.movie_titles)):
      result += "\t" + ("<tr><td>" if html else "") + statement_data.movie_titles[i] + ("</td><td>" if html else "\t") + "{:.1f}".format(statement_data.rental_amounts[i]) + ("</td></tr>" if html else "") + "\n"
    result += "</table>\n" if html else ""
    
    result += "<p>" if html else ""
    result += "You owed " + ("<em>" if html else "") + "{:.1f}".format(statement_data.amount_owed) 
    result += "</em></p>" if html else ""
    result += "\n"
    
    result += "<p>" if html else ""
    result += "You earned "+ ("<em>" if html else "") + str (statement_data.frequent_renter_points) + ("</em>"  if html else "") + " frequent renter points"
    result += "</p>" if html else ""
    return result
    