def get_labels(current):
    current_month = current.month + 1
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    labels = {}
    while len(labels) < 12:
        labels[current_month] = months[current_month - 1]
        if current_month < 12:
            current_month += 1
        else:
            current_month = 1
    return labels