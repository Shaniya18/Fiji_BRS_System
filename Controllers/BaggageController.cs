using Microsoft.AspNetCore.Mvc;
using FijiBRS_StaffDashboard.Models;
using Newtonsoft.Json;
using System.Text;

namespace FijiBRS_StaffDashboard.Controllers
{
    public class BaggageController : Controller
    {
        private readonly HttpClient _httpClient = new HttpClient();

        // UPDATED: Now pointing to your live Render API
        private readonly string _baseUrl = "https://fiji-brs-system.onrender.com/api/baggage/";

        public async Task<IActionResult> Index()
        {
            try
            {
                var response = await _httpClient.GetAsync(_baseUrl + "staff/");
                if (response.IsSuccessStatusCode)
                {
                    var jsonResponse = await response.Content.ReadAsStringAsync();
                    var baggageList = JsonConvert.DeserializeObject<List<Baggage>>(jsonResponse);

                    return View(baggageList ?? new List<Baggage>());
                }
            }
            catch
            {
                // UPDATED: Professional error message for the dashboard
                ViewBag.Error = "Remote API Service is currently unreachable. Please contact ICT Support.";
            }

            return View(new List<Baggage>());
        }

        [HttpPost]
        public async Task<IActionResult> LoadBaggage(string tagId)
        {
            try
            {
                // 1. Check if bag exists
                var checkResponse = await _httpClient.GetAsync(_baseUrl + $"track/{tagId}/");
                if (!checkResponse.IsSuccessStatusCode)
                {
                    return Json(new { success = false, message = "INVALID TAG ID", sound = "error" });
                }

                var content = await checkResponse.Content.ReadAsStringAsync();
                var bag = JsonConvert.DeserializeObject<Baggage>(content);

                // 2. Handle potential null bag object
                if (bag?.Status == "LOADED")
                {
                    return Json(new { success = false, message = "ALREADY LOADED", sound = "warning" });
                }

                // 3. Execute PATCH request to update Django via Render
                var updateData = new { status = "LOADED" };
                var json = JsonConvert.SerializeObject(updateData);
                var patchRequest = new HttpRequestMessage(new HttpMethod("PATCH"), _baseUrl + $"staff/{tagId}/")
                {
                    Content = new StringContent(json, Encoding.UTF8, "application/json")
                };

                var updateResponse = await _httpClient.SendAsync(patchRequest);
                if (updateResponse.IsSuccessStatusCode)
                {
                    return Json(new { success = true, message = "LOAD SUCCESSFUL", sound = "success" });
                }

                return Json(new { success = false, message = "CLOUD UPDATE FAILED", sound = "error" });
            }
            catch
            {
                return Json(new { success = false, message = "NETWORK ERROR: CLOUD API OFFLINE", sound = "error" });
            }
        }
    }
}