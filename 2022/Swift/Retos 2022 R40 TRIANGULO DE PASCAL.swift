
func pascalTriangle(size: Int) {

    if size < 0 {
        return
    }
    
    var lastRow: [Int] = []

    for row in 0..<size {

        var currentRow: [Int] = []

        var triangleRow = ""

        for element in 0...row {

            if element > 0 && element < row {
                let value = lastRow[element - 1] + lastRow[element]
                triangleRow += "\(value) "
                currentRow.append(value)
            } else {
                triangleRow += "1 "
                currentRow.append(1)
            }
        }
        print(String(repeating: " ", count: size - row) + triangleRow)

        lastRow = currentRow
    }
}

pascalTriangle(size: 10)