using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

namespace TicketOffice.Specs.Steps;

public record Train(Dictionary<string, Seat> seats)
{
}

public class Seat
{
    public string? coach { get; set; }
    public string? seat_number { get; set; }
    public string? booking_reference { get; set; }
}

public class RestCalls 
{
    public static Train MakeTrainSeatsReservationRestCall(string trainId, string booking_reference)
    {
        var URL = "http://localhost:5091/reserve";
        var requestMessageContent = new StringContent(
            "{\"train_id\":\"" + trainId + "\",\"seats\": [\"1A\", \"1B\"], \"booking_reference\": \"" + booking_reference + "\"}", Encoding.UTF8, "application/json");
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


    public static Train GetTrainSeatInformation(string trainId)
    {
        var URL = "http://localhost:5091/data_for_train/" + trainId;
        var urlParameters = "";
        var trainData = "";
        
        HttpClient client = new HttpClient();
        client.BaseAddress = new Uri(URL);
        HttpResponseMessage response = client.GetAsync(urlParameters).Result;
        if (response.IsSuccessStatusCode)
        {
            trainData = response.Content.ReadAsStringAsync().Result;
        }
        else 
        {
            Console.WriteLine("{0} ({1})", (int)response.StatusCode, response.ReasonPhrase);
        }
        client.Dispose();
        return JsonSerializer.Deserialize<Train>(trainData)!;
    }

    public static string SampleCodeForBookingReferenceRestCall() 
    {
        var URL = "http://localhost:5041/booking_reference";
        var urlParameters = "";
        var bookingReference = "";

        HttpClient client = new HttpClient();
        client.BaseAddress = new Uri(URL);
        HttpResponseMessage response = client.GetAsync(urlParameters).Result;
        if (response.IsSuccessStatusCode)
        {
            bookingReference = response.Content.ReadAsStringAsync().Result;
            Console.WriteLine("Booking reference fetched: {0}", bookingReference);
        }
        else 
        {
            Console.WriteLine("{0} ({1})", (int)response.StatusCode, response.ReasonPhrase);
        }
        client.Dispose();

        return bookingReference;
    }
}