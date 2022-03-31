

string message = "150-177-154-156-149-223-157-144-197-223-214";

message.Split('-')
    .Select(x => int.Parse(x))
    .Select(x => 255 - x)
    .Select(x => Convert.ToChar(x))
    .ToList().SwapEvery2<char>()
    .ForEach(x => Console.WriteLine(x));


public static class x
{
    public static List<T> SwapEvery2<T>(this List<T> list)
    {
        T temp = list[0];
        for (int i = 0; i < list.Count - 1; i++)
        {
            temp = list[i];
            list[i] = list[i + 1];
            list[i + 1] = temp;
            i++;
        }

        return list;
    }
}
