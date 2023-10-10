#Q9 cacti.py question


def cacti_number(plot):
    if not isinstance(plot, list) or not all(isinstance(row, list) for row in plot):
        raise ValueError("Input must be a 2-D array.")

    # set counts of 0's and 1's in plot to 0
    availableCount = 0

    for i in range(len(plot)):
        for j in range(len(plot[i])):
            if plot[i][j] == 0:
                # Check adjacent positions (up, down, left, right)
                if i > 0 and plot[i - 1][j] == 1:
                    availableCount += 0 # Adjacent cacti above
                elif i < len(plot) - 1 and plot[i + 1][j] == 1:
                    availableCount += 0  # Adjacent cacti below
                elif j > 0 and plot[i][j - 1] == 1:
                    availableCount += 0  # Adjacent cacti to the left
                elif j < len(plot[i]) - 1 and plot[i][j + 1] == 1:
                    availableCount += 0  # Adjacent cacti to the right
                else:
                    plot[i][j] = 1
                    availableCount += 1
                
    return availableCount






