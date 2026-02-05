using System;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using Newtonsoft.Json;

namespace FijiBRS_StaffDashboard.Models
{
    public class Baggage
    {
        // Centralized constant for aviation limits
        public const decimal StandardWeightLimit = 23.0m;

        [JsonProperty("tag_id")]
        [DisplayName("Baggage Tag ID")]
        public string TagId { get; set; } = string.Empty;

        [JsonProperty("passenger_name")]
        [DisplayName("Passenger Name")]
        public string PassengerName { get; set; } = string.Empty;

        [JsonProperty("weight_kg")]
        [DisplayName("Weight (kg)")]
        public decimal WeightKg { get; set; }

        [JsonProperty("status")]
        public string Status { get; set; } = "PENDING";

        [JsonProperty("updated_at")]
        [DisplayName("Last Updated")]
        public DateTime UpdatedAt { get; set; }

        [JsonProperty("flight_number")]
        [DisplayName("Flight Number")]
        public string FlightNumber { get; set; } = string.Empty;

        // --- COMPUTED PROPERTIES FOR UI LOGIC ---

        /// <summary>
        /// Logic for identifying heavy bags based on aviation standard.
        /// </summary>
        public bool IsOverweight => WeightKg > StandardWeightLimit;

        /// <summary>
        /// Returns a friendly description of the current status for tooltips or logs.
        /// </summary>
        public string StatusDescription => Status?.ToUpper() switch
        {
            "LOADED" => "Bag confirmed in aircraft hold",
            "CHECKED_IN" => "Bag accepted at check-in counter",
            "FLAGGED" => "Requires security or weight inspection",
            "PENDING" => "Awaiting handling",
            _ => "Status unknown"
        };

        /// <summary>
        /// Maps the status to a Bootstrap badge color class.
        /// </summary>
        public string StatusBadgeClass => Status?.ToUpper() switch
        {
            "LOADED" => "bg-success",           // Green
            "CHECKED_IN" => "bg-info text-dark", // Light Blue
            "PENDING" => "bg-secondary",        // Grey
            "FLAGGED" => "bg-warning text-dark",// Yellow
            _ => "bg-dark"                      // Default
        };
    }
}