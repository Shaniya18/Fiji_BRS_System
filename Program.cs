var builder = WebApplication.CreateBuilder(args);

// 1. Add services to the container (the "Engine" setup)
builder.Services.AddControllersWithViews();

var app = builder.Build();

// 2. Configure the HTTP request pipeline (the "Traffic" setup)
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles(); // Loads your CSS/Images

app.UseRouting();

app.UseAuthorization();

// 3. Set the Gate (App starts at Login page)
app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Account}/{action=Login}/{id?}");

app.Run();