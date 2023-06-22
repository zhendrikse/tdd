class StatementPrinter:
  def print_header(customer_name):
    return "Rental Record for " + customer_name 

  def print_amount(amount_as_string):
    return "You owed " + amount_as_string

  def print_renter_points(frequent_renter_points_as_string):
    return "You earned " + frequent_renter_points_as_string + " frequent renter points"			

class TextStatementPrinter:

  @staticmethod
  def print(statement_data):
    result = StatementPrinter.print_header(statement_data.name)
    result += "\n"
    
    for i in range(len(statement_data.movie_titles)):
      result += "\t" + statement_data.movie_titles[i] + "\t" + "{:.1f}".format(statement_data.rental_amounts[i]) + "\n"
		
    result += StatementPrinter.print_amount("{:.1f}".format(statement_data.amount_owed))
    result += "\n"
    result += StatementPrinter.print_renter_points(str(statement_data.frequent_renter_points)) 
    return result

class HtmlStatementPrinter:
  
  @staticmethod
  def print(statement_data):
    result = "<h1>" + StatementPrinter.print_header("<em>"+ statement_data.name + "</em></h1>")
    result += "\n"
    
    result += "<table>\n"
    for i in range(len(statement_data.movie_titles)):
      result += "\t<tr><td>" + statement_data.movie_titles[i] + "</td><td>" + "{:.1f}".format(statement_data.rental_amounts[i]) + "</td></tr>\n"
    result += "</table>\n"
    
    result += "<p>" + StatementPrinter.print_amount("<em>" + "{:.1f}".format(statement_data.amount_owed) + "</em></p>")
    result += "\n"
    result += "<p>" + StatementPrinter.print_renter_points("<em>" + str(statement_data.frequent_renter_points) + "</em>") + "</p>"
    return result
