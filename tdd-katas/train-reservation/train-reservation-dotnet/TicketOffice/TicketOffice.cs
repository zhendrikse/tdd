using System;
using System.Text;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;

namespace TicketOffice;

public class TicketOffice
{
    public int FirstNumber { set; private get; }
    public int SecondNumber { set; private get; }

    public int Add()
    {
        return FirstNumber + SecondNumber;
    }

    public void CancelReservation(string traindId, string booking_reference) {
        ResetTrain(traindId);
    }

    public string ReserveSeats(string stringId, int seats)
    {
        return "{\"train_id\": \"express_2000\", \"booking_reference\": \"75bcd15\", \"seats\": [\"1A\", \"1B\"]}";
    }

    static void ResetTrain(string trainId)
    {
        var URL = "http://localhost:5091/reset/" + trainId;
        var requestMessageContent = new StringContent("", Encoding.UTF8, "application/json");

        HttpClient client = new HttpClient();
        client.BaseAddress = new Uri(URL);
        HttpResponseMessage response = client.PostAsync(URL, requestMessageContent).Result;
        if (response.IsSuccessStatusCode)
        {
            var trainInfo = response.Content.ReadAsStringAsync().Result;
            // Console.WriteLine("Reservation with booking reference {0} successfully made", bookingReference);
        }
        else 
        {
            Console.WriteLine("{0} ({1})", (int)response.StatusCode, response.ReasonPhrase);
        }
        client.Dispose();    
    }

    static void Main(string[] args)
    {
        Console.WriteLine("Put your code to make the ticket office a REST service right here");
    }

}
