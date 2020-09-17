func calculateTime(from array:[Int], at index:Int) > Int {
    guard array.count > 0 && index > 0 && index index {
            seconds += min(array[i], array[index]-1)
        }
    }
    return seconds
}