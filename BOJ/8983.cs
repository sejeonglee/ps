// See https://aka.ms/new-console-template for more information
// Main
ProblemCondition condition = InputModule.inputProblemCondition();
var answer = Enumerable.Range(1, condition.N)
                       .Where(i => InputModule.inputPoint().isInRange(condition))
                       .Count();
Console.WriteLine(answer);

// Declaration
class Point
{
  public int x { get; set; }
  public int y { get; set; }

  public bool isInRange(ProblemCondition condition)
  {
    var searchIndex = condition.firePoints.BinarySearch(this.x);
    int minDist = 0;
    if (searchIndex < 0)
    {
      var nextFirePoint = condition.firePoints.ElementAtOrDefault(-1 - searchIndex);
      var prevFirePoint = condition.firePoints.ElementAtOrDefault(-2 - searchIndex);

      var nextDist = nextFirePoint == default(int) ? int.MaxValue : euclideanDist(nextFirePoint);
      var prevDist = prevFirePoint == default(int) ? int.MaxValue : euclideanDist(prevFirePoint);
      minDist = Math.Min(nextDist, prevDist);
    }
    else
    {
      minDist = euclideanDist(condition.firePoints[searchIndex]);
    }
    return minDist <= condition.L;
  }

  private int euclideanDist(int firePointX)
  {
    return Math.Abs(this.x - firePointX) + this.y;
  }
}

class ProblemCondition
{
  public int M { get; set; }
  public int N { get; set; }
  public int L { get; set; }
  public List<int>? firePoints { get; set; }
}

class InputModule
{
  private static string[] readLineAndSplit()
  {
    string? inputString = Console.ReadLine();
    if (inputString == null)
    {
      throw new ArgumentNullException();
    }
    return inputString.Split();
  }

  public static ProblemCondition inputProblemCondition()
  {
    var firstArgs = readLineAndSplit();

    int M, N, L;
    int.TryParse(firstArgs[0], out M);
    int.TryParse(firstArgs[1], out N);
    int.TryParse(firstArgs[2], out L);

    var firePoints = new List<int>(
      readLineAndSplit().Select(s => int.Parse(s)).OrderBy(x => x)
    );

    return new ProblemCondition()
    {
      M = M,
      N = N,
      L = L,
      firePoints = firePoints
    };

  }

  public static Point inputPoint()
  {
    var s = readLineAndSplit();
    return new Point()
    {
      x = int.Parse(s[0]),
      y = int.Parse(s[1]),
    };
  }
}