using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;

namespace TicketOffice;

// public class DataObject
// {
//     public string? Name { get; set; }
// }

public class TicketOffice
{
    public int FirstNumber { set; private get; }
    public int SecondNumber { set; private get; }

    public int Add()
    {
        return FirstNumber + SecondNumber;
    }

    public string ReserveSeats(string stringId, int seats)
    {
        return "{\"train_id\": \"express_2000\", \"booking_reference\": \"75bcd15\", \"seats\": [\"1A\", \"1B\"]}";
    }

    static void Main(string[] args)
    {
        var URL = "http://localhost:5041/booking_reference";
        var urlParameters = "";

        HttpClient client = new HttpClient();
        client.BaseAddress = new Uri(URL);
        HttpResponseMessage response = client.GetAsync(urlParameters).Result;
        if (response.IsSuccessStatusCode)
        {
            // Parse the response body.
            //var dataObjects = response.Content.ReadAsAsync<IEnumerable<DataObject>>().Result;
            // foreach (var d in dataObjects)
            // {
            //     Console.WriteLine("{0}", d.Name);
            // }
            var bookingReference = response.Content.ReadAsStringAsync().Result;
            Console.WriteLine("Booking reference fetched: {0}", bookingReference);
        }
        else 
        {
            Console.WriteLine("{0} ({1})", (int)response.StatusCode, response.ReasonPhrase);
        }
        client.Dispose();
    }
}
