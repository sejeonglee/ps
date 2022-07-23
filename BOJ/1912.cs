var n = int.Parse(Console.ReadLine());

var arr = Console.ReadLine().Split().Select(s => int.Parse(s)).ToArray()[..n];

var dp = Enumerable.Repeat(0, n).ToArray();

dp[0] = arr[0];
arr.Select((value, index) => (value, index)).ToList()
    .ForEach( pair=>
    {
        var (value, index) = pair;
        if (index == 0) return;

        dp[index] = Math.Max(dp[index - 1] + value, value);
    });

var answer = dp.Max();
Console.WriteLine(answer);