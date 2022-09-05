var inputLine = Console.ReadLine();



string Process(string sentence)
{
  var characters = new[]{
        'U', 'C', 'P', 'C'
    };
  foreach (var c in characters)
  {
    var n = sentence.IndexOf(c);
    if (n == -1)
    {
      return "I hate UCPC";
    }

    sentence = sentence[(n + 1)..];
  }

  return "I love UCPC";
}

Console.WriteLine(Process(inputLine));