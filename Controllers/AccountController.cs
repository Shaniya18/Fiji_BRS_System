using Microsoft.AspNetCore.Mvc;
using System.Collections.Concurrent;

namespace FijiBRS_StaffDashboard.Controllers
{
    public class AccountController : Controller
    {
        // Thread-safe dictionaries to track attempts and lockout times without a DB
        private static readonly ConcurrentDictionary<string, int> _attempts = new();
        private static readonly ConcurrentDictionary<string, DateTime> _lockoutTimes = new();

        [HttpGet]
        public IActionResult Login()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Login(string username, string password)
        {
            var userKey = username?.ToLower() ?? "unknown";

            // 1. Check if user is currently locked out
            if (_lockoutTimes.TryGetValue(userKey, out DateTime lockTime))
            {
                if (DateTime.Now < lockTime)
                {
                    var timeLeft = lockTime - DateTime.Now;
                    ViewBag.LockoutMinutes = (int)Math.Ceiling(timeLeft.TotalMinutes);
                    return View("Lockout");
                }
                else
                {
                    // Lock expired, clean up
                    _lockoutTimes.TryRemove(userKey, out _);
                    _attempts.TryRemove(userKey, out _);
                }
            }

            // 2. Hardcoded Credentials for Fiji BRS Staff Demo
            // Username: staff_admin | Password: Fiji2026!
            if (username == "staff_admin" && password == "Fiji2026!")
            {
                _attempts.TryRemove(userKey, out _);
                // In a real app, we would set an Authentication Cookie here
                return RedirectToAction("Index", "Baggage");
            }

            // 3. Increment failed attempts
            int failedCount = _attempts.AddOrUpdate(userKey, 1, (key, count) => count + 1);

            if (failedCount >= 5)
            {
                _lockoutTimes[userKey] = DateTime.Now.AddMinutes(30);
                ViewBag.LockoutMinutes = 30;
                return View("Lockout");
            }

            ViewBag.Error = $"Invalid login. {5 - failedCount} attempts remaining before lockout.";
            return View();
        }

        public IActionResult Logout()
        {
            return RedirectToAction("Login");
        }
    }
}