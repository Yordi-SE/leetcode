bool isPowerOfThree(int n)
{
    int t = n;
    if (t == 1)
        return true;
    if (t != 1 && t < 3)
        return false;
    else if (t == 1)
        return true;
    else if (t % 3 != 0)
        return false;
    t = n / 3;
    if (t != 0)
         return isPowerOfThree(t);
    return true;
}