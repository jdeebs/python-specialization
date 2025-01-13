from books.models import Book
# Imports for file object to display visual representations of analytics
from io import BytesIO
import base64
import matplotlib.pyplot as plt

def get_bookname_from_id(val):
    bookname = Book.objects.get(id=val)
    return bookname

def get_graph():
    # Create a BytesIO buffer for the image
    buffer = BytesIO()

    # Create a plot with a bytesIO object as a file-like object. Set format to png
    plt.savefig(buffer, format='png')

    # Set cursor to the beginning of the stream
    buffer.seek(0)

    # Retrieve the content of the file
    image_png = buffer.getvalue()

    # Encode the bytes-like object
    graph = base64.b64encode(image_png)

    # Decode to get the string as output
    graph = graph.decode('utf-8')

    # Free up memory of buffer
    buffer.close()

    # Return the image/graph
    return graph

def get_chart(chart_type, data, **kwargs):
    # Switch plot backend to AGG (Anti-Grain Geometry) - to write to file
    # AGG is preferred solution to write PNG files
    plt.switch_backend('AGG')

    # Specify figure size
    fig = plt.figure(figsize=(6,3))

    # Select chart_type based on user input from the form
    if chart_type == '#1':
        # Plot bar chart between date on x-axis and quantity on y-axis
        plt.bar(data['date_created'], data['quantity'])

    elif chart_type == '#2':
        # Generate pie chart based on the price
        # Book titles are sent from the view as labels
        labels = kwargs.get('labels')
        plt.pie(data['price'], labels=labels)

    elif chart_type == '#3':
        # Plot line chart based on date on x-axis and price on y-axis
        plt.plot(data['date_created'], data['price'])
    
    else:
        print('unknown chart type')

    # Specify layout details
    plt.tight_layout()

    # Render the graph to file
    chart = get_graph()
    return chart