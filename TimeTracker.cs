const string timeStampList =
    """
    10:19-17:48
    9:14-18:23
    9:08-18:12
    9:30-17:31
    """;

var startTimeFriday = TimeSpan.Parse("9:35");
var overtimeLastWeek = TimeSpan.Parse("14:49") - TimeSpan.Parse("12:27");

var overtimeList = timeStampList.Split('\n').Select(st =>
{
    var startAndEndArray = st.Split('-');
    var start = TimeSpan.Parse(startAndEndArray[0]);
    var end = TimeSpan.Parse(startAndEndArray[1]);
    return end - start - TimeSpan.FromHours(7);
}).ToList();

Console.WriteLine("From last week: " + overtimeLastWeek);
overtimeList.ForEach(ot => Console.WriteLine(ot));

var totalOvertime = overtimeList.Aggregate(TimeSpan.Zero, (current, overtime) => current + overtime);
totalOvertime += overtimeLastWeek;
Console.WriteLine("Total: " + totalOvertime);

var timeToWorkOnFriday = TimeSpan.FromHours(7) - totalOvertime;
Console.WriteLine("Time to work on Friday: " +  timeToWorkOnFriday);

Console.WriteLine($"arr: {startTimeFriday} => go: {startTimeFriday + timeToWorkOnFriday}");
