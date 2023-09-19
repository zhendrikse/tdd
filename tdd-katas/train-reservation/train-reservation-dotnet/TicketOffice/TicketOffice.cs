using System;
using System.Text;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text.Json;

namespace TicketOffice;

public record Train(Dictionary<string, Seat> seats)
{
}

public class Seat
{
    public string? coach { get; set; }
    public string? seat_number { get; set; }
    public string? booking_reference { get; set; }
}

public class TicketOffice
{
    private readonly string TRAIN_DATA_URL = "http://localhost:5091/";

    public Train CancelReservation(string trainId, string booking_reference) {
        var URL = TRAIN_DATA_URL + "cancel";
        var requestMessageContent = new StringContent(
            "{\"train_id\":\"" + trainId + "\",\"booking_reference\": \"" + booking_reference + "\"}", Encoding.UTF8, "application/json");
        var trainInfo = "";

        HttpClient client = new HttpClient();
        client.BaseAddress = new Uri(URL);
        HttpResponseMessage response = client.PostAsync(URL, requestMessageContent).Result;
        
        if (response.IsSuccessStatusCode)
        {
            trainInfo = response.Content.ReadAsStringAsync().Result;
        }
        else 
        {
            Console.WriteLine("{0} ({1})", (int)response.StatusCode, response.ReasonPhrase);
        }
        client.Dispose();    
        return JsonSerializer.Deserialize<Train>(trainInfo)!;
    }

    public string ReserveSeats(string trainId, int seats)
    {
        return "{\"train_id\": \"" + trainId + "\", \"booking_reference\": \"75bcd15\", \"seats\": [\"1A\", \"1B\"]}";
    }

    static void Main(string[] args)
    {
        Console.WriteLine("Put your code to make the ticket office a REST service right here");
    }

}
